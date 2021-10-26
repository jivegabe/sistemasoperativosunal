import os
result = os.path.relpath("C:/Users/johan/Desktop/llamadosalsistema") ##regresa el mismo path especificado, pero en su forma relativa al archivo en el que se ejecuta
print ("El path relativo de 19.py a 'llamadosalsistema' es: " + result)