'''Desarrolar una funcion que reciba como parametro dos numeros enteros positivos y 
devuelva el numero que resulte de concatenar ambos valores.'''

def contador_de_digitos(num1,num2):
    aux = num2
    cont = 0

    while num2 > 0:
        num2 //= 10
        cont += 1

    else:
        multiplicador = 10 ** cont
        numero = num1 * multiplicador
        return print('El numero concatenado es: ', numero + aux)

            

def main():
    numero_1 = int(input('Escribi una el primer numero: '))
    numero_2 = int(input('Escribi el segundo numero: '))

    while numero_1 < 1 or numero_2 < 1 : 
        print('\n Ambos numero deben ser mayor a cero\n')
        numero_1 = int(input('Escribi una el primer numero: '))
        numero_2 = int(input('\nEscribi el segundo numero: '))

    son = contador_de_digitos(numero_1,numero_2)

if __name__ == '__main__':
    main()
