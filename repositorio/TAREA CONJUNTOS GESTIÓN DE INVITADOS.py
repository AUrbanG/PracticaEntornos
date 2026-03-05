# TAREA CONJUNTOS GESTIÓN DE INVITADOS
# Imagina que estás organizando una fiesta y necesitas gestionar la lista de invitados. 
# Tienes varias listas con los nombres de las personas que han confirmado su asistencia a diferentes actividades previas a la fiesta (por ejemplo, una cena, una sesión de juegos, etc.). 
# Quieres realizar las siguientes tareas utilizando conjuntos:

	# 1.	Crear un conjunto con todos los invitados: A partir de las listas de asistentes a las actividades previas, crear un único conjunto que contenga a todos los invitados a la fiesta, 
			# eliminando cualquier duplicado.

	# 2.	Encontrar los invitados que asistieron a la cena y a la sesión de juegos: Determinar qué invitados asistieron a ambas actividades.

	# 3.	Encontrar los invitados que asistieron a la cena, pero no a la sesión de juegos: Identificar quiénes fueron a la cena, pero se perdieron la sesión de juegos.

	# 4.	Encontrar los invitados que asistieron a la sesión de juegos, pero no a la cena: Identificar quiénes fueron a la sesión de juegos, pero no a la cena.

	# 5.	Encontrar los invitados que asistieron a la cena o a la sesión de juegos (o a ambas): Determinar la unión de los asistentes a ambas actividades.

	# 6.	Encontrar los invitados que asistieron solo a una de las dos actividades (cena o juegos): Determinar la diferencia simétrica entre los asistentes a ambas actividades.

# PISTA: YO CREARÍA UNA LISTA DE ASISTENTES POR CADA EVENTO, SEGUIDAMENTE DICHAS LISTAS SE PUEDEN CONVERTIR EN CONJUNTOS, Y A PARTIR DE AHÍ…

Asistentes_cena=["Fran", "Tomás", "Álvaro", "Antonio", "Juanfran", "Sergio", "Javier", "Jesús", "Rubén", "Alejandro", "Carlos"]
Asistentes_sesion_de_juegos=["Ismael", "Lorenzo", "Francisco", "Jose", "Manuel", "David", "Ariadna", "Paco", "Samuel", "Consta", "Miguel", "Alejandro", "Rubén"]

C_invitados= set(Asistentes_cena).union(set(Asistentes_sesion_de_juegos))
C_cena= set(Asistentes_cena)
C_sesiondejuegos= set(Asistentes_sesion_de_juegos)



#1
def Mostrar_invitados():
	return print(f"Lista de invitados:  {C_invitados}\n")



# 2 y 5
def Mostrar_asistentes_cena_y_sesiondejuegos():
	Asistentes_comunes= C_cena & C_sesiondejuegos
	return print(f"Los invitados que asistieron a la cena y a la sesión de juegos son: {Asistentes_comunes}\n")

#3
def Mostrar_asistentes_fuera_de_sesiondejuegos():
	asistentes_fuera_de_sesiondejuegos= C_cena - C_sesiondejuegos
	return print(f"Los invitados que asistieron a la cena pero no a la sesión de juegos son: {asistentes_fuera_de_sesiondejuegos}\n")


#4
def Mostrar_asistentes_fuera_de_cena():
	asistentes_fuera_de_cena= C_sesiondejuegos - C_cena
	return print(f"Los invitados que asistieron a la sesión de juegos pero no a la cena son: {asistentes_fuera_de_cena}\n")

# 5
def Mostrar_asistentes_cena():
	return print(f"Los invitados que asistieron a la cena son: {C_cena}\n")

# 5
def Mostrar_asistentes_sesiondejuegos():
	return print(f"Los invitados que asistieron a la sesión de juegos son:  {C_sesiondejuegos}\n")


#6
def Mostrar_asistentes_simetricos():
	asistentes_simetricos= C_cena ^ C_sesiondejuegos
	return print(f"Los invitados que asistieron solo a una de las dos actividades son: {asistentes_simetricos}\n")


Mostrar_invitados()
Mostrar_asistentes_cena_y_sesiondejuegos()
Mostrar_asistentes_fuera_de_sesiondejuegos()
Mostrar_asistentes_fuera_de_cena()
Mostrar_asistentes_cena()
Mostrar_asistentes_sesiondejuegos()
Mostrar_asistentes_simetricos()