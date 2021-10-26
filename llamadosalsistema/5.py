import os

new_directory = "pruebasPython\\test1\\congig\\data"
os.chdir("../")
upperDirectory = os.getcwd()

path = os.path.join(upperDirectory,new_directory)
os.makedirs(path)##Crea el nuevo directorio en el path especificado de forma recursiva, es decir, puede crear cualquier directorio intermedio del path que aún no exista
print ("El directorio ha sido creado en:" + path)
