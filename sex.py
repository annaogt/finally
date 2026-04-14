import time
import math
from rich import print
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def cargando(segundos=1, mensaje="Procesando..."):
    with console.status(f"[white]{mensaje}", spinner="dots"):
        time.sleep(segundos)

print('\033c')
print('[bold blue]---------------------------------------------------------')
print('\t[bold blue]░█▀▀░█░░░█▀▀░█▀▀░▀█▀░█▀▄░█▀█░█▀▀░█▀█░█░░░█▀▀')
print('\t[bold blue]░█▀▀░█░░░█▀▀░█░░░░█░░█▀▄░█░█░█░░░█▀█░█░░░█░░')
print('\t[bold blue]░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀')
print('\t[blue]Welcome to the final project')

time.sleep(1)

print('\n[blue]Calcular consumo de electricidad de maquinas')
print('[blue]---------------------------------------------------------')

total_operaciones = 0
cont_electricidad = 0
cont_corriente = 0
cont_potencia = 0
cont_magnetismo = 0

respuesta = 'si'

while respuesta == 'si':

    print('\n\t[bold cyan]Escoja una opcion:')
    print('\t [white]☆.- Calcular electricidad gastada')
    print('\t [white]☆.- Calcular corriente electrica')
    print('\t [white]☆.- Calcular potencia electrica')
    print('\t [white]☆.- Calcular magnetismo')

    texto = Prompt.ask("\t¿Que desea realizar?").lower()

    print('\033c')
    total_operaciones += 1

    match texto:

        case '1' | 'electricidad' | 'electricidad gastada':
            cont_electricidad += 1

            cargando()

            print('\n[blue]\tCalculo de electricidad')
            print('[blue]---------------------------------------------------------')

            print('\t[white]☆.- Consumo por horas')
            print('\t[white]☆.- Consumo diario')
            print('\t[white]☆.- Consumo mensual')

            op = Prompt.ask("\tIngrese una opcion").lower()

            

        case '2' | 'corriente':
            cont_corriente += 1

            cargando()

            voltaje = float(Prompt.ask("\tVoltaje (V)"))
            resistencia = float(Prompt.ask("\tResistencia (Ω)"))

            if resistencia != 0:
                corriente = voltaje / resistencia
                print(f'[bold green]\tCorriente: {corriente} A')
            else:
                print('[bold red]\tNo se puede dividir entre 0')    

        case '3' | 'potencia':
            cont_potencia += 1

            cargando()

            voltaje = float(Prompt.ask("\tVoltaje (V)"))
            corriente = float(Prompt.ask("\tCorriente (A)"))

            potencia = voltaje * corriente
            print(f'[bold green]\tPotencia: {potencia} W')

        case '4' | 'magnetismo':
            cont_magnetismo += 1

            cargando()

            corriente = float(Prompt.ask("\tCorriente (A)"))
            distancia = float(Prompt.ask("\tDistancia (m)"))

            mu0 = 4 * math.pi * 1e-7

            if distancia != 0:
                campo = (mu0 * corriente) / (2 * math.pi * distancia)
                print(f'[bold green]\tCampo magnetico: {campo} T')
            else:
                print('[bold red]\tLa distancia no puede ser 0')

        case _:
            print('[bold red]\tOpcion no valida')

    print('\n[blue]---------------------------------------------------------')

    respuesta = Prompt.ask("\t¿Desea otra operacion? (si/no)").lower()

    while respuesta not in ['si', 'no']:
        respuesta = Prompt.ask("\tEscribe 'si' o 'no'").lower()

    print('\033c')

print('[bold blue]========== RESUMEN ==========')
print(f'[white]☆ Total operaciones: [bold green]{total_operaciones}')
print(f'[white]☆ Electricidad: [bold green]{cont_electricidad}')
print(f'[white]☆ Corriente: [bold green]{cont_corriente}')
print(f'[white]☆ Potencia: [bold green]{cont_potencia}')
print(f'[white]☆ Magnetismo: [bold green]{cont_magnetismo}')
print('[bold blue]=============================')