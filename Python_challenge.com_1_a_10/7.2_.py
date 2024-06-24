import cv2
import numpy as np

# Carga la imagen en escala de grises
gray_image = cv2.imread("Python_challenge.com_1_a_10\imagen_decodificada.png", cv2.IMREAD_GRAYSCALE)

# Realiza operaciones en la matriz de píxeles (por ejemplo, contar valores únicos)
unique_values = np.unique(gray_image)

# Muestra los valores únicos
print(unique_values)