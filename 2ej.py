'''Desarrollar una funcion que reciba tres numeros enteros positivos y
 verifiquen si correspondden a una fecha valida (dia, mes, año). 
Devolver True o False segun la fecha sea correacta o no.
Realizar tambien un programa para verificar el comportamiento de la funcion.'''


def febrero(dia,year):

    bisiesto = (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)
    if (bisiesto == False and dia > 28):
        return False
    
    else:
        return True
        

def dias_del_mes(dia):
    if dia < 1 or dia > 30:
        print("El dia esta fuera de rango")
        return False
    
    else:
        return  True
    
def chequeos(dia,mes,year):

    if dia < 1 or dia > 31:
        print("El dia esta fuera de rango")
        return False
    
    elif mes < 1 or mes > 12:
        print("El mes esta fuera de rango")            
        return False
        
    elif  year < 1000 or year > 2028:
        print("El año esta fuera de rango")
        return False
    
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        mes_dias = dias_del_mes(dia)
        return mes_dias
    
    elif mes == 2:
        f_mes = febrero(dia, year)
        return f_mes
    
    else:

        return True






def main():
    day = int(input('Escribi un dia numerico: '))
    month = int(input('Escribi un mes numerico: '))
    anho = int(input('Escribi un año numerico: '))
    valor1 = chequeos(day, month, anho)

    print (f'\nLa fecha es {valor1} y la misma es {day}/{month}/{anho}\n')
    
    
if __name__ == "__main__":
    main()