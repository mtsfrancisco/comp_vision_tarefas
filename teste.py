import cv2
import numpy as np

# Carrega a imagem principal e o template
imagem = cv2.imread('images/moedas.webp')
template = cv2.imread('images/moedastemplate.png')

# Converte para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Tamanho do template
w, h = template_gray.shape[::-1]

# Aplica template matching usando TM_SQDIFF
resultado = cv2.matchTemplate(imagem_gray, template_gray, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

# Define um limiar (para TM_SQDIFF valores menores são melhores)
threshold = 0.5
localizacoes = np.where(resultado <= threshold * min_val)

# Desenha retângulos nas correspondências
for pt in zip(*localizacoes[::-1]):
    cv2.rectangle(imagem, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow('TM_SQDIFF', resultado)
cv2.imshow('Resultado - TM_SQDIFF', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()