

myfile = open("B_Python_Developer/test.txt")

# Puedes especificar el modo usado para abrir un archivo aplicando un segundo argumento a la función open.
# Enviar "r" significa abrir en modo de lectura, que es el predeterminado.
# Enviar "w" significa modo de escritura, para reescribir el contenido de un archivo.
# Enviar "a" significa el modo append, para añadir nuevo contenido al final del archivo.

# Añadir "b" a un modo lo abre en modo binario, que se utiliza para los archivos que no son de texto (como los de imagen y sonido).

# Por ejemplo:

# write mode
open("B_Python_Developer/test.txt", "w")

# read mode
open("B_Python_Developer/test.txt", "r")
open("B_Python_Developer/test.txt")

# binary write mode
open("B_Python_Developer/test.txt", "wb")

# Se pueden combinar modos, por ejemplo, wb del código anterior abre el archivo en el modo de escritura binaria.




# debemos cerrar los archivitos 
myfile.close()