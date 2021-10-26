import os

file_name = "test1.py"
path= os.getcwd()
os.path.join(path,file_name)
try: 
    os.remove(path)##intentara eliminar el archivo en el path especificado, si no es un archivo sino un directorio dara el error "IsADirectoryError", si
                   ##por el contrario el directorio no existe, dara el error "FileNotFoundError"
    print ("El archivo " + file_name + " ha sido eliminado")                   
except:             
    print("ha ocurrido un error")
    