import numpy as np
from numpy import random
import scipy.stats as st
#import random
import math

poblacion = 0
desviacion = 0.2
iteraciones = 1000
lamda = 1

# lamda = 1
# lamda = 1

namesfile = ["u+1.txt","u+y.txt","u_coma_y.txt"]
pop=[]
id = 0
file = open(namesfile[id],"w")
# file = open("u+y.txt","w")
# file = open("u_y.txt","w")

def ordenar( x, y ) :
    return  x.fitness > y.fitness

class indv:
	global desviacion
	fitness = 0
	x1 = 0
	x2 = 0
	porcent = 0
	o1=desviacion
	o2=desviacion
    
def funcion(x1, x2):
	return -math.cos(x1)*math.cos(x2)*math.exp(-math.pow(x1-math.pi,2)-pow(x2-math.pi,2))
	# return x1 - (x1/3)

def mostrarAptitud():
	i=1
	for x in pop:
		cadena = str(i)+")  [" +str(x.x1 )+ " ,\t" +str( x.x2) +"]"+": ["+str(x.o1)+" , "+str(x.o2)+"]\tFitness: "+str(x.fitness)
		file.write(cadena+"\n")
		i+=1
	file.write("\n")

def mostrarPoblacion():
	file.write( "Poblacion\n")
	i=1
	for x in pop:
		cadena = str(i)+")  [" +str(x.x1 )+ " ,\t" +str( x.x2) +"]"+": ["+str(x.o1)+" , "+str(x.o2)+"]"
		file.write(cadena+"\n")
		i+=1
	file.write("\n")

def metodoTorneo():
		# file.write( "torneo")
		# global poblacion
		p1 = random.randint(0,poblacion-1)
		p2 = random.randint(0,poblacion-1)
		# file.write( str(p1)+"-"+str(p2)+"\n")
		while p1 == p2:
			p2 = random.randint(0,poblacion-1)
		# file.write( "torneo2s")

		#### Minimizacion
		if (pop[p1].fitness < pop[p2].fitness):
			file.write("Padre: "+ str(p1+1) +" - "+ str(p2+1) +" => "+ str(p1+1) +" ["+ str(pop[p1].x1 ) +" ,"+ str(pop[p1].x2) +"]"+" ["+ str(pop[p1].o1) +" , "+ str(pop[p1].o2) +"]\n")
			return p1
		else:
			file.write("Padre: "+ str(p1+1) +" - "+ str(p2+1) +" => "+ str(p2+1) +" ["+ str(pop[p2].x1 ) +" ,"+ str(pop[p2].x2) +"]"+" ["+ str(pop[p2].o1) +" , "+ str(pop[p2].o2) +"]\n")
			return p2

def operadorSeleccion():
	for x in range(0,lamda):
		pop.pop()

def crearPoblacion():
	# poblacion = random.randint(8,15)
	for x in range(0,poblacion):
		s1 = indv()
		s1.x2 =  round(random.uniform(-10,10),5)
		s1.x1 =  round(random.uniform(-10,10),5)
		s1.fitness = funcion(s1.x1, s1.x2)
		pop.append(s1)
	pop.sort(key=lambda x: x.fitness)

def normal(x , desvio):
	retorno = -0.5 * (math.pow(x / desvio, 2))
	retorno = math.exp(retorno)
	retorno = retorno / (desvio * math.sqrt(6.283284))
	return retorno;

def valor_x(lim_inf, lim_sup, desvio, delta, aleatorio):
	area = 0
	aux = normal(lim_inf,desvio)
	for i in np.arange(lim_inf+delta,lim_sup,delta):
		aux_suma = normal(i,desvio)
		area += (aux+aux_suma)
		if ((area*(delta/2.0)) > aleatorio):
			return i
		aux=aux_suma
	return -1

def adaptacionOperador(o):
	do = 1/math.sqrt(2*math.sqrt(2))
	Ale1=np.random.normal(0,do)
	file.write("Aleatorio1: "+str(Ale1)+"\t ")
	return o * math.exp(Ale1)
	
def mutacion(h):
	file.write("Mutacion\n")
	A1 = random.rand()
	A2 = random.rand()
	A3 = random.rand()
	A4 = random.rand()

	var_1 = valor_x(-10.0,10.0,0.59460356,0.0001,A1)
	var_2 = valor_x(-10.0,10.0,0.59460356,0.0001,A2)
	h.o1 = h.o1*math.exp(var_1)
	h.o2 = h.o2*math.exp(var_2)

	var_1 = valor_x(-10.0,10.0,h.o1,0.0001,A3)
	var_2 = valor_x(-10.0,10.0,h.o2,0.0001,A4)
	h.x1 = h.x1 + var_1
	h.x2 = h.x2 + var_2

	file.write("Aleatorio1: "+str(A1)+"\t"+"Aleatorio2: "+str(A3)+"\n")
	file.write("Aleatorio1: "+str(A2)+"\t"+"Aleatorio2: "+str(A4)+"\n")

	#h.o1 = round(adaptacionOperador(h.o1),5)
	#Ale2=np.random.normal(0.0, h.o1)

	#file.write("Aleatorio2: "+str(Ale2)+"\n")
	#h.x1 = h.x1 + Ale2
	#h.o2 = round(adaptacionOperador(h.o2),5)
	#Ale3 = np.random.normal(0.0, h.o2)

	#file.write("Aleatorio2: "+str(Ale3)+"\n")

	file.write("["+str(h.x1)+","+str(h.x2)+"] ["+str(h.o1)+","+str(h.o2)+"]\n\n")
	pop.append(h)

def cruzamiento(a,b):
	file.write("Cruzamiento\n")
	h1 = indv()
	h1.x1 = 0.5 * (a.x1+b.x1)
	h1.x2 = 0.5 * (a.x2+b.x2)
	h1.o1 =round(math.sqrt(a.o1 * b.o1),5)
	h1.o2 =round(math.sqrt(a.o2 * b.o2),5)
	h1.fitness = funcion(h1.x1, h1.x2)
	file.write("["+str(h1.x1)+","+str(h1.x2)+"] ["+str(h1.o1)+","+str(h1.o2)+"]\n")
	mutacion(h1)

def seleccionarIndividuos():
	for x in range(0,lamda):
		#file.write( "De: "+str(len(pop))+" individuos\n")
		file.write( "Generar Descendiente "+str(x+1)+"\n")
		file.write( "Seleccion de Padres\n")
		p1 = metodoTorneo()
		p2 = metodoTorneo()

		#file.write( "Seleccionando individuos\n")
		#file.write( "p1: "+str(p1+1)+"\n")
		#file.write( "p2: "+str(p2+1)+"\n")
		cruzamiento(pop[p1],pop[p2])
	
	# file.write( "oooooooooooooo1")

def menu(c):
	global lamda,poblacion,file,desviacion,iteraciones
	poblacion=8
	numero = c
	if(numero == 1):
		lamda = 1

		file = open(namesfile[0],"w")
	elif(numero == 2):
		lamda = random.randint(2,poblacion)
		#poblacion = random.randint(lamda+1,15)
		file = open(namesfile[1],"w")
	else:
		lamda = random.randint(poblacion,15)
		#poblacion = random.randint(5,lamda)
		file = open(namesfile[2],"w")

	file.write("Parametros:"+"\n")
	file.write("- Cantidad de Individuos (Mu): "+str(poblacion)+"\n")
	file.write("- Cantidad de Descendientes (Lambda): "+str(lamda)+"\n")
	file.write("- Desviacion Estandar Inicial: "+str(desviacion)+"\n")
	file.write("- Cantidad de Genes por Individuo: 2"+"\n")
	file.write("- Selección por torneo (2)"+"\n")
	file.write("- Cantidad de Iteraciones: "+str(iteraciones)+"\n")
	file.write("\n")
	#file.write("MU: "+str(poblacion)+" LAMBDA: "+ str(lamda)+"\n")

def main(opc):
	menu(opc)
	crearPoblacion()
	mostrarPoblacion()
	file.write("Calcular la Aptitud para cada Individuo\n")
	mostrarAptitud()
	
	for x in range(1,iteraciones):
		file.write( "**** Iteracion "+str(x)+"****\n")
		#file.write("desviacion: "+str(desviacion)+"\n")
		seleccionarIndividuos()
		#mostrarPoblacion()
		file.write("Unir mu individuos con lambda descendientes\n")
		mostrarAptitud()
		pop.sort(key=lambda x: x.fitness)
		operadorSeleccion()
		file.write( "Escoger los mejores mu (Nueva Poblacion)\n")
		#mostrarPoblacion()
		mostrarAptitud()
	file.close()

main(1)
pop=[]
main(2)
pop=[]
main(3)
pop=[]
print("Archivo generado")
print()

