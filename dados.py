"""
Para este proyecto, tendrás que crear un programa que simule la tirada de dados.
Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6.
El programa deberá imprimirlos en pantalla, imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.
"""
import random

lanzar = "si"
while lanzar == "si":
    dado = random.choices(list(range(1,7)),k=2) 
    print("\nAl lanzar los dados se obtuvo: ", dado) 
    print("La suma de los lados es: ",dado[0] + dado[1]) 
    lanzar = input("¿Desea lanzar los dados nuevamente? Si/No: \n",).lower() 

