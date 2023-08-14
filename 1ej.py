'''Desarrollar una funcion que reciba tres numeros positivos y devuelva el mayor de los tres, 
solo si es unico(estricto). En caso de no existir el mayor estricto devolver -1. 
No utilizar operadores logicos. Desarrollar tambien un programa para ingresar los tres valores, 
invocar a la funcion y mostrar el maximo hallado, o un mensaje informativo si este no existe.'''


def mayor(mayor, n1, n2):
    
    
    if n1 >= mayor:
        mayor = n1

    if mayor > n2:
        return mayor
    
    if n2 > mayor:
        return n2
    
    else:
        return -1
    
    


def number():
    numero = -1
    while numero < 0:
        numero = int(input('Escribi un numero: '))
        
    return numero
    

def main():
    num0 = number()
    num1 = number() 
    num2 = number()
    respuesta = mayor(num0,num1,num2)
    print(respuesta)
    
if __name__ == "__main__":
    main()
