import os
result = os.path.getatime(".")##Regresa la fecha y hora del ultimo acceso al directorio especificdo, pero en valor epoch (esto es la cantidad de segundos transcurridos desde la medianoche UTC del 1 de enero de 1970) 
print ("Ultimo acceso al path en epoch: " + str(result) +" segundos")