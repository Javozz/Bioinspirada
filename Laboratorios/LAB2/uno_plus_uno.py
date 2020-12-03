import numpy as np
import scipy.stats as st
from numpy import random
import math

poblacion = 0
desviacion = 0.2
iteraciones = 100
lamda = 1
# lamda = 1
# lamda = 1

namesfile = ["1+1.txt"]
pop=[]
id = 0
file = open(namesfile[id],"w")

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
	file.write("Calcular la Aptitud para cada Individuo\n")
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

def adaptacionOperador(o):
	do = 1/math.sqrt(2*math.sqrt(2));
	Ale1=np.random.normal(0,do)
	file.write("Aleatorio1: "+str(Ale1)+"\t ")
	return o * math.exp(Ale1)
	
def mutacion(h):
	#file.write("Mutacion\n")
	h.o1 = round(adaptacionOperador(h.o1),5)
	Ale2=np.random.normal(0.0, h.o1)
	file.write("Aleatorio2: "+str(Ale2)+"\n")
	h.x1 = h.x1 + Ale2
	h.o2 = round(adaptacionOperador(h.o2),5)
	Ale3 = np.random.normal(0.0, h.o2)
	file.write("Aleatorio2: "+str(Ale3)+"\n")
	h.x2 = h.x2 + Ale3

	#file.write("["+str(h.x1)+","+str(h.x2)+"] ["+str(h.o1)+","+str(h.o2)+"]\n\n")

	pop.append(h)

def mutacion2(h):
	file.write("Mutacion\n")
	A1 = random.rand()
	A2 = random.rand()

	var_1 = valor_x(-10.0,10.0,h.o1,0.0001,A1)
	var_2 = valor_x(-10.0,10.0,h.o2,0.0001,A2)

	var_1 = h.o1*math.exp(var_1)
	var_2 = h.o2*math.exp(var_2)

	h.x1 = h.x1 + var_1
	h.x2 = h.x2 + var_2

	file.write("Aleatorio1: "+str(A1)+"\n")
	file.write("Aleatorio1: "+str(A2)+"\n")



	file.write("["+str(h.x1)+","+str(h.x2)+"] ["+str(h.o1)+","+str(h.o2)+"]\n\n")
	pop.append(h)

def cruzamiento():
	mutacion(h1)

def seleccionarIndividuos():
	cruzamiento()

def menu():
	global lamda,poblacion,file,desviacion,iteraciones
	#print ("Eliga una opcion")
	print ("1+1.txt)")
	
	lamda = 1
	poblacion = 1
	file = open(namesfile[0],"w")

	file.write("Parametros:"+"\n")
	file.write("- Cantidad de Individuos (Mu): "+str(poblacion)+"\n")
	file.write("- Desviacion Estandar Inicial: "+str(desviacion)+"\n")
	file.write("- Cantidad de Genes por Individuo: 2"+"\n")
	file.write("- Cruzamiento Medio"+"\n")
	file.write("- Cantidad de Iteraciones: "+str(iteraciones)+"\n")
	file.write("\n")
	#file.write("MU: "+str(poblacion)+" LAMBDA: "+ str(lamda)+"\n")

def main():
	menu()
	crearPoblacion()
	mostrarPoblacion()
	mostrarAptitud()
	
	for x in range(1,iteraciones):
		global pop
		file.write( "**** Iteracion "+str(x)+"****\n")
		cadena = "[" +str(pop[0].x1 )+ " ,\t" +str( pop[0].x2) +"]"+": ["+str(pop[0].o1)+" , "+str(pop[0].o2)+"]\t: "+str(pop[0].fitness)
		file.write(cadena+"\n")
		
		mutacion2(pop[0])

		cadena = "[" +str(pop[1].x1 )+ " ,\t" +str( pop[1].x2) +"]"+": ["+str(pop[1].o1)+" , "+str(pop[1].o2)+"]\t: "+str(pop[1].fitness)+"\n"
		file.write(cadena+"\n")

		if(pop[0].fitness<pop[1].fitness):
			pop[0].o1=pop[0].o1*1.5**(-.25)
			pop[0].o2=pop[0].o2*1.5**(-.25)
		else:
			pop[0].x1=pop[1].x1
			pop[0].x2=pop[1].x1
			pop[0].o1=pop[0].o1*1.5
			pop[0].o2=pop[0].o2*1.5
		pop.pop()
		#mostrarAptitud()
		
		#mostrarAptitud()
	file.close()

main()
