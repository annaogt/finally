import time
import math

print('\033c')
print('---------------------------------------------------------')

print('\t welcome to the finally project', end="", flush=True)
time.sleep(2)

print('\r' + ' ' * 50, end="")
print('\r\t\t Calcular consumo de electricidad de maquinas')

print('\n---------------------------------------------------------')

total_operaciones = 0
cont_electricidad = 0
cont_corriente = 0
cont_potencia = 0
cont_magnetismo = 0

respuesta = 'si'

while respuesta == 'si':

    print('\t Escoja una opcion:')
    print('\t ☆.- calcular la electricidad gastada')
    print('\t ☆.- calcular la corriente electrica')
    print('\t ☆.- calcular la potencia electrica')
    print('\t ☆.- calcular el magnetismo')

    texto = input('\t\t ¿Que desea realizar? -> ').lower()

    print('\033c')

    total_operaciones += 1

    match texto:

        case 'calcular la electricidad gastada' | 'electricidad gastada' | '1' | 'electricidad':
            cont_electricidad += 1

            print('\t cargando.....', end="", flush=True)
            time.sleep(1)

            print('\r\t\t calcular la electricidad gastada de maquinaria')

            print('\n--------------------------------------')
            print('¿Qué lapso de tiempo le gustaría?')
            print('\t ☆.- consumo por horas')
            print('\t ☆.- consumo electrico diario')
            print('\t ☆.- consumo mensual')

            op = input('Ingrese una opcion: ').lower()

            if op in ['1', 'horas', 'consumo por horas']:
                potencia = float(input('Ingrese la potencia en watts: '))
                horas = int(input('Ingrese las horas: '))
                energia = (potencia / 1000) * horas
                print(f'La energia consumida es de {energia} kWh')

            elif op in ['2', 'diario']:
                potencia = float(input('Ingrese la potencia en watts: '))
                energia = (potencia / 1000) * 24
                print(f'La energia diaria es de {energia} kWh')

            elif op in ['3', 'mensual']:
                potencia = float(input('Ingrese la potencia en watts: '))
                energia = (potencia / 1000) * 720
                print(f'La energia mensual es de {energia} kWh')

            else:
                print('Opcion no valida')

        case 'calcular la corriente electrica' | 'corriente electrica' | '2' | 'corriente':
            cont_corriente += 1

            print('\t cargando.....')
            time.sleep(1)

            voltaje = float(input("Ingresa el voltaje (V): "))
            resistencia = float(input("Ingresa la resistencia (Ω): "))

            if resistencia != 0:
                corriente = voltaje / resistencia
                print(f'La corriente electrica es de {corriente} A')
            else:
                print("No se puede dividir entre 0")

        case 'calcular la potencia electrica' | '3' | 'potencia':
            cont_potencia += 1

            print('\t cargando.....')
            time.sleep(1)

            voltaje = float(input("Ingresa el voltaje (V): "))
            corriente = float(input("Ingresa la corriente (A): "))

            potencia = voltaje * corriente
            print(f'La potencia electrica es de {potencia} W')

        case 'calcular el magnetismo' | '4' | 'magnetismo':
            cont_magnetismo += 1

            print('\t cargando.....')
            time.sleep(1)

            corriente = float(input("Ingrese la corriente (A): "))
            distancia = float(input("Ingrese la distancia (m): "))

            mu0 = 4 * math.pi * 1e-7

            if distancia != 0:
                campo = (mu0 * corriente) / (2 * math.pi * distancia)
                print(f'El campo magnetico es de {campo} T')
            else:
                print("La distancia no puede ser 0")

        case _:
            print("Opcion no valida")

    print('\n--------------------------------------')

    respuesta = input('¿Desea realizar otra operacion? (si/no): ').lower()

    while respuesta not in ['si', 'no']:
        respuesta = input("Por favor escribe 'si' o 'no': ").lower()

    print('\033c')


print('========== RESUMEN ==========')
print(f'Total de operaciones realizadas: {total_operaciones}')
print(f'Electricidad calculada: {cont_electricidad} veces')
print(f'Corriente calculada: {cont_corriente} veces')
print(f'Potencia calculada: {cont_potencia} veces')
print(f'Magnetismo calculado: {cont_magnetismo} veces')
print('=============================')