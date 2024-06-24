
import zipfile

# mi ruta  inicial 
# C:\Users\fedeh\Desktop\channel\90052.txt
# C:\Users\fedeh\Desktop\channel.zip
# "C:/Users/fedeh/Desktop/channel.zip"

# toma los comentarios que puede tener un archivo zip y los imprime en pantalla 




# Abre el archivo ZIP en modo de lectura


# Abre el archivo ZIP en modo de lectura
with zipfile.ZipFile("C:/Users/fedeh/Desktop/channel.zip", "r") as archivo_zip:
    # Obtén la lista de información de los archivos en el archivo ZIP
    lista_info = archivo_zip.infolist()


    

    # Itera sobre cada objeto ZipInfo en la lista
    for info in lista_info:
        # Imprime el nombre del archivo y su comentario
        print("Nombre del archivo:", info.filename)
        print("Comentario:", info.comment)
        print()

