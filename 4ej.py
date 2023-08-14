'''Un comercio de electrodomesticos necesita para su linea de cajas un programa que le indique al cajero el cambio
 que debe entregarle al cliente. 
Para eso se ingresan dos numeros enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuantos billetes de cada denominacion deben ser entregados al clientes como vuelto, 
de tal forma se minimice la cantidad de billetes. considerar que existen billetes de 500, 100, 50, 20, 10, 5, 1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente'''
def caja(valor,pagado,vuelto):
    billete0 = 500
    billete1 = 100
    billete2 = 50
    billete3 = 20
    billete4 = 10
    billete5 = 5
    billete6 = 1


    if valor > pagado:
        print(f'El pago es insuficientes se adeuda ${-vuelto}')
    else:
        print(f'\n El vuelto que se debe abonar es ${vuelto}')
        if vuelto // billete0 != 0:
            cant0 = vuelto // billete0
            vuelto %= billete0
            print (f'\nNecesita {cant0} billete de ${billete0}')
            
        if vuelto // billete1 != 0:
            cant0 = (vuelto // billete1)
            vuelto %= billete1
            print (f'\nNecesita {cant0} billete de ${billete1}')
            
        if vuelto // billete2 != 0:
            cant0 = vuelto // billete2
            vuelto %= billete2
            print (f'\nNecesita {cant0} billete de ${billete2}')

        if vuelto // billete3 != 0:
            cant0 = vuelto // billete3
            vuelto %= billete3
            print (f'\nNecesita {cant0} billete de ${billete3}')

        if vuelto // billete4 != 0:
            cant0 = vuelto // billete4
            vuelto %= billete4
            print (f'\nNecesita {cant0} billete de ${billete4}')

        if vuelto // billete5!= 0:
            cant0 = vuelto // billete5
            vuelto %= billete5
            print (f'\nNecesita {cant0} billete de ${billete5}')

        if vuelto // billete6 != 0:
    
            cant0 = vuelto // billete6
            vuelto %= billete6
            print (f'\nNecesita {cant0} billete de ${billete6}')


def main():
    costo = int(input('Costo del producto: $'))
    pagado = int(input('Pagado con: $'))
    vuelto = pagado - costo
    cash = caja(costo,pagado,vuelto)

if __name__ == '__main__':
    main()

