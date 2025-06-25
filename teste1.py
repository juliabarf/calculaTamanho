import cv2
import numpy as np


#teste que eu to usando atualmente para calcular a área total
#configuração
caminho_imagem = ("poroSo.png")
area_por_pixel_um2 = 0.5  # cada pixel representa 0.5 µm²

#carrega a imagem em escala de cinza
imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
    exit()

# binariza a imagem  (0 = preto, 255 = branco) ===
_, binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

#calcula a porosidade
total_pixels = binaria.size
pixels_brancos = cv2.countNonZero(binaria)
porosidade_percentual = (pixels_brancos / total_pixels) * 100

#calcula a área dos poros
area_total_poros_um2 = pixels_brancos * area_por_pixel_um2
area_total_poros_mm2 = area_total_poros_um2 / 1e6  # 1 mm² = 1.000.000 µm²

#resultados
print(f"Porosidade: {porosidade_percentual:.2f}%")
print(pixels_brancos)
print(f"Área de poros: {area_total_poros_um2:.1f} µm²")
print(f"Área de poros: {area_total_poros_mm2:.3f} mm²")
