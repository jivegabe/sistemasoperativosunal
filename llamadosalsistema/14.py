import os
for root, dirs, files in os.walk("C:/Users/johan/Desktop/llamadosalsistema",True):
    print("path:" + root)
    print("directories:" + str(dirs))
    print("files:" + str(files))
    print("########")
##os.walk recorre todos los directorios y subdirectorios, retornando los paths de los mismos y los nombres de los archivos y directorios que puedan contener