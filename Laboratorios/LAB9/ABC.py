import numpy as np
from numpy import random
import math
import random


FA = []


class Fuente():
	datos = np.zeros(2)
	funcion = 0
	fitness = 0
	repe = 0

def funcion(Fuente):
	
	return round(math.pow((Fuente.datos[0] + 2*Fuente.datos[1] - 7),2) + math.pow((2*Fuente.datos[0] + Fuente.datos[1] - 5),2),5)

def fitness(Fuente):

	if Fuente.funcion>=0:
		Fuente.fitness = round(1/(1+Fuente.funcion),3)
	else:
		Fuente.fitness = round(1 - Fuente.funcion,3)

	return Fuente.fitness

def Fuente_Iniciales(SN,dim):
	global FA
	tmp = np.zeros(dim)
	for i in range(SN):
		F = Fuente()
		tmp[0] = round(np.random.uniform(-10,10),4)
		tmp[1] = round(np.random.uniform(-10,10),4)
		
		F.datos = tmp.copy()
		F.funcion = funcion(F)
		

		if F.funcion>=0:
			F.fitness = round(1/(1+F.funcion),3)
		else:
			F.fitness = round(1 - F.funcion,3)

		FA.append(F)

def Mejor_Dif(Fuente,Nueva):
	if Fuente.funcion < Nueva.funcion:
		return "NO"
	else:
		return "SI"

def mostrar(FA):
	for i in range(len(FA)):
		print(i+1,')',FA[i].datos[0],'\t',FA[i].datos[1],'\t',FA[i].funcion,'\t',FA[i].fitness,'\t',FA[i].repe)

def Mostrar_Proba(FA):
	v_prop=[]
	suma = 0
	for j in range(len(FA)):
		suma += FA[j].fitness
	
	prop = 0
	for i in range(len(FA)):
		porcentaje = FA[i].fitness/suma
		prop += porcentaje
		v_prop.append(prop)
		print(i+1,')',FA[i].datos[0],' \t',FA[i].datos[1],'\t',FA[i].funcion,'\t',FA[i].fitness,'\t',round(porcentaje,3),'\t',round(prop,3),'\t',FA[i].repe)	
	return v_prop

def Encontrar_ikj(prop,rand):
	j = random.randint(0,1)
	i = 0
	for x in range(len(prop)):
		if rand<prop[x]:
			i = x
			break
		i = x
	k = random.randint(0,2)
	while i == k:
		k = random.randint(0,2)

	return i,k,j

def Mejor_Fuente(FA):
	F = Fuente()
	F = FA[0]
	F.datos[0] = FA[0].datos[0].copy()
	F.datos[1] = FA[0].datos[1].copy()

	for i in range(len(FA)):
		if F.funcion > FA[i].funcion:
			F = FA[i]
			F.datos[0] = FA[i].datos[0].copy()
			F.datos[1] = FA[i].datos[1].copy()

	return F

def V(num1,num2,phi):

	return round(num1+phi*(num1-num2),4)

def inicio():
	SN = 3
	D = 2
	iteraciones = 150
	print('Parametros')
	print('SN = ',SN)
	print('D = ',D)
	print('Iteraciones =',iteraciones)
	print()
	Fuente_Iniciales(SN,D)

	print('*** Fuentes Iniciales de Alimento ***')
	mostrar(FA)
	print()
	MFA = Mejor_Fuente(FA)
	print('*** Mejor Fuente de Alimento: [',MFA.datos[0],'\t',MFA.datos[1],']\t= ',MFA.funcion)
	print()

	for itera in range(iteraciones):

		print('**** Iteración ',itera+1,' ****')
		print('*** Enviar a Abejas Empleadas - Soluciones Candidatas ****')

		for i in range(len(FA)):
			j = random.randint(0,1)
			k = random.randint(0,2)
			phi = round(np.random.uniform(-1,1),4)
			
			while i == k:
				k = random.randint(0,2)

			new = V(FA[i].datos[j],FA[k].datos[j],phi)

			if new<-10:
				new = -10.00

			if 10<new:
				new = 10.00

			N = Fuente()
			if j==0:
				N.datos[0] = new
				N.datos[1] = FA[i].datos[1].copy()
				N.funcion = funcion(N)
				N.fitness = fitness(N)

				cambio = Mejor_Dif(FA[i],N)
				if cambio == "NO":
					N.repe = N.repe+1
				else:
					FA[i].datos[0] = N.datos[0].copy()
					FA[i].datos[1] = N.datos[1].copy()
					FA[i].funcion = N.funcion
					FA[i].fitness = N.fitness
					FA[i].repe = 0

				print(k+1,' ',j,'\t',phi,'\t',N.datos[0],'\t',N.datos[1],'\t',N.funcion,'\t',N.fitness,'\t',cambio,'\t',N.repe)
			
			else:
				N.datos[0] = FA[i].datos[0].copy()
				N.datos[1] = new
				N.funcion = funcion(N)
				N.fitness = fitness(N)
				cambio = Mejor_Dif(FA[i],N)
				if cambio == "NO":
					N.repe = N.repe+1
				else:
					FA[i].datos[0] = N.datos[0].copy()
					FA[i].datos[1] = N.datos[1].copy()
					FA[i].funcion = N.funcion
					FA[i].fitness = N.fitness
					FA[i].repe = 0
				print(k+1,' ',j,'\t',phi,'\t',N.datos[0],'\t',N.datos[1],'\t',N.funcion,'\t',N.fitness,'\t',cambio,'\t',N.repe)

		#print()
		#print('Mostrar actualizaciones')
		#mostrar(FA)
		print()
		print('*** Calcular la Probabilidad de Selección de cada Fuente de Alimento ****')
		prop = Mostrar_Proba(FA)
		print()
		print('*** Enviar a Abejas Observadoras ****')
		for x in range(len(FA)):
			rand1 = round(np.random.uniform(0,1),3)
			i,k,j = Encontrar_ikj(prop,rand1)
			phi = round(np.random.uniform(-1,1),4)
			N = Fuente()

			new = V(FA[i].datos[j],FA[k].datos[j],phi)
			if j==0:
				N.datos[0] = new
				N.datos[1] = FA[i].datos[1].copy()
			else:
				N.datos[0] = FA[i].datos[0].copy()
				N.datos[1] = new

			N.funcion = funcion(N)
			N.fitness = fitness(N)

			cambio = Mejor_Dif(FA[i],N)

			if cambio == "NO":
				N.repe = FA[i].repe
				N.repe = N.repe+1
			else:
				FA[i].datos[0] = N.datos[0].copy()
				FA[i].datos[1] = N.datos[1].copy()
				FA[i].funcion = N.funcion
				FA[i].fitness = N.fitness
				FA[i].repe = 0

			print('** Observadora ',x+1,' - Aleatorio: ',rand1,'\t i=',i+1,' k=',k+1,' j=',j)
			
			print(phi,'  ',N.datos[0],'\t ',N.datos[1],'\t',N.funcion,'\t',N.fitness,'\t',cambio,'\t',N.repe)
			print('Nuevas Probabilidades')
			prop = Mostrar_Proba(FA)
			print()
		
		print('*** Enviar a Abejas Exploradoras ****')
		mostrar(FA)
		print()
		MFF = Mejor_Fuente(FA)
		if MFF.funcion<MFA.funcion:
			MFA.datos[0] = MFF.datos[0]
			MFA.datos[1] = MFF.datos[1]
			MFA.funcion = MFF.funcion
		
		print('*** Mejor Fuente de Alimento: [',MFA.datos[0],'\t',MFA.datos[1],']\t= ',MFA.funcion)
		print()
	






#################################
#################################
inicio()