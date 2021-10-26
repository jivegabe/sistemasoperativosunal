import os
result = os.path.getctime(".")##Regresa la fecha y hora de la creacion de este directorio (este comportamiento solo es en windows, en unix es la fecha del ultimo cambio de metadatos del directorio)
print ("Este directorio fue creado el: " + str(result) +" segundos (en tiempo epoch)")