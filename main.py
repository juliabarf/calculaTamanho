import cv2

# Carrega a imagem
imagem = cv2.imread('testeImagem.png')

# Converte para tons de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detecta as bordas
bordas = cv2.Canny(cinza, 50, 100)

# Encontra os contornos
contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Suponha que o maior contorno seja o objeto de referência (ex: moeda)
contorno_ref = max(contornos, key=cv2.contourArea)

# Calcula o retângulo que envolve o objeto de referência
x, y, w, h = cv2.boundingRect(contorno_ref)

# Define o tamanho real da referência (ex: moeda de 2.4 cm)
tamanho_real_cm = 2.0  # cm

# Calcula quantos pixels existem por centímetro
pixels_por_cm = w / tamanho_real_cm

# Agora, medimos os outros objetos
for contorno in contornos:
    if cv2.contourArea(contorno) < 100:
        continue

    x, y, w, h = cv2.boundingRect(contorno)
    largura_cm = w / pixels_por_cm
    altura_cm = h / pixels_por_cm

    # Desenha retângulo e escreve as medidas
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 0), 2)
    cv2.putText(imagem, f"{largura_cm:.1f}x{altura_cm:.1f} cm", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

# Mostra a imagem com medidas
cv2.imshow("Medidas", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
