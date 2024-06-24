from imprimir import espacio as aa


aa()


def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)


aa()

def function(named_arg, richard,  *args):
    print(named_arg)
    print (richard)
    print(args)

function(1, 2, 3, 4, 5)


aa()
aa()



#**kwargs (para los argumentos de las palabras clave) te permite manejar argumentos con 
#nombre que no has definido de antemano.



def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
    print(args)
    print(y)
    print(x)
    
my_func(2, 3, 4, 5, 6, a=7, b=8)

#el valor de y cambia de 7 a 3 claramente por que lo llamamos con 3 en la funcion 


aa()


def my_func(x=7, y=7, *args, **kwargs):
    print("kwargs:", kwargs)
    print("args:",args)
    print("y :",y)
    print("x:",x)
    
my_func(3, z=4, *(5, 6), a=7, b=8)



aa()

def my_func(x=7, y=7, *args, **kwargs):
    print("kwargs ", kwargs)
    print("args", args)
    print("y ", y)
    print("x ", x)
    
my_func(3, *(5, 6), 9, 20, z=4, a=7, b=8)
print("-----")
#diferencia del asterisco en la llamada 
print("sin asterisco en la llamada le asigna los dos valores a \"y\" ")
my_func(3, (5, 6, 8, 8, 8, 8, 8, 8, 8,), 9, 20, z=4, a=7, b=8)

aa()



def my_func(x=7, y=7, *args, **kwargs):
    print("kwargs:", kwargs)
    print("args:",args)
    print("y :",y)
    print("x:",x)
    
my_func(3, z=4, *(5, 6, 8, 8, 8, 8, 8, 8, 8, ), a=7, b=8)


