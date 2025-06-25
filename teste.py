import cv2
import numpy as np

# Caminho da imagem
imagem = cv2.imread("testeImagem.png", cv2.IMREAD_GRAYSCALE)

# Garante que a imagem está binária (0 e 255)
_, binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

# Conta os pixels
total_pixels = binaria.size
pixels_brancos = cv2.countNonZero(binaria)

# Calcula a porosidade (% de branco)
porosidade = (pixels_brancos / total_pixels) * 100

print(f"Porosidade: {porosidade:.2f}%")
