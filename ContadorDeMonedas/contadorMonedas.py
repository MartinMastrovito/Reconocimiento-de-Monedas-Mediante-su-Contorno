
import cv2
import numpy as np

#cargamos la imagen

valGauss=3
original=cv2.imread( "monedas.jpg" )
gris=cv2.cvtColor(original , cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valGauss,valGauss),0)#reducir o agrandar el ruido, imagen,
canny=cv2.Canny(gauss,60,100)
kernel=np.ones((valGauss,valGauss),np.uint8)
#hago un cierre para solo obtener los contornos
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)#morph close establece eliminar el ruido interior

contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#usa 2 valores ya que la funcion devuelve dos valores
print("monedas encontradas={}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(0,0,255),2)#-1 para mostrar todos los contornos
#mostramos resultados

cv2.imshow("Grises",gris)
cv2.imshow("Gauss",gauss)
cv2.imshow("Canny",canny)
cv2.imshow("Resultado",original)
cv2.waitKey(0)