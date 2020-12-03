import math
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def Generar_Mutacion(rango):
	aleatorio=round(random.uniform(-rango,rango),5)
	return aleatorio

def Generar_B(alpha):
	aleatorio=round(random.uniform(-alpha,alpha+1),4)
	return aleatorio

def Prop_media():
	prop=50.0/100.0
	aleatorio=round(random.uniform(0.0,1.0),1)
	if(prop>aleatorio):
		print("Derecha")
		return True
	else:
		print("Izquierda")
		return False

def Cruzamiento_BLX(beta1, beta2, x1, y1, x2, y2):
	x3 = x1 + beta1*(x2-x1)
	y3 = y1 + beta2*(y2-y1)
	return x3,y3

def Prop_Cruzamiento(probabilidad):
	prop=probabilidad/100.0
	aleatorio=round(random.uniform(0.0,1.0),1)
	if(prop>aleatorio):
		print("Cruzamiento")
		return True
	else:
		print("Sin Cruzamiento")
		return False

def Prop_Mutacion(probabilidad):
	prop=probabilidad/100.0
	aleatorio=round(random.uniform(0.0,1.0),1)
	if(prop>aleatorio):
		print("Mutacion")
		return True
	else:
		print("Sin Mutacion")
		return False

def Generar_poblacion(x):
	Pob_Ini=[]
	for i in range(x):
		x = round(random.uniform(-10.0,10),5)
		y = round(random.uniform(-10.0,10),5)
		tupla=(x,y)
		Pob_Ini.append(tupla)
	return Pob_Ini

def funcion(x,y):
	fact1 = -math.cos(x)*math.cos(y)
	fact2 = math.exp(-math.pow((x-math.pi),2)-math.pow((y-math.pi),2))
	y = fact1*fact2
	return y

def funcion2(x,y):
        y = float(pow((x+2*y-7),2)+(pow((2*x+y-5),2)))
        return y

def Calcular_Aptitud(Poblacion):
	Aptitud=[]
	for i in range(len(Poblacion)):
		tmp=funcion(Poblacion[i][0],Poblacion[i][1])
		Aptitud.append(tmp)

	return Aptitud

##################################################

def Creacion_Mating_Pool():
	Mating_Pool = []
	for i in range(len(x)):
		if (Aptitud[x[i]-1]<Aptitud[y[i]-1]):
			print(x[i],' ',y[i],' ->',x[i])
			Mating_Pool.append(x[i])
		else:
			print(x[i],' ',y[i],' ->',y[i])
			Mating_Pool.append(y[i])
	print()
	return Mating_Pool

def Seleccion_Padre(Pob_Ini,i,x1,y1,Mating_Pool):
	padre1=Pob_Ini[Mating_Pool[x1[i]-1]-1]
	padre2=Pob_Ini[Mating_Pool[y1[i]-1]-1]
	print(x1[i],' - ',y1[i],' => ',Mating_Pool[x1[i]-1],' - ',Mating_Pool[y1[i]-1],' => ','[',padre1,'] - [',padre2,']')
	return padre1,padre2

def Cruzamiento(Padre1,Padre2):
	if(Prop_Cruzamiento(70)):
		beta1 = Generar_B(alpha)
		beta2 = Generar_B(alpha)
		print('Beta 1: ',beta1)
		print('Beta 2: ',beta2)
		x3,y3 = Cruzamiento_BLX(beta1, beta2, padre1[0], padre1[1], padre2[0], padre2[1])
		Pmutar=(x3,y3)
		print(Pmutar)
		#print(Pob_Ini[Mating_Pool[x1[i]-1]-1],' ',Pob_Ini[Mating_Pool[y1[i]-1]-1])
		#print(Pob_Ini[Mating_Pool[x1[i]-1]-1][0],' ',Pob_Ini[Mating_Pool[y1[i]-1]-1][1])
	else:
		if(Prop_media()):
			print(padre2)
			Pmutar=padre2
		else:
			print(padre1)
			Pmutar=padre1
	return Pmutar

def Mutar(Pmutar):
	if(Prop_Mutacion(10)):
		randd = Generar_Mutacion(10)
		print(randd, 'random')
		if(Prop_media()):
			print(Pmutar[1])
			Pmutar=list(Pmutar)
			Pmutar[1]= randd
			Pmutar=tuple(Pmutar)
			print(Pmutar)
		else:
			print(Pmutar[0])
			Pmutar=list(Pmutar)
			Pmutar[0]=randd
			Pmutar=tuple(Pmutar)
			print(Pmutar)
	print()
	return Pmutar

########################################################################################
########################################################################################
########################################################################################
########################################################################################
#Parametros
#- Cantidad de Individuos: 8
#- Cantidad de Genes por Individuo: 2
#- Selección por torneo (2)
#- Probabilidad de Cruzamiento: 0.6
#- Cruzamiento BLX-Alpha, Alpha = 0.5
#- Probabilidad de Mutación: 0.5
#- Mutación Uniforme
#- Cantidad de Iteraciones: 1000

alpha=0.5

t1=(-0.23049 , 3.17004)
t2=(-4.11155 , -8.72488)
t3=(-7.1934 , -2.79477)
t4=(1.09901 , 5.0153)
t5=(1.64154 , -6.70599)
t6=(9.35123 , 4.57899)
t7=(9.52661 , 8.74949)
t8=(6.79533 , -7.69008)
t9=(-2.60852 , -9.30492)
t10=(3.66493 , -4.92946)
t11=(4.1958 , -8.72677)
t12=(8.0046 , -0.52386)
t13=(1.18602 , 0.15667)
t14=(-6.35218 , 2.25305)
t15=(-3.1124 , -9.1466)
t16=(-4.34637 , -2.87708)

Poblacion=8
Pob_Ini = []

'''
Pob_Ini.append(t1)
Pob_Ini.append(t2)
Pob_Ini.append(t3)
Pob_Ini.append(t4)
Pob_Ini.append(t5)
Pob_Ini.append(t6)
Pob_Ini.append(t7)
Pob_Ini.append(t8)
'''

Pob_Ini = Generar_poblacion(Poblacion)
for i in range(len(Pob_Ini)):
	print(Pob_Ini[i])

print('zzzzzzzzzzzzzzzzzzz')

for a in range(10000):
	New_Pob_Ini = []
	Aptitud=Calcular_Aptitud(Pob_Ini)

	for i in range(len(Aptitud)):
		print(Aptitud[i])
	print()

	print("******iteracion ",a+1,"*******")
	x = [1,2,3,4,5,6,7,8]
	y = [1,2,3,4,5,6,7,8]
	random.shuffle(x)
	random.shuffle(y)
	print("Creacion del Mating Pool")
	Mating_Pool=Creacion_Mating_Pool()

	x1 = [1,2,3,4,5,6,7,8]
	y1 = [1,2,3,4,5,6,7,8]
	random.shuffle(x1)
	random.shuffle(y1)

	for i in range(len(x1)):
		print("*Seleccion de Padres*")
		padre1,padre2 = Seleccion_Padre(Pob_Ini,i,x1,y1,Mating_Pool)
		Pmutar=Cruzamiento(padre1,padre2)
		N_padre = Mutar(Pmutar)
		New_Pob_Ini.append(N_padre)

	Pob_Ini=New_Pob_Ini
	print("Nueva Poblacion")
	for i in range(len(Pob_Ini)):
		print(Pob_Ini[i])
	print()
