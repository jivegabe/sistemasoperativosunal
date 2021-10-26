import os
file_name = "test2.py"
print("El peso anterior del archivo era: " + str(os.path.getsize(file_name))+ " bytes")
os.truncate(file_name, 42) ##Trunca el peso del archivo dado a la cantidad de bytes especificada
print("\n y ahora el archivo a sido truncado a: " + str(os.path.getsize(file_name)) + " bytes")