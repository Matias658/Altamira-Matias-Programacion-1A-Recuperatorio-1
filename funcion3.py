#3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y 
#su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" 
#la deja como "agilmoort"

palabra = input("ingrese una palabra: ")

def ordenar_caracteres(cadena:str):
    lista_cadena = list(cadena)
    tam_cadena = len(lista_cadena)
    for i in range(tam_cadena - 1):  
        for j in range(i + 1, tam_cadena):
            if lista_cadena[i] > lista_cadena[j]:
                aux = lista_cadena[i]
                lista_cadena[i] = lista_cadena[j]
                lista_cadena[j] = aux
    cadena = "".join(lista_cadena)
    print(cadena)

        
palabra_invertida = ordenar_caracteres(palabra)
