# busca bien 3 mayusc una minusc y 3 mayusc ..  en la web .
# tiene en cuenta que antes que arranque la cadena TTTaTTT no haya mas mayusc ejemplo 
# ASDFgHJKL  no sirve 
# aSDFgHJKl  si sirve



import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print()
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))

print()
print ("*************************************")
print()
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
matches = re.findall("([^A-Z]+)([A-Z]{3})([a-z])([A-Z]{3})([^A-Z]+)", data)


# en la busqueda tenemos el patron a buscar 

# [a-z]: 1 letra minúscula
# [A-Z]: 1 letra mayúscula
# [A-Z]{3}: 3 letras mayúsculas consecutivas
# [A-Z]{3}[a-z][A-Z]{3}: 3 letras mayúsculas + 1 letra minúscula + 3 letras mayúsculas
# [^A-Z]: cualquier carácter PERO una letra mayúscula
# [^A-Z]+: al menos uno de esos personajes
# [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+: algo más antes y después de nuestro patrón ( AAAbCCC) para que no haya más de 3 letras mayúsculas consecutivas en cada lado
# [^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+: ...y solo nos importan las minúsculas



# Este patrón busca una secuencia que no contenga letras mayúsculas [^A-Z]+, 
# seguida de exactamente tres letras mayúsculas [A-Z]{3}, 
# luego un carácter minúsculo que captura ([a-z]), 
# nuevamente seguido por tres letras mayúsculas [A-Z]{3}, 
# y finalmente otra secuencia que no contiene letras mayúsculas [^A-Z]+.


# La expresión [ ^A-Z]+ en el patrón busca una secuencia de uno o más caracteres que no sean letras mayúsculas. Aquí hay una explicación detallada:

# [^A-Z]: Este segmento de la expresión regular coincide con un solo carácter que no sea una letra mayúscula.
# El ^ dentro de los corchetes [] indica "no". Entonces, [^A-Z] coincide con cualquier carácter que no sea una letra mayúscula de la A a la Z.

# [^A-Z]+: El + después de [^A-Z] indica que este patrón debe aparecer una o más veces consecutivas. 
# Por lo tanto, [^A-Z]+ coincide con una secuencia de uno o más caracteres que no son letras mayúsculas.

# [ ^A-Z]+: El espacio antes del ^ es un error tipográfico. Este patrón coincide con cualquier carácter 
# que no sea una letra mayúscula de la A a la Z, incluidos los espacios. El espacio aquí no afectará 
# la funcionalidad de la expresión regular, ya que será tratado simplemente como otro carácter que no sea una letra mayúscula.

# En resumen, [ ^A-Z]+ busca una secuencia de uno o más caracteres que no sean letras mayúsculas, incluidos los espacios.




for match in matches:
    print(match[2])
print()
print("----------------------------------------")
print()
for match in matches:
    print(match[1]," ",   match[2], " " , match[3])
print()
print("++++++++++++++++++++++++++++++++++++++++++")
print()
for match in matches:
    print(f"{match[0][:1]}, {match[1]}, {match[2]}, {match[3]}, {match[4][:1]}")






