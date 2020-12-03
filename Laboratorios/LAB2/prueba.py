import numpy as np
#import scipy.stats as st
import random
import math

def Generar_poblacion(x):
	Pob_Ini=[]
	for i in range(x):
		x = round(random.uniform(-10.0,10),5)
		y = round(random.uniform(-10.0,10),5)
		tupla=(x,y)
		Pob_Ini.append(tupla)
	return Pob_Ini

def fitness(P):
	pass
def selec_padres():
	pass
def cruzamiento():
	pass

def Mutar():
	A1 = round(random.uniform(.0,1.0),6)
	A2 = round(random.uniform(.0,1.0),6)
	A3 = round(random.uniform(.0,1.0),6)
	A4 = round(random.uniform(.0,1.0),6)
	print(A1,A2,A3,A4)

def Inicio():
	Poblacion_Inicial = Generar_poblacion(8)
	for i in range(len(Poblacion_Inicial)):
		print(Poblacion_Inicial[i])
	fitness(Poblacion_Inicial)
	Mutar()

################
################
Inicio()
