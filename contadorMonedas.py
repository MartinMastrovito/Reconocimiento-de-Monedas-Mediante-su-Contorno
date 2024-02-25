
import cv2
import numpy

#cargamos la imagen

valGauss=3
original=cv2.imread( "monedas.jpg" )
gris=cv2.cvtColor(original , cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valGauss,valGauss),0)#reducir o agrandar el ruido, imagen,
canny=cv2.Canny(gauss,60,100)


#mostramos resultados

cv2.imshow("Grises",gris)
cv2.imshow("Gauss",gauss)
cv2.imshow("Canny",canny)
cv2.waitKey(0)