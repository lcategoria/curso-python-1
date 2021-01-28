'''for i in range(5):
    if (i == 0):
        print("Asalto al capitolio")
    if (i == 1):
        print("Destruccion al Congreso")
    if (i == 2):
        print("Muerte al Imperio Yanky")
    if (i == 3):
        print("Matar al Capitalismo")
    if (i == 4):
        print("Controlar America")
    print(i)'''

'''import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)'''

'''import os
os.environ['HTTP_PROXY'] = 'http://suproxy.server.com'''

'''print("Hello World")'''
# sears.py
# 1.2.5 Ejemplo
'''billete_grosor = 0.11 * 0.001 # Metros (0.11m)
sears_altura = 442 # Altura (metros)
num_billetes = 1
dia = 1

while num_billetes * billete_grosor < sears_altura:
    print(dia, num_billetes, num_billetes * billete_grosor)
    dia = dia + 1
    num_billetes = num_billetes * 2
print('Numero de dias', dia)
print('Numero de facturas', num_billetes)
print('Altura final', num_billetes * billete_grosor)'''

#1.2.7 - 1.2.8
'''a = 3 + 4
b = a * 2
print(b)'''

#1.2.8 Variables
'''altura = 442
_height = 442 # valido
altura2 = 442'''

#1.2.9 Tipos
'''
altura = 442
altura = 442.0
height = 'Muy Alto'''

#1.2.10
'''
nombre = 'Jake'
Nombre = 'Elwood'
NOMBRE = 'Guido'''

#1.2.13
'''a = 1
b = 0
if a > b:
    print ('Computadora dice no')
else:
    print('Computadora dice si')'''
'''a = 1
b = 2
if a > b:
    print('Computadora dice si')
elif a == b:
    print('COmputadora dice si')
else:
    print('Ana es un Gato')'''

'''nombre = 'Ana Moreno'
print ('Mi novia se llama', nombre)'''

'''print('Hola')
print('Mi nombre es', 'Jake')'''

'''print('Hola ', end = '')
print('Mi nombre es', 'Marcos')'''

#1.2.15
'''nombre = input('Ingrese su nombre: ')
print('Tu nombre es', nombre)'''

'''a = 1
b = 0
if a > b:
    pass
else:
    print('Computer says false')'''

print("hola")
print("hola")