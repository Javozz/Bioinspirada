import numpy as np
from numpy import random
import math
import random

pop = []

class Ind():
	datos = np.zeros(4)
	fitness = 0

class Poblacion():

	P = []

def funcion(ind):

	return math.pow((ind.datos[0] + 2*ind.datos[1] - 7),2) + math.pow((2*ind.datos[0] + ind.datos[1] - 5),2) + math.pow((ind.datos[2] + 2*ind.datos[3] - 7),2) + math.pow((2*ind.datos[2] + ind.datos[3] - 5),2)

def funcion2(ind):

	return math.pow((ind[0] + 2*ind[1] - 7),2) + math.pow((2*ind[0] + ind[1] - 5),2) + math.pow((ind[2] + 2*ind[3] - 7),2) + math.pow((2*ind[2] + ind[3] - 5),2)

def poblacion_inicial(tot,dim):
	tmp = np.zeros(dim)
	for i in range(tot):
		ind = Ind()
		tmp[0] = round(np.random.uniform(-10,10),5)
		tmp[1] = round(np.random.uniform(-10,10),5) 
		tmp[2] = round(np.random.uniform(-10,10),5) 
		tmp[3] = round(np.random.uniform(-10,10),5) 
		
		ind.datos = tmp.copy()
		ind.fitness = funcion(ind)
		pop.append(ind)

def mostrar_poblacion(pop):
	for i in range(len(pop)):
		print(i+1,") [",pop[i].datos[0],"\t",pop[i].datos[1],"\t",pop[i].datos[2],"\t", pop[i].datos[3],"]", "\tFitness:", pop[i].fitness)

def aleatorios(v):
	v = v+1
	arr = []
	for i in range(len(pop)):
		arr.append(i+1)
	arr.remove(v)
	random.shuffle(arr)
	a = arr[0]
	b = arr[1]
	c = arr[2]
	return a,b,c

def inicio():
	global pop
	
	new_pop = []

	indiv = 8
	dimensiones = 4
	Fmut = 1.2
	Fcru = 0.5
	iteraciones = 200
	print("Parametros")
	print("- Cantidad de Individuos: ",indiv)
	print("- Cantidad de Dimensiones: ",dimensiones)
	print("- Constante de Mutación (F): ",Fmut)
	print("- Constante de Cruzamiento (CR): ",Fcru)
	print("- Cantidad de Iteraciones: ",iteraciones)
	print()

	poblacion_inicial(indiv,dimensiones)
	print("Poblacion Inicial")
	mostrar_poblacion(pop)
	print()
	print("Calcular la Aptitu de cada individuo")
	mostrar_poblacion(pop)
	print()
	for it in range(iteraciones):
		print("Iteracion ",it+1)
		for v in range(len(pop)):
			print("Vector ",v+1)
			print("Mutacion")
			xm,xk,xl = aleatorios(v)
			dif = pop[xk-1].datos - pop[xl-1].datos
			fdif= Fmut*dif
			mutado = pop[xm-1].datos+fdif
			print("xm: ",xm,"xk: ",xk,"xl: ",xl)
			print("xk - xl (Vector de Diferencias): ",dif)
			print("F*(xk - xl) (Vector de Diferencias Ponderado): ",fdif)
			print("xm + F*(xk - xl) (Vector Mutado): ",mutado)
			print("Cruzamiento")
			r1 = round(np.random.sample(),4)
			r2 = round(np.random.sample(),4)
			r3 = round(np.random.sample(),4)
			r4 = round(np.random.sample(),4)
			print(r1)
			print(r2)
			print(r3)
			print(r4)
			new_mut =[]

			if r1 <0.5:
				new_mut.append(mutado[0])
			else:
				new_mut.append(pop[v].datos[0])
			if r2 <0.5:
				new_mut.append(mutado[1])
			else:
				new_mut.append(pop[v].datos[1])
			if r3 <0.5:
				new_mut.append(mutado[2])
			else:
				new_mut.append(pop[v].datos[2])
			if r4 <0.5:
				new_mut.append(mutado[3])
			else:
				new_mut.append(pop[v].datos[3])
			
			ffitt = funcion2(new_mut)
			new_mut = np.array(new_mut)
			print("Vector Trial: ",new_mut, "Fitness: ",ffitt)
			if pop[v].fitness < ffitt:
				new_pop.append(pop[v])
				print("El vector target continua en la siguiente problación.")
			else:
				new_ind = Ind()
				new_ind.datos = new_mut.copy()
				new_ind.fitness = ffitt
				new_pop.append(new_ind)
				print("El vector target es reemplazado por el vector trial en la siguiente población")
			print()

		pop = new_pop
		print("Nueva Poblacion")
		mostrar_poblacion(pop)
		new_pop = []

###################################
###################################
###################################

inicio()












