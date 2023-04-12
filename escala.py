import numpy as np
import cv2

im = cv2.imread("teste.png")
print (im.shape)
altura, largura = im.shape[:2]
cv2.imshow("teste", im)

cv2.waitKey(0)

ponto = (largura / 2, altura / 2) 
rota = cv2.getRotationMatrix2D(ponto, 50, 0.5)
teste = cv2.warpAffine(im, rota, (largura, altura))
cv2.imshow("teste", teste)

cv2.waitKey(0)