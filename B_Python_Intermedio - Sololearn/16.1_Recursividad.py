from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz



def is_even(x):   #par
    if x == 0:
        return True
    else:
        return is_odd(x-1)
 
def is_odd(x):  # impar
    return not is_even(x)



print(is_odd(4))
print(is_even(5))


# Para is_even(5):

# is_even(5) llama a is_odd(4) (ya que 5 - 1 = 4).
# is_odd(4) llama a is_even(3) (ya que 4 - 1 = 3).
# is_even(3) llama a is_odd(2) (ya que 3 - 1 = 2).
# is_odd(2) llama a is_even(1) (ya que 2 - 1 = 1).
# is_even(1) llama a is_odd(0) (ya que 1 - 1 = 0).
# is_odd(0) llama a is_even(0).
# is_even(0) devuelve True.

# Ambas secuencias de llamadas terminan en is_even(0), lo que devuelve True. La diferencia radica en cómo
# se llega a ese punto: para is_even(4), se hacen cuatro llamadas a is_odd antes de llegar a is_even(0), 
# mientras que para is_even(5), se hacen cinco llamadas a is_odd.





aa()


# is_odd(4):
# La función evalúa not is_even(3).
# is_even(3) llama a is_odd(2).
# is_odd(2) llama a not is_even(1).
# is_even(1) llama a is_odd(0).
# Ahora estamos en el caso base. Cuando 𝑥=0 ,
# x=0, is_odd(0) devuelve True.
# La función is_even(1) recibe not True, que es False.
# La función is_odd(2) recibe False.
# La función is_even(3) recibe False.
# Finalmente, is_odd(4) recibe False.
# is_even(5):
# La función evalúa is_odd(4).
# is_odd(4) ya lo hemos evaluado como False según el proceso anterior.
# Por lo tanto, is_even(5) recibe not False, que es True.