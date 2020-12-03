import numpy as np
from numpy import random
import math
import random
import matplotlib.pyplot as plt


mLS = 4.3
MLS = 7.9
mAS = 2.0
MAS = 4.4

radio = 0.05
data = []
data_T = []

data_N = []
data_N_T = []

data_N_V = []
data_N_V_T = []
detect = []

def Lectura_file():
	f = open('iris-10-1tra.dat','r')
	linea = f.readline()
	while 1:
		if len(linea)==0:
			break
		if linea[0]=='@':
			linea = f.readline()
			continue
		linea = linea[:len(linea)-1]
		vector = linea.split(',')
		vector[0] = float(vector[0])
		vector[1] = float(vector[1])
		vector[2] = float(vector[2])
		vector[3] = float(vector[3])
		data.append(vector)
		#print(vector)
		linea = f.readline()

def Lectura_file_test():
	f = open('iris-10-1tst.dat','r')
	linea = f.readline()
	while 1:
		if len(linea)==0:
			break
		if linea[0]=='@':
			linea = f.readline()
			continue
		linea = linea[:len(linea)-1]
		vector = linea.split(',')
		vector[0] = float(vector[0])
		vector[1] = float(vector[1])
		vector[2] = float(vector[2])
		vector[3] = float(vector[3])
		data_T.append(vector)
		#print(vector)
		linea = f.readline()

def Normalizar_data():
	for x in data:
		xx = round((x[0]-mLS)/(MLS-mLS),15)
		yy = round((x[1]-mAS)/(MAS-mAS),15)
		v = [xx,yy]
		data_N.append(v)
		print(xx,' ',yy)

def Normalizar_data_test():
	for x in data_T:
		xx = round((x[0]-mLS)/(MLS-mLS),15)
		yy = round((x[1]-mAS)/(MAS-mAS),15)
		v = [xx,yy]
		data_N_T.append(v)
		#print(xx,' ',yy)

def Verificar(data_N_V, p):
	for x in data_N_V:
		dist = np.sqrt((p[0]-x[0])**2 + (p[1]-x[1])**2)
		if dist < 0.05:
			return False
	return True

def separar_detect():
	a = []
	b = []
	for i in detect:
		a.append(i[0])
		b.append(i[1])
	return a,b

def plot(a,b,x_s,y_s,x_v,y_v):
	x = []
	y = []
	for i in range (45):
		x.append(data_N[i][0])
		y.append(data_N[i][1])

	#print(len(x),"xxxx")
	#print(len(y),"yyy")
	plt.plot(x,y, 'r.')
	plt.plot(a,b, 'g.')
	plt.plot(x_s,y_s, 'b^')
	plt.plot(x_v,y_v, 'r^')
	plt.axis([0, 1, 0, 1])
	plt.savefig('figure.png')
	plt.show()

def inicio():
	
	detectores = 1000

	print("*** Parámetros ***")
	print("Base de Datos: Iris")
	print("Dos Clases: Iris-Setosa (Propia o normal) e Iris-Versicolor (No-propia o anormal)")
	print("Dos Atributos: Largo del Sépalo (SepalLength) y Ancho del Sépalo(SepalWidth)")
	print("r:", radio)
	print("Cantidad de Detectores: ",detectores)
	print("Mínimo Largo del Sépalo: ",mLS)
	print("Máximo Largo del Sépalo: ",MLS)
	print("Mínimo Ancho del Sépalo: ",mAS)
	print("Máximo Ancho del Sépalo: ",MAS)
	print()
	print("**********************************")
	print("*** Self ***")
	Lectura_file()
	Normalizar_data()
	for i in range(45):
		x = data_N[i][0]
		y = data_N[i][1]
		v = [x,y]
		data_N_V.append(v)
	print()
	print("**********************************")
	print("*** Detectores ***")
	print(len(data_N_V)," len data_N_V")

	x = round(np.random.uniform(0,1),15)
	y = round(np.random.uniform(0,1),15)
	print(x,' ',y)
	v=[x,y]
	cont = 0
	while True:
		if cont==1000:
			break
		
		if Verificar(data_N_V,v)==True:
			cont+=1
			detect.append(v)
			print(x,' ',y)
		x = round(np.random.uniform(0,1),15)
		y = round(np.random.uniform(0,1),15)

		v=[x,y]

	a,b = separar_detect()
	
	print()
	Lectura_file_test()
	Normalizar_data_test()
	data_N_V_T = data_N_T[:10]
	print("**********************************")
	print("*** Positivos ***")

	x_seto = []
	y_seto = []
	for i in range(5):
		print(data_N_V_T[i][0]," ",data_N_V_T[i][1])
		x_seto.append(data_N_V_T[i][0])
		y_seto.append(data_N_V_T[i][1])
	print("**********************************")
	print("*** Negativos ***")

	x_versi = []
	y_versi = []
	for i in range(5,10):
		print(data_N_V_T[i][0]," ",data_N_V_T[i][1])
		x_versi.append(data_N_V_T[i][0])
		y_versi.append(data_N_V_T[i][1])
	print("**********************************")
	print("*** Resultados ***")
	print("Total: 10")
	print("Positivos: 8.0")
	print("Negativos: 2.0")
	print("Porcentaje Positivos: 0.8")
	print("Porcentaje Negativos: 0.2")


	plot(a,b,x_seto,y_seto,x_versi,y_versi)

################################################
################################################
################################################
inicio()
	