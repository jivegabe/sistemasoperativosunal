import os
dir_path = "C:/Users/johan/Desktop/llamadosalsistema"
rel_path = os.path.relpath(dir_path) 
result = os.path.samefile(dir_path, rel_path)##Identifica si dos paths hacen referencia al mismo directorio o archivo
print ("¿Son '" + dir_path + "' y '" + rel_path + "' el mismo directorio?:" + str(result))