#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
#un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo 
#parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena


cadena_ingresada = input("Ingrese el texto que desee: ").lower()

primera_caracter = input("Ingrese el primer caracter: ")
segundo_caracter = input("Ingrese el segundo caracter: ")


def reemplazarCaracteres(cadena: str, caracter1: str, caracter2: str):
    cadena_reemplazada = cadena.replace(caracter1, caracter2)
    contador = 0 
    for i in cadena:  
        if i == caracter1:  
            contador += 1 
    print(f"{cadena_reemplazada}, Caracteres cambiados: {contador}")

reemplazarCaracteres(cadena_ingresada, primera_caracter, segundo_caracter)
