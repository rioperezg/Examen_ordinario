from ast import main
"""""
Cree una función hollow_triangle(altura) que devuelva un triángulo hueco de la altura correcta. La altura se pasa a través de 
la función y la función debe devolver una lista que contiene cada línea del triángulo hueco.

hollow_triangle(6)

 should return : ['_____#_____', '____#_#____', '___#___#___', '__#_____#__', '_#_______#_', '###########']

hollow_triangle(9)

 should return : ['________#________', '_______#_#_______', '______#___#______', '_____#_____#_____', '____#_______#____', 
 '___#_________#___', '__#___________#__', '_#_____________#_', '#################']
"""
def Hollow_triangle(n):
    for i in range(1, n+1):
        return(" "*(n-i) + "# "*i)
print(Hollow_triangle(6))







if __name__=="__main__":
    main()