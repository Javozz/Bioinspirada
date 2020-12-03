import numpy as np
from numpy import random
import math
import random


pop = []
ML = []
MG = []

class Ind():
	datos = np.zeros(4)
	fitness = 0

def funcion(ind):

	return math.pow((ind.datos[0] + 2*ind.datos[1] - 7),2) + math.pow((2*ind.datos[0] + ind.datos[1] - 5),2)

def Poblacion_Inicial(tot,dim):
	global ML
	tmp = np.zeros(dim)
	for i in range(tot):
		ind = Ind()
		tmp[0] = round(np.random.uniform(-10,10),6)
		tmp[1] = round(np.random.uniform(-10,10),6)
		tmp[2] = round(np.random.uniform(-1,1),6)
		tmp[3] = round(np.random.uniform(-1,1),6)
		
		ind.datos = tmp.copy()
		ind.fitness = funcion(ind)
		pop.append(ind)

	for j in range(len(pop)):
		ind = Ind()
		ML.append(ind)
		ML[j].datos = pop[j].datos.copy()
		ML[j].fitness = pop[j].fitness

def mostrar_poblacion_fitness(pop):
	for i in range(len(pop)):
		print(i+1,") x1 =",pop[i].datos[0],"\tx2 =",pop[i].datos[1],"\tFitness =",pop[i].fitness)

def mostrar_poblacion(pop):
	for i in range(len(pop)):
		print(i+1,") x1 =",pop[i].datos[0],"\tx2 =",pop[i].datos[1],"\tv1 =",pop[i].datos[2],"\t v2 =", pop[i].datos[3])

def mostrar_fitness(pop):
	for i in range(len(pop)):
		print(i+1,") ",pop[i].fitness)

def mejores_locales(pop,ML):
	for i in range(len(pop)):
		#print(ML[i].fitness,"  ",pop[i].fitness," ML ")
		if ML[i].fitness>pop[i].fitness:
			ML[i].datos[0] = pop[i].datos[0].copy()
			ML[i].datos[1] = pop[i].datos[1].copy()
			ML[i].datos[2] = pop[i].datos[2].copy()
			ML[i].datos[3] = pop[i].datos[3].copy()
			ML[i].fitness =  pop[i].fitness

def mejor_global(ML):
	global MG
	ind = Ind()
	ind = ML[0]

	for i in range(len(ML)):
		if ind.fitness > ML[i].fitness:
			ind = ML[i]

	if len(MG)==0:
		MG.append(ind)
		
	else:
		if MG[0].fitness > ind.fitness :
			MG.pop()
			MG.append(ind)
		

def actualizar_velocidad(ind,ind_ml,ind_mg,w,r1,r2):
	ind = Ind()

	ind.datos[2] = round(w*ind.datos[2]+2*r1*(ind_ml.datos[0]-ind.datos[0])+2*r2*(ind_mg.datos[0]-ind.datos[0]),5)
	ind.datos[3] = round(w*ind.datos[3]+2*r1*(ind_ml.datos[1]-ind.datos[1])+2*r2*(ind_mg.datos[1]-ind.datos[1]),5)
	ind.datos[0] = round(ind.datos[0]+ind.datos[2],5)
	ind.datos[1] = round(ind.datos[1]+ind.datos[3],5)
	return ind

def fitness(pop):
	for i in range(len(pop)):
		pop[i].fitness = funcion(pop[i])

def inicio():
	global ML

	iteraciones = 100
	print("Parametros")
	print("- Tamaño de la Población: 6")
	print("- Valores iniciales para $v_i$ entre -1.0 y 1.0")
	print("- w: número aleatorio entre 0.0 y 1.0 para cada iteración")
	print("- rand_1, rand_2: número aleatorio entre 0.0 y 1.0 para cada individuo")
	print("- C_1, C_2$: 2.0")
	print("- Cantidad de Iteraciones: 100")
	print()

	Poblacion_Inicial(10,4)
	print("*** Cúmulo de Partículas Inicial ***")
	mostrar_poblacion(pop)
	print()
	print("Fitness")
	mostrar_fitness(pop)
	print()
	mejores_locales(pop,ML)
	mejor_global(ML)
	print("Mejores Locales")
	mostrar_poblacion_fitness(ML)
	print()
	print("Mejor Global")
	mostrar_poblacion_fitness(MG)
	

	for itera in range(iteraciones):
		print()
		print("*** Iteracion ",itera+1," ***")

		w = round(np.random.uniform(0,1),6)
		print("w: ",w)
		for i in range(len(pop)):
			
			r1 = round(np.random.uniform(0,1),6)
			r2 = round(np.random.uniform(0,1),6)
			
			print("\t r1: ",w," r2: ",r2)

			ind = actualizar_velocidad(pop[i],ML[i],MG[0],w,r1,r2)
			
			pop[i].datos[0] = ind.datos[0].copy()
			pop[i].datos[1] = ind.datos[1].copy()
			pop[i].datos[2] = ind.datos[2].copy()
			pop[i].datos[3] = ind.datos[3].copy()

			print(i+1,")"," x1: ",pop[i].datos[0],"\tx2: ",pop[i].datos[1],"\tv1: ",pop[i].datos[2],"\tv2: ",pop[i].datos[3])

		fitness(pop)
		print()
		print("Fitness")
		mostrar_fitness(pop)

		mejores_locales(pop,ML)
		mejor_global(ML)
		print()
		print("Mejores Locales")
		mostrar_poblacion_fitness(ML)
		print()
		print("Mejor Global")
		mostrar_poblacion_fitness(MG)





#########################################################
#########################################################
#########################################################

inicio()





