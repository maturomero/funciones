'''Escribir dos funciones sepraradas para imprimir por pantalla los siguientes patrones de asteriscos, 
donde la cantidad de filas se recibe como parametro.'''

def caracteres(filas):
    for i in range(1,filas+1):
        print("\n**********")

def caracteres_2(filas):
    for i in range(1,filas + 1):
        print((i * 2) * '*')


def main():
    
    filas = int(input('Candtidad de filas: '))
    while filas <= 0:
        print('No se admite el cero o numeros negativos.\n')
        filas = int(input('Candtidad de filas hacer: '))

    caracteres(filas)
    caracteres_2(filas)
        

if __name__ == '__main__':
    main()

