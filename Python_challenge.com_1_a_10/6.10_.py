import zipfile
import re


# toma los comentarios que puede tener un archivo zip y los imprime en pantalla 



# Abre el archivo ZIP en modo de lectura
with zipfile.ZipFile("C:/Users/fedeh/Desktop/channel.zip", "r") as archivo_zip:
    # Obtén la lista de información de los archivos en el archivo ZIP
    lista_info = archivo_zip.infolist()

    # Inicializa una cadena vacía para almacenar los comentarios
    comentarios_concatenados = ""

    # Itera sobre cada objeto ZipInfo en la lista
    for info in lista_info:
        # Concatena el comentario del archivo actual al comentario general
        comentarios_concatenados += info.comment.decode("utf-8")  # Decodifica el comentario de bytes a cadena

    # Imprime todos los comentarios concatenados
    print("Comentarios de corrido:")
    print(comentarios_concatenados)




archivo_zip = "C:/Users/fedeh/Desktop/channel.zip"
num = '90052'
comments = []

with zipfile.ZipFile(archivo_zip, 'r') as z:
    while True:
        filename = num + ".txt"
        content = z.read(filename).decode("utf-8")
        comments.append(z.getinfo(filename).comment.decode("utf-8"))
        print(content)
        match = re.search("Next nothing is (\d+)", content)
        if match is None:
            break
        num = match.group(1)

print("".join(comments))

print(" it's in the air. look at the letters." )
print(" http://www.pythonchallenge.com/pc/def/oxygen.html" )






# Este código abrirá el archivo ZIP archivo.zip, leerá el contenido del archivo num + ".txt" en cada iteración del bucle while, 
#buscará la cadena "Next nothing is (\d+)" en el contenido y, si se encuentra, actualizará num con el número correspondiente y continuará 
# al siguiente archivo. Los comentarios de cada archivo se agregarán a la lista comments, que luego se imprimirá al final.

# Asegúrate de ajustar 'archivo.zip' al nombre de tu archivo ZIP y asegurarte de que la lógica del bucle esté bien adaptada a tu caso de uso específico.