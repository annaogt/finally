import time
import math

print('\033c')
print('---------------------------------------------------------')

print('\t welcome to the finally project', end="", flush=True)
time.sleep(3)

print('\r' + ' ' * 50, end="")
print('\r\t\t Calcular consumo de electricidad de maquinas', end="", flush=True)

time.sleep(1)

print('\n---------------------------------------------------------')
horas=0
respuesta='si'

while respuesta=='si':

    print('\t Escoja una opcion:')
    print('\t ☆.- calcular la electricidad gastada')
    print('\t ☆.- calcular la corriente electrica')
    print('\t ☆.- calcular la potencia electrica')
    print('\t ☆.- calcular el magnetismo')

    texto = input('\t\t ¿Que desea realizar? -> ').lower()

    print('\033c')



    match texto:
        case 'calcular la electricidad gastada' | 'electricidad gastada' | '1' | 'electricidad':    

            print('\t cargando.....', end="", flush=True)
            time.sleep(3)

            print('\r' + ' ' * 50, end="")
            print('\r\t\t calcular la electricidad gastada de la maquina', end="", flush=True)

            time.sleep(1)


            print('que lapso de tiempo le gustaria  ')
            print('\t ☆.- consumo por horas \n\t ☆.- consumo electrico diario \n\t ☆.- consumo mensual' )
            op=input('ingrese una opcion ')

            if op=='consumo por horas' or op=='horas' or op=='1':
                potencia=float(input('ingrese la potencia en watts'))
                horas=int(input('por favor ingresar horas'))
                energia=(potencia/1000)*horas
                print(f'la energia gastada por la maquina en un lapso de {horas}h es de {energia}kwh')

            elif op=='consumo de electricidad diario' or op=='electricidad diaria' or op=='diaria' or op=='diario' or op=='2':
                horas=24
                potencia=float(input('ingrese la potencia en watts'))
                energia=(potencia/1000)*horas
                print(f'la energia gastada por la maquina en un lapso de {horas}h es de {energia}kwh')
        
            elif op=='consumo de electricidad mensual' or op=='electricidad mensual' or op=='mensual' or op=='3':
                horas=720
                potencia=float(input('ingrese la potencia en watts'))
                energia=(potencia/1000)*horas
                print(f'la energia gastada por la maquina en un lapso de {horas}h es de {energia}kwh')

            else:
                print('algo salio mal, por favor ingrese una opcion valida')

        case 'calcular la corriente electrica' | 'corriente electrica' | '2' | 'corriente':
            print('\t cargando.....', end="", flush=True)
            time.sleep(3)

            print('\r' + ' ' * 50, end="")
            print('\r\t\t calcular corriente electrica de la maquina', end="", flush=True)

            time.sleep(1)

            voltaje=float(input("Ingresa el voltaje (V): "))
            resistencia=float(input("Ingresa la resistencia (Ω): "))

            if resistencia != 0:
                corriente = voltaje / resistencia
                print(f'la corriente electrica de la maquina es de {corriente}A')
            else:
                print("No se puede dividir entre 0")

        case 'calcular la potencia electrica' | 'calcular potencia electrica' | '3' | 'potencia electrica' | 'potencia':
            print('\t cargando.....', end="", flush=True)
            time.sleep(3)

            print('\r' + ' ' * 50, end="")
            print('\r\t\t calcular potencia electrica de la maquina', end="", flush=True)

            time.sleep(1)


            voltaje = float(input("Ingresa el voltaje (V): "))
            corriente = float(input("Ingresa la corriente (A): "))
            potencia = voltaje * corriente

            print(f'la potencia electrica de la maquina es de {potencia}W')

        case 'calcular el magnetismo' | 'calcular magnetismo' | '4' | 'magnetismo':
            print('\t cargando.....', end="", flush=True)
            time.sleep(3)

            print('\r' + ' ' * 50, end="")
            print('\r\t\t calcular el magnetismo de la maquina', end="", flush=True)

            time.sleep(1)

            corriente= float(input("ingrese la corriente (A): "))
            longitud= float(input("ingrese la distancia (m): "))

            mu0 = 4 * math.pi * 1e-7
            campo = (mu0 * corriente) / (2 * math.pi * longitud)

            print(f'el magnetismo de la maquina es de {campo}T')

    respuesta=input('Desea realizar otra operacion? (si/no)').lower()
    if respuesta not in ['si', 'no']:
        print("Por favor escribe 'si' o 'no'")
    print('\033c')