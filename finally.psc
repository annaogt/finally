Algoritmo ElectroCalc
	
    Definir texto, respuesta, op Como Cadena
    Definir total_operaciones, cont_electricidad, cont_corriente, cont_potencia, cont_magnetismo Como Entero
    Definir potencia, horas, energia, voltaje, resistencia, corriente, distancia, campo, mu0 Como Real
	
    Limpiar Pantalla
    Escribir "---------------------------------------------------------"
    Escribir "     ELECTROCALC PRO"
    Escribir "Calcular consumo de electricidad de maquinas"
    Escribir "---------------------------------------------------------"
	
    total_operaciones <- 0
    cont_electricidad <- 0
    cont_corriente <- 0
    cont_potencia <- 0
    cont_magnetismo <- 0
	
    respuesta <- "si"
	
    Mientras respuesta = "si" Hacer
		
        Escribir ""
        Escribir "Escoja una opcion:"
        Escribir "1.- Electricidad gastada"
        Escribir "2.- Corriente electrica"
        Escribir "3.- Potencia electrica"
        Escribir "4.- Magnetismo"
		
        Escribir "¿Que desea realizar?"
        Leer texto
		
        Limpiar Pantalla
		
        total_operaciones <- total_operaciones + 1
		
        Segun texto Hacer
			
			"1","calcular la electricidad gastada","electricidad gastada","electricidad":
                cont_electricidad <- cont_electricidad + 1
				
                Escribir "Calculo de electricidad"
                Escribir "1.- Por horas"
                Escribir "2.- Diario"
                Escribir "3.- Mensual"
				
                Leer op
				
                Si op = "2" o op = "dias" o op = "dia"  Entonces
                    Escribir "Ingrese la potencia (W): "
                    Leer potencia
                    Escribir "Ingrese las horas: "
                    Leer horas
					
                    energia <- (potencia / 1000) * horas
                    Escribir "Energia consumida: ", energia, " kWh"
					
                Sino
                    Si op = "3" o op = "mensual" o op == "mes" Entonces
                        Escribir "Ingrese la potencia (W): "
                        Leer potencia
						
                        energia <- (potencia / 1000) * 24
                        Escribir "Energia diaria: ", energia, " kWh"
						
                    Sino
                        Si op = "3" Entonces
                            Escribir "Ingrese la potencia (W): "
                            Leer potencia
							
                            energia <- (potencia / 1000) * 720
                            Escribir "Energia mensual: ", energia, " kWh"
                        Sino
                            Escribir "Opcion no valida"
                        FinSi
                    FinSi
                FinSi
				
            "2","calcular la corriente electrica","corriente electrica","corriente":
                cont_corriente <- cont_corriente + 1
				
                Escribir "Voltaje (V): "
                Leer voltaje
                Escribir "Resistencia (Ohm): "
                Leer resistencia
				
                Si resistencia <> 0 Entonces
                    corriente <- voltaje / resistencia
                    Escribir "Corriente: ", corriente, " A"
                Sino
                    Escribir "No se puede dividir entre 0"
                FinSi
				
            "3","calcular la potencia electrica","potencia":
                cont_potencia <- cont_potencia + 1
				
                Escribir "Voltaje (V): "
                Leer voltaje
                Escribir "Corriente (A): "
                Leer corriente
				
                potencia <- voltaje * corriente
                Escribir "Potencia: ", potencia, " W"
				
            "4","calcular el magnetismo", "magnetismo":
                cont_magnetismo <- cont_magnetismo + 1
				
                Escribir "Corriente (A): "
                Leer corriente
                Escribir "Distancia (m): "
                Leer distancia
				
                mu0 <- 4 * PI * 0.0000001
				
                Si distancia <> 0 Entonces
                    campo <- (mu0 * corriente) / (2 * PI * distancia)
                    Escribir "Campo magnetico: ", campo, " T"
                Sino
                    Escribir "La distancia no puede ser 0"
                FinSi
				
            De Otro Modo:
                Escribir "Opcion no valida"
				
        FinSegun
		
        Escribir ""
        Escribir "¿Desea otra operacion? (si/no): "
        Leer respuesta
		
        Mientras respuesta <> "si" Y respuesta <> "no" Hacer
            Escribir "Escribe si o no: "
            Leer respuesta
        FinMientras
		
        Limpiar Pantalla
		
    FinMientras
	
    Escribir "========== RESUMEN =========="
    Escribir "Total operaciones: ", total_operaciones
    Escribir "Electricidad: ", cont_electricidad
    Escribir "Corriente: ", cont_corriente
    Escribir "Potencia: ", cont_potencia
    Escribir "Magnetismo: ", cont_magnetismo
    Escribir "============================="
	
FinAlgoritmo