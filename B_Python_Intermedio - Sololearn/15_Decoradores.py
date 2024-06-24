from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()


aa()

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)

print_text()

aa()

#your code goes here
def decor(func):
    def wrap(num):
        print('***')
        func(num)
        print('***')
        print('END OF PAGE')
    return wrap
@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input())


