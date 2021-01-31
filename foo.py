class A:
    def __init__(self):
        self.name = 'clase'
def saludo(self):
    print('Hola soy A')

class B(A):
    def saludo(self):
        print('Hola soy B')

a = A( )
b = B( )
b.saludo( )