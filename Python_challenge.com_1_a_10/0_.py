

#http://www.pythonchallenge.com/pc/def/0.html




#numero potenciado a potencia 



# Solicitud de Datos
numero = int(input('>>> Introduce el numero a potenciar: '))  #2
potencia= int(input('>>> Introduce potenciar: '))             #38
 
for multiplicador in range(1,potencia+1):
    resultado = numero ** multiplicador
    print("%d ^ %2d = %d" % (numero,multiplicador,resultado))
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a  potenciar: '))
 
for multiplicador in range(1,11):
    resultado = numero ** multiplicador
    print(f"{numero} ^ {multiplicador:2} = {resultado}")
    

