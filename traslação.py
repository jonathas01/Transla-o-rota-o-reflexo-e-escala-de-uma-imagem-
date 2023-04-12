import numpy as np
import cv2

im = cv2.imread("teste.png")
print (im)
altura, largura = im.shape[:2]
cv2.imshow("teste", im)

cv2.waitKey(0)


#translacao  para direita
deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])
desloca = cv2.warpAffine(im, deslocamento, (largura, altura))
cv2.imshow("direita", desloca)

cv2.waitKey(0)

#translacao  para esquerda

deslocamento = np.float32([[1, 0, -25], [0, 1, -50]])
desloca = cv2.warpAffine(im, deslocamento, (largura, altura))
cv2.imshow("esquerda", desloca)

cv2.waitKey(0)