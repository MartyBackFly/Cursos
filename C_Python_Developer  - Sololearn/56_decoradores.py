from imprimir import espacio as aa

aa()

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
#----------------------------------------------------------------

#Ahora print_text corresponde a nuestra versión decorada.


def decor(func):
    def richard():
        print("============")
        func()
        print("============")
    return richard

def print_text():
    print("Hello world!")

print_text()
aa()

print_text = decor(print_text)
print_text()

#----------------------------------------------------------------
aa()


def decor(func):
    def mabel():
        print("============")
        func()
        print("============")
    return mabel

@decor
def print_text():
    print("con @ decimos que printext sera el parametro de decor")

print_text()


aa()