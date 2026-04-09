Algoritmo finally
	
	Definir respuesta, text, op Como Cadena
	Definir total_operaciones, cont_electricidad, cont_corriente, cont_potencia, cont_magnetismo Como Entero
	Definir potencia, horas, energia, voltaje, resistencia, corriente, distancia, campo, mu0 Como Real
	
	Escribir "calcular consumo de energia de maquinas"
	
	total_operaciones <- 0
	cont_electricidad <- 0
	cont_corriente <- 0
	cont_potencia <- 0
	cont_magnetismo <- 0
	
	respuesta = "si"
	
	Mientras respuesta = "si" Hacer
		
		Escribir "escoja una opcion"
		Escribir "1.- electricidad"
		Escribir "2.- corriente"
		Escribir "3.- potencia"
		Escribir "4.- magnetismo"
		
		Leer text
		
		Segun text Hacer
			
			'1','calcular la electricidad gastada','electricidad gastada','electricidad':
				cont_electricidad <- cont_electricidad + 1
				
				Escribir "1.- horas"
				Escribir "2.- diario"
				Escribir "3.- mensual"
				Leer op
				
				Si op = "1" Entonces
					Escribir "potencia en watts:"
					Leer potencia
					Escribir "horas:"
					Leer horas
					energia <- (potencia / 1000) * horas
					Escribir "energia:", energia, "kWh"
					
				SiNo
					Si op = '2' o op = 'dias' o op = 'dia' Entonces
						Escribir 'Ingrese la potencia en watts: '
						Leer potencia
						energia <- (potencia / 1000) * 24
						Escribir "energia diaria:", energia
						
					SiNo
						Si op = "3" o op = 'mensual' Entonces
							Escribir 'Ingrese la potencia en watts: '
							Leer potencia
							energia <- (potencia / 1000) * 720
							Escribir "energia mensual:", energia
						SiNo
							Escribir "opcion no valida"
						FinSi
					FinSi
				FinSi
				
			'2','calcular la corriente electrica','corriente electrica','corriente':
				cont_corriente <- cont_corriente + 1
				Escribir 'Ingresa el voltaje (V): '
				Leer voltaje
				Escribir 'Ingresa la resistencia (?): '
				Leer resistencia
				
				Si resistencia <> 0 Entonces
					corriente <- voltaje / resistencia
					Escribir "corriente:", corriente
				SiNo
					Escribir "error division entre 0"
				FinSi
				
			'3','calcular la potencia electrica','potencia':
				cont_potencia <- cont_potencia + 1
				Escribir 'Ingresa el voltaje (V): '
				Leer voltaje
				Escribir 'Ingresa la corriente (A): '
				Leer corriente
				potencia <- voltaje * corriente
				Escribir "potencia:", potencia
				
			'4','calcular el magnetismo', 'magnetismo':
				cont_magnetismo <- cont_magnetismo + 1
				Escribir 'Ingrese la corriente (A): '
				Leer corriente
				Escribir 'Ingrese la distancia (m): '
				Leer distancia
				
				mu0 <- 4 * PI * 0.0000001
				
				Si distancia <> 0 Entonces
					campo <- (mu0 * corriente) / (2 * PI * distancia)
					Escribir "campo:", campo
				SiNo
					Escribir "distancia no valida"
				FinSi
				
			De Otro Modo:
				Escribir "opcion no valida"
				
		FinSegun
		
		total_operaciones <- total_operaciones + 1
		
		Escribir "¿Desea continuar? (si/no)"
		Leer respuesta
		
	FinMientras
	
	Escribir "========== RESUMEN =========="
	Escribir "Total:", total_operaciones
	Escribir "Electricidad:", cont_electricidad
	Escribir "Corriente:", cont_corriente
	Escribir "Potencia:", cont_potencia
	Escribir "Magnetismo:", cont_magnetismo
	Escribir "============================="
	
FinAlgoritmo