import os

new_directory = "pruebasPython"
os.chdir("../")
upperDirectory = os.getcwd()

path = os.path.join(upperDirectory,new_directory)##junta el path actual con el nombre del nuevo directorio para crear un nuevo path
print ("El proximo directorio estará en:" + path)