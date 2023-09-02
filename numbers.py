"""
     Los valores numericos pueden ser de diferentes tipos los cuales vamos a poder manipular
     los numero nunca se deben encapsular entre comillas.
"""


def numbers():
    edad = 12
    print(f"Numero entero =  {edad}, tipo de dato = {type(edad)}")

    ingresos = 525.25
    print(f"Numero flotante =  {ingresos}, tipo de dato = {type(ingresos)}")

    # Restando a valores
    egresos = 100
    ingresos2 = 50
    # Forma 1 de resta
    ingresos = ingresos - egresos
    print(f'Saldo total egresos= {ingresos}')

    # Forma 2 de resta
    ingresos -= egresos
    print(f'Saldo total egresos= {ingresos}')

    # Forma 1 de suma
    ingresos = ingresos + ingresos2
    print(f'Saldo total ingresos = {ingresos}')

    # Forma 2 de suma
    ingresos += ingresos2
    print(f'Saldo total ingresos = {ingresos}')

    # Ejercicio para calcular el promedio de 3 meses de ingresos

    presupuesto_enero = float(input('Presupuesto para el mes de enero: '))
    presupuesto_febrero = float(input('Presupuesto para el mes de febrero: '))
    presupuesto_marzo = float(input('Presupuesto para el mes de marzo: '))
    presupuesto_promedio = presupuesto_enero + presupuesto_febrero + presupuesto_marzo
    print(
        f'Los ingresos de los 3 meses son {presupuesto_promedio} y el promedio de los presupuestos son iguales a {presupuesto_promedio / 3}')


if __name__ == '__main__':
    numbers()
