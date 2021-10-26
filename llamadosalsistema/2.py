import os
result = os.getcwd()
print ("Anterior directorio de trabajo:" + result)
os.chdir("../") ## "../" te saca al directorio en el que esta contenido tu directorio actual
result = os.getcwd()
print ("Actual directorio de trabajo:" + result)