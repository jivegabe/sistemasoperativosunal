import os
result = os.getcwd()

print ("'" + result + "' existe?:" + str(os.path.exists(result))) ##os.path.exists indica si el directorio especificado existe, retorna un booleano

dir_falso = os.path.join(result,"directorioFalso") 
print ("'"+dir_falso + "' existe?:" + str(os.path.exists(dir_falso)))