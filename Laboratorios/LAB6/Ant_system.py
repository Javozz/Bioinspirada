import numpy as np
from numpy import random
import math
import random

Rutas = []
fitness = []
Ciudades = ['A','B','C','D','E','F','G','H','I','J']

distancia =[[ 0, 12,  3, 23,  1,  5, 23, 56, 12, 11],
			[12,  0,  9, 18,  3, 41, 45,  5, 41, 27],
			[ 3,  9,  0, 89, 56, 21, 12, 48, 14, 29],
			[23, 18, 89,  0, 87, 46, 75, 17, 50, 42],
			[ 1,  3, 56, 87,  0, 55, 22, 86, 14, 33],
			[ 5, 41, 21, 46, 55,  0, 21, 76, 54, 81],
			[23, 45, 12, 75, 22, 21,  0, 11, 57, 48],
			[56,  5, 48, 17, 86, 76, 11,  0, 63, 24],
			[12, 41, 14, 50, 14, 54, 57, 63,  0,  9],
			[11, 27, 29, 42, 33, 81, 48, 24,  9,  0]]

class Hormiga():
	recorrido = []

def MostrarMatriz(M):
	for i in range(len(M)):
		for j in range(len(M)):
			print(round(M[i][j],4),"\t",end="")
		print()

def iniciarFeromona(v):
	M = []
	for i in range(10):
		F =[]
		for j in range(10):
			if i!=j:
				F.append(v)
			else:
				F.append(0)
		M.append(F)
	return M

def iniciarVisibilidad():
	M =[]
	for i in range(10):
		f=[]
		for j in range(10):
			if i!=j:
				valor = round(float(1/distancia[i][j]),4)
				f.append(valor)
			else:
				f.append(0)
		M.append(f)
	return M

def CalcularFitness():
	fitness = []
	
	for i in range(len(Rutas)):
		suma = 0
		for j in range(len(Rutas)-1):
			suma += distancia[Ciudades.index(Rutas[i][j])][Ciudades.index(Rutas[i][j+1])]
			#print(Ciudades.index(Rutas[i][j])," - ",Ciudades.index(Rutas[i][j+1])," // ",distancia[Ciudades.index(Rutas[i][j])][Ciudades.index(Rutas[i][j+1])])
		fitness.append(suma)

	return fitness

def Verificar(x,y):
	lista = []
	for i in range(len(Rutas)):
		for j in range(len(Rutas)-1):
			if Rutas[i][j]==x:
				if Rutas[i][j+1]==y:
					#print(Rutas[i][j]," ",Rutas[i][j+1]," - ",x," ",y," primer ", i+1)
					lista.append(i)
		for k in range(len(Rutas)-1):
			if Rutas[i][k]==y:
				if Rutas[i][k+1]==x:
					#print(Rutas[i][k]," ",Rutas[i][k+1]," - ",x," ",y," segundo ", i+1)
					lista.append(i)
	return lista

def PasoHormiga(lista,k):
	if len(lista)==0:
		return False
	for i in range(len(lista)):
		if k == lista[i]:
			return True
	return False

def FuncionActFeromona(Mat_Fer):
	New_Mat_Fer = []
	for i in range(len(Ciudades)):
		fila_Mat_Fer = []
		for j in range(len(Ciudades)):
			if Ciudades[i]!=Ciudades[j]:
				total = 0
				lista = Verificar(Ciudades[i],Ciudades[j])
				total += Mat_Fer[i][j]*0.99
				print(Ciudades[i],"-",Ciudades[j],": Feromona = ",round(Mat_Fer[i][j]*0.99,4),end="")
				for k in range(len(Rutas)):
					if PasoHormiga(lista,k)==True:
						print(" + ",round(1/fitness[k],4),end="")
						total+=1/fitness[k]
					else:
						print(" + 0",end="")
				print(" = ",round(total,4))
				#print(lista)
				fila_Mat_Fer.append(total)
			else:
				fila_Mat_Fer.append(0)
		New_Mat_Fer.append(fila_Mat_Fer)

	return New_Mat_Fer

def MejorHormiga():
	#Rutas[]
	pass

def inicio():
	global fitness
	global Rutas
	Ciudades_N = [0,1,2,3,4,5,6,7,8,9]
	N_ciudad = 10
	C_hormg = 9
	Fini = 0.1
	alpha = 1.0
	beta = 1.0
	rho = 0.99
	Q = 1.0
	iteraciones = 50
	print("Parámetros:")
	print("Cantidad de Hormigas: ",C_hormg)
	print("Feromona Inicial: ",Fini)
	print("alfa: ",alpha)
	print("beta: ",beta)
	print("rho: ",rho)
	print("Q: ",Q)
	print("Cantidad de Iteraciones: ",iteraciones)
	Mat_Fer = iniciarFeromona(Fini)
	Mat_Visib = iniciarVisibilidad()
	print()
	print("Matriz de Distancia:")
	MostrarMatriz(distancia)
	print()
	print("Matriz de Visibilidad:")
	MostrarMatriz(Mat_Visib)
	#print("-------------------------------------------------")
	random.shuffle(Ciudades_N)
	C_actual = Ciudades_N[0]
	Ciudades_N=Ciudades_N[1:]
	Ciudades_N.sort()

	Ciudades_tmp2 = Ciudades.copy()	# Copia
	random.shuffle(Ciudades_tmp2) 	# Desordenar
	C_actual_2 = Ciudades_tmp2[0]	# Ciudad Inicial
	Ciudades_tmp2.remove(C_actual_2)	# Eliminar Inicial

	for i in range(iteraciones):
		print("-------------------------------------------------")
		print("Iteracion ", i+1)
		print()
		print("Matriz de Visibilidad:")
		MostrarMatriz(Mat_Visib)
		print()
		print("Matriz de Feromona:")
		MostrarMatriz(Mat_Fer)
		print()
		
		Ciudades_tmp2.sort()				# Ordenar

		for j in range(C_hormg):
			Recorrido = []
			Ciudades_tmp = Ciudades_tmp2.copy()	# Copia

			print("Hormiga: ",j+1)
			print("Ciudad Inicial: ", C_actual_2)
			Ciu1 = Ciudades.index(C_actual_2)
			Recorrido.append(Ciudades[Ciu1])
			for itt in range(9):
				suma = 0
				for x in Ciudades_tmp:
					Ciu2 = Ciudades.index(x)
					suma = suma + Mat_Fer[Ciu1][Ciu2]*Mat_Visib[Ciu1][Ciu2]
					print(Ciudades[Ciu1],"-",Ciudades[Ciu2],": t =", Mat_Fer[Ciu1][Ciu2]," n = ",Mat_Visib[Ciu1][Ciu2]," t*n = ", round((Mat_Fer[Ciu1][Ciu2]*Mat_Visib[Ciu1][Ciu2]),5))

				print("Suma: ",round(suma,5))
				probabi = []
				
				for y in Ciudades_tmp:
					Ciu2 = Ciudades.index(y)
					probabi.append(Mat_Fer[Ciu1][Ciu2]*Mat_Visib[Ciu1][Ciu2]/suma)
					print(Ciudades[Ciu1],"-",Ciudades[Ciu2],": prob = ",round(Mat_Fer[Ciu1][Ciu2]*Mat_Visib[Ciu1][Ciu2]/suma,5))

				r1 = round(np.random.sample(),6)
				print("Numero aleatorio para la Probabilidad: ",r1)
				
				suma_prop = 0
				for z in range(len(Ciudades_tmp)):
					suma_prop+=probabi[z]
					if(r1<suma_prop):
						Ciu_Sig = Ciudades_tmp[z]
						Recorrido.append(Ciu_Sig)
						Ciudades_tmp.remove(Ciu_Sig)
						Ciu1 = Ciudades.index(Ciu_Sig)
						print("Ciudad Siguiente: ",Ciu_Sig)
						print()
						break
				#print(Ciudades_tmp, "Ciudades FFFFF")
			print()
			print("Hormiga ",j+1," ",Recorrido)
			Rutas.append(Recorrido)

		print()
		fitness = CalcularFitness()

		for hh in range(len(Rutas)):
			print("Hormiga ",hh+1,Rutas[hh]," - costo: ",fitness[hh])

		print()
		New_Mat_Fer = FuncionActFeromona(Mat_Fer)
		#print("Nueva matriz")
		#MostrarMatriz(New_Mat_Fer)
		Mat_Fer = New_Mat_Fer.copy()
		Rutas = []


###################################################
###################################################
###################################################
inicio()

	
	
	
	



