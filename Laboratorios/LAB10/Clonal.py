import numpy as np
from numpy import random
import math
import random



Pop = []
PopClon_tmp = []
Ciudades = ['A','B','C','D','E','F','G','H','I','J']

distancia =[[ 0,  1,  3, 23, 11,  5, 83, 21, 28, 45],
			[ 1,  0,  1, 18,  3, 41, 20, 61, 95, 58],
			[ 3,  1,  0,  1, 56, 21, 43, 17, 83, 16],
			[23, 18,  1,  0,  1, 46, 44, 45, 50, 11],
			[11,  3, 56,  1,  0,  1, 93, 38, 78, 41],
			[ 5, 41, 21, 46,  1,  0,  1, 90, 92, 97],
			[83, 20, 43, 44, 93,  1,  0,  1, 74, 29],
			[21, 61, 17, 45, 38, 90,  1,  0,  1, 28],
			[28, 95, 83, 50, 78, 92, 74,  1,  0,  1],
			[45, 58, 16, 11, 41, 97, 29, 28,  1,  0]]

#print(Ciudades)
#random.shuffle(Ciudades)
#print(Ciudades)

class Clon():
	ruta = []
	fitness = 0

def Generar_poblacion(P):
	Ciudades_tmp = Ciudades.copy()
	for i in range(P):
		random.shuffle(Ciudades_tmp)
		clon = Clon()
		clon.ruta = Ciudades_tmp.copy()
		Pop.append(clon)

def Mostrar_poblacion(Pop, tot=len(Pop)):
	for j in range(tot):
		print(j+1,') ',end="")
		for x in range(len(Pop[0].ruta)):
			print(Pop[j].ruta[x],end="")
		print("\t",Pop[j].fitness)

def CalcularFitness(Pop):
	for i in range(len(Pop)):
		global Ciudades
		suma = 0
		for j in range(len(Pop[0].ruta)-1):
			x = Ciudades.index(Pop[i].ruta[j])
			y = Ciudades.index(Pop[i].ruta[j+1])
			valor = distancia[x][y]
			suma += valor
		Pop[i].fitness = suma

	Pop.sort(key=lambda x: x.fitness)

def CalcularFitness_ind(ruta):
	global Ciudades
	suma = 0
	for j in range(len(ruta)-1):
		x = Ciudades.index(ruta[j])
		y = Ciudades.index(ruta[j+1])
		valor = distancia[x][y]
		suma += valor
	return suma

def Imprimir_Unidos(Ruta):
	cadena = ""
	for i in range(len(Ruta)):
		cadena = cadena + Ruta[i]
	return cadena

def Poblacion_Clon():
	PopClon = []
	Clones = 5
	pos = 1
	for i in range(5):
		for j in range(Clones):
			PopClon.append(Pop[i].ruta.copy())
		Clones-=1

	cambios = 1
	maximo = 5
	top = maximo
	posiciones = [0,1,2,3,4,5,6,7,8,9]
	for i in range(len(PopClon)):
		vv = Imprimir_Unidos(PopClon[i])
		print(i+1,")",vv, end="")
		if top == maximo:
			posiciones_tmp = posiciones.copy()
		for j in range(cambios):
			random.shuffle(posiciones_tmp)
			x = posiciones_tmp[0]
			posiciones_tmp.pop(0)
			y = posiciones_tmp[0]
			print(" [",x,",",y,"] ", end="")
			tmp = PopClon[i][x]
			PopClon[i][x] = PopClon[i][y]
			PopClon[i][y] = tmp
		top-=1
		if top == 0:
			cambios+=1
			maximo-=1
			top =maximo
		vv = Imprimir_Unidos(PopClon[i])
		fit = CalcularFitness_ind(PopClon[i])
		print(vv,"\t",fit)
		clon = Clon()
		clon.ruta = PopClon[i].copy()
		clon.fitness = fit
		PopClon_tmp.append(clon)

	PopClon_tmp.sort(key=lambda x: x.fitness)

def Poblacion_S():
	for x in range(5):
		vv = Imprimir_Unidos(PopClon_tmp[x].ruta)
		print(x+1,")", vv,"\t", PopClon_tmp[x].fitness)

def Poblacion_R():
	Ciudades_tmp = Ciudades.copy()
	for i in range(2):
		clon = Clon()
		random.shuffle(Ciudades_tmp)
		clon.ruta = Ciudades_tmp.copy()
		clon.fitness = CalcularFitness_ind(Ciudades_tmp)
		PopClon_tmp.append(clon)
		vv = Imprimir_Unidos(clon.ruta)
		print(i+1,")",vv,"\t",clon.fitness)

	PopClon_tmp.sort(key=lambda x: x.fitness)

def Poblacion_P():
	global PopClon_tmp
	global Pop
	Pop = Pop[:2]
	for i in range(5):
		Pop.append(PopClon_tmp[i])
	PopClon_tmp = []

	for j in range(len(Pop)):
		vv = Imprimir_Unidos(Pop[j].ruta)
		print(j+1,")",vv ,"\t",Pop[j].fitness)

	Pop.sort(key=lambda x: x.fitness)

def inicio():
	P = 7
	F = 5
	PClone = 15
	S = 5
	R = 2
	Dim = 10
	iteraciones = 250
	print('Parametros:')
	print('Tamaño población P:',P)
	print('Tamaño población F:',F)
	print('Tamaño población PClone y PHyper::',PClone)
	print('Tamaño población S:',S)
	print('Tamaño población R:',R)
	print('Dimensiones del vector (anticuerpo):',Dim)
	print('Cantidad de Iteraciones:',iteraciones)
	print()
	print('*** Población P ****')
	Generar_poblacion(P)
	CalcularFitness(Pop)
	Mostrar_poblacion(Pop,7)
	print()
	
	for i in range(iteraciones):
		print("Iteracion ",i+1)
		print("*** Población F ****")
		Mostrar_poblacion(Pop,5)
		print()
		print("*** Población PClone ****")
		Poblacion_Clon()
		print()
		print("*** Población S ****")
		Poblacion_S()
		print()
		print("*** Población R ****")
		Poblacion_R()
		print()
		print("*** Población P ****")
		Poblacion_P()
		print()




#############################################
#############################################
#############################################

inicio()
