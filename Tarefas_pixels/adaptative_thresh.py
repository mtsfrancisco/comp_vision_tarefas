import cv2
import cv2.ximgproc
import numpy as np
from scipy.interpolate import griddata

# Step 1: Smooth the image by averaging gray-level values in a neighborhood
def smooth_image(image, kernel_size=5):
    smoothed = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return smoothed

# Step 2: Compute the gradient magnitude of the smoothed image
def compute_gradient_magnitude(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(grad_x, grad_y)
    return magnitude

# Step 3: Threshold and thin the gradient image
def threshold_and_thin_gradient(magnitude, thresh_val=50):
    _, thresholded = cv2.threshold(magnitude, thresh_val, 255, cv2.THRESH_BINARY)
    thinned = cv2.ximgproc.thinning(np.uint8(thresholded))
    return thinned

# Step 4: Sample the smoothed image at maximal gradient points
def sample_maximal_gradient_points(image, gradient_points):
    sampled_values = image[gradient_points > 0]
    return sampled_values

# Step 5: Interpolate sampled gray levels over the image
def interpolate_image(sample_points, sampled_values, shape):
    grid_x, grid_y = np.mgrid[0:shape[0], 0:shape[1]]
    interpolated = griddata(sample_points, sampled_values, (grid_x, grid_y), method='linear', fill_value=0)
    return interpolated

# Step 6: Segment the image using the interpolated threshold surface
def segment_image(image, threshold_surface):
    segmented = np.where(image > threshold_surface, 255, 0).astype(np.uint8)
    return segmented

# Step 7: Validate and remove ghost objects
def validate_objects(segmented_image, gradient_magnitude, gradient_threshold=20):
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(segmented_image, connectivity=8)
    validated_image = np.zeros_like(segmented_image)

    for i in range(1, num_labels):  # Skip the background label 0
        mask = labels == i
        edge_values = gradient_magnitude[mask]
        if np.mean(edge_values) > gradient_threshold:
            validated_image[mask] = 255

    return validated_image

# Example Usage
image_path = 'images/barco.jpeg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

smoothed_image = smooth_image(original_image)
gradient_magnitude = compute_gradient_magnitude(smoothed_image)
thinned_gradient = threshold_and_thin_gradient(gradient_magnitude)
sampled_values = sample_maximal_gradient_points(smoothed_image, thinned_gradient)
interpolated_surface = interpolate_image(np.column_stack(np.nonzero(thinned_gradient)), sampled_values, smoothed_image.shape)
segmented_image = segment_image(smoothed_image, interpolated_surface)
validated_image = validate_objects(segmented_image, gradient_magnitude)

# Show results
cv2.imshow("Original Image", original_image)
cv2.imshow("Smoothed Image", smoothed_image)
cv2.imshow("Gradient Magnitude", gradient_magnitude / gradient_magnitude.max())
cv2.imshow("Thinned Gradient", thinned_gradient)
cv2.imshow("Segmented Image", segmented_image)
cv2.imshow("Validated Image", validated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()