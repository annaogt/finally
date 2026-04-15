import time
import math
from rich import print
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def cargando(segundos=0.5, mensaje="Procesando..."):
    with console.status(f"[white]{mensaje}", spinner="dots"):
        time.sleep(segundos)

print('\033c')
print('[bold blue]---------------------------------------------------------')
print('\t[bold blue]░█▀▀░█░░░█▀▀░█▀▀░▀█▀░█▀▄░█▀█░█▀▀░█▀█░█░░░█▀▀')
print('\t[bold blue]░█▀▀░█░░░█▀▀░█░░░░█░░█▀▄░█░█░█░░░█▀█░█░░░█░░')
print('\t[bold blue]░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀')
print('\t[blue]Welcome to the final project')

time.sleep(2)

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

        case '1' | 'electricidad' | 'electricidad gastada' | 'gastada':
            cont_electricidad += 1

            cargando()

            print('\n[blue]\t CALCULAR LA ELECTRICIDAD DE LA MAQUINA')
            print('[blue]---------------------------------------------------------')

            print('\t[white]☆.- Consumo por horas')
            print('\t[white]☆.- Consumo diario')
            print('\t[white]☆.- Consumo mensual')

            op = Prompt.ask("\tIngrese una opcion").lower()

            if op in ['1', 'horas', 'consumo por horas']:
                print('\n[blue]\t CALCULAR ELECTRICIDAD DE LA MAQUINA POR HORAS')
                try: potencia = float(input('\tIngrese la potencia en watts: '))
                except ValueError:
                    print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                    exit()
                try:horas = int(input('\tIngrese las horas: '))
                except ValueError:
                    print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                    exit()
                energia = (potencia / 1000) * horas
                print(f'\tLa energia consumida es de {energia} kWh')

            elif op in ['2', 'diario']:
                print('\n[blue]\t CALCULAR ELECTRICIDAD DE LA MAQUINA POR UN DIA')
                try: potencia = float(input('\tIngrese la potencia en watts: '))
                except ValueError:
                    print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                    exit()
                energia = (potencia / 1000) * 24
                print(f'\tLa energia diaria es de {energia} kWh')

            elif op in ['3', 'mensual']:
                print('\n[blue]\t CALCULAR ELECTRICIDAD GASTADA EN UN MES')
                try: potencia = float(input('\tIngrese la potencia en watts: '))
                except ValueError:
                    print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                    exit()
                energia = (potencia / 1000) * 720
                print(f'\tLa energia mensual es de {energia} kWh')

            else:
                print('\t\tOpcion no valida')
            
        case '2' | 'corriente'| 'corrientes':
            cont_corriente += 1

            cargando()
            print('\n[blue]\t CALCULAR CORRIENTE ELECTRICA DE LA MAQUINA')

            try: voltaje = float(Prompt.ask("\tVoltaje (V)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()
            try: resistencia = float(Prompt.ask("\tResistencia (Ω)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()

            if resistencia != 0:
                corriente = voltaje / resistencia
                print(f'[bold green]\tCorriente: {corriente} A')
            else:
                print('[bold red]\tNo se puede dividir entre 0') 

        case '3' | 'potencia' | 'potencias':
            cont_potencia += 1

            cargando()
            print('\n[blue]\t CALCULAR POTENCIA ELECTRICA')

            try: voltaje = float(Prompt.ask("\tVoltaje (V)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()

            try: corriente = float(Prompt.ask("\tCorriente (A)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()
            potencia = voltaje * corriente
            print(f'[bold green]\tPotencia: {potencia} W')

        case '4' | 'magnetismo' | 'magnetismos':
            cont_magnetismo += 1

            cargando()
            print('\n[blue]\t CALCULAR MAGNETISMO DE LA MAQUINA')
            try: corriente = float(Prompt.ask("\tCorriente (A)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()

            try: distancia = float(Prompt.ask("\tDistancia (m)"))
            except ValueError:
                print("[yellow][!][/yellow] Ingresa un dato de tipo numero!")
                exit()


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
        try:  respuesta = Prompt.ask("\tEscribe 'si' o 'no'").lower()
        except ValueError:
            print("[yellow][!][/yellow] Ingresa un dato valido!")
            exit() 

    print('\033c')

print('[bold blue]========== RESUMEN ==========')
print(f'[white]☆ Total operaciones: [bold green]{total_operaciones}')
print(f'[white]☆ Electricidad: [bold green]{cont_electricidad}')
print(f'[white]☆ Corriente: [bold green]{cont_corriente}')
print(f'[white]☆ Potencia: [bold green]{cont_potencia}')
print(f'[white]☆ Magnetismo: [bold green]{cont_magnetismo}')
print('[bold blue]=============================')