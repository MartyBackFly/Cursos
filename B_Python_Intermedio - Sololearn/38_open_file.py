from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

myfile = open("filename.txt")


# Enviar "r" significa abrir en modo lectura, que es el predeterminado. 

# Enviar "w" significa modo de escritura, para reescribir el contenido de un archivo.

# Enviar "a" significa modo de adjunto, para agregar nuevo contenido al final del archivo.

# Agregar "b" a un modo lo abre en modo binario, que se utiliza para archivos que no son de texto (como archivos de imagen y sonido).



# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")



# Puedes combinar modos, por ejemplo, wb del código anterior abre el archivo en binary write modo.

# Una vez que un archivo ha sido abierto y utilizado, deberías cerrarlo.

# Esto se hace con el método close del objeto de archivo. 

file = open("filename.txt", "w")


# do stuff to the file
file.close()


# raise                              aumentar

# do stuff to the file         hacer cosas al archivo    