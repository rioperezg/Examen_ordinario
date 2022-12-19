from ast import main
"""""
Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de letras en "sixzero" es siete. 
El número de letras en "siete" es cinco. El número de letras en "cinco" es cuatro. El número de letras en "cuatro" es cuatro: 
hemos alcanzado un equilibrio estable.

Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que tiene siete letras. El número de letras en 
"siete" es cinco, y el número de letras en "cinco" es cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y 
contando el número de letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número de letras es igual 
a cuatro.

 

Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola palabra (en lugar del nombre propio del 
número en inglés). Por ejemplo, escribe 12 como "unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa 
y nueve).

Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde ese número entero hasta un equilibrio estable:
"""
# Debemos equilibrar el numero de letras de cada palabra = al numero en si
def Equilibrio(n):
    # Decclaramos los numero primero del 1 al 10
    numeros_iniciales= [0,1,2,3,4,5,6,7,8,9]
    cero = 0
    uno = 1
    dos = 2
    tres = 3
    cuatro = 4
    cinco = 5
    seis = 6
    siete = 7
    ocho = 8
    nueve = 9
    for i in range(0,10):
        if numeros_iniciales[i] == n:
            if numeros_iniciales[i] == 0:
                return cero
            elif numeros_iniciales[i] == 1:
                return uno
            elif numeros_iniciales[i] == 2:
                return dos
            elif numeros_iniciales[i] == 3:
                return tres
            elif numeros_iniciales[i] == 4:
                return cuatro
            elif numeros_iniciales[i] == 5:
                return cinco
            elif numeros_iniciales[i] == 6:
                return seis
            elif numeros_iniciales[i] == 7:
                return siete
            elif numeros_iniciales[i] == 8:
                return ocho
            elif numeros_iniciales[i] == 9:
                return nueve





if __name__=="__main__":
    main()