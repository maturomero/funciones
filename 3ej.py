'''Una persona desea llevar el control de los gastos realizados al viajear en el subterraneo dentro de un mes.
 Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes, 
 se solicita desarrollar una funcion que reciba como parametro la cantidad de viajes realizado en un determinado mes y
 devuelva el total gastado en viajes. Realizar tambien un programa para verificar el comportamiento de la funcion.'''

def descuento(tarifa):
    viajes = positivo()
    total = 0

    if viajes == 0:
        print('No realizaste viajes en el mes')

    for i in range (1,viajes+1):
        
        if i <= 20:
            total += tarifa

        elif i > 20 and i <= 30:
            total += tarifa * 0.80

        elif i > 30 and i < 40:
            total += tarifa * 0.70

        else:
            total += tarifa * 0.60

    return total

def positivo():
    viajes = -1
    while viajes < 0:
        print('\nNo se admiten numeros negativos\n')

        viajes = int(input('Cuantos viejes realizaste en el mes, escibi un valor numerico entero: '))
    return viajes

        
def main():
    tarifa = 80
    valor_mensual = descuento(tarifa)
    print(f'El gasto total del mes es: ${round(valor_mensual)}')


if __name__ == "__main__":
    main()
