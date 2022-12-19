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
    numeros_iniciales = list("0123456789")
    Corresp = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    for i in n:
        for j in numeros_iniciales:
            if i == j:
                for k in Corresp:
                    if j == k:
                    # Ahora hemos de considerar la longitud de la palabra  == al numero
                        if len(Corresp[k]) == int(i):
                            print("Hemos llegado a un equilibrio estable") 
                    break
                else:
                    pass
                break
print(Equilibrio("60"))
        
                
        





if __name__=="__main__":
    main()