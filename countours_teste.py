import cv2
import numpy as np

# Passo 1: Carregar a imagem
image = cv2.imread('images/coins1.jpg')  # Substitua 'imagem.png' pelo caminho da sua imagem

# Passo 2: Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Passo 3: Aplicar o threshold para separar o objeto do fundo
gray = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)  # Ajuste o valor de 240 conforme necessário
cv2.imshow('Binary Image', binary)

# Passo 4: Encontrar as coordenadas dos pixels do objeto
# Obter os índices dos pixels não brancos (onde o valor é 255 na imagem binária)
coordinates = np.column_stack(np.where(binary < 255))

# Passo 5: Calcular a bounding box
x, y, w, h = cv2.boundingRect(coordinates)

# Passo 6: Desenhar a bounding box na imagem original
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Verde com espessura 2

# Mostrar a imagem com a bounding box
cv2.imshow('Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
