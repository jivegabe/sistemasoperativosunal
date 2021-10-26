import os

new_directory = "pruebasPython"
os.chdir("../")
upperDirectory = os.getcwd()

path = os.path.join(upperDirectory,new_directory)
os.mkdir(path)##Crea el nuevo directorio en el path especificado
print ("El directorio ha sido creado en:" + path)