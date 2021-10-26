import os
path = "/" ##esblace el path como el root del disco actual en el que se encuentra windows, en mi caso "C"
dir_list=os.listdir(path) ##Muestra una lista de todos los directorios en el path especificado
print (dir_list)