
import random

file = open("prog_evolutiva.txt","w")
ABC = ['A','B','C','D','E']
texto = ["Desactivar un estado","Cambia estado inicial","Cambiar simbolo de entrada","Cambiar simbolo de salida","Cambiar un estado de salida","Activar un estado"]

########################################
########################################

class estado:
	activo=0
	e1=0
	e2=0
	s1=0
	s2=0
	est1=0
	est2=0

class Mach:
	linea=""
	salida=""
	fitness=0

class Machines:
	M=[]

def ver(entrada):
	M1 = []
	for i in range(len(entrada)):
		if i%7 == 0:
			E1 = estado()
			E1.activo = entrada[i]
			E1.e1 = entrada[i+1]
			E1.e2 = entrada[i+2]
			E1.s1 = entrada[i+3]
			E1.s2 = entrada[i+4]
			E1.est1 = entrada[i+5]
			E1.est2 = entrada[i+6]
			M1.append(E1)
	return M1

def estado_inicial(M1):
	for i in range(len(M1)):
		if M1[i].activo == '2':
			#print(M1[i].activo+M1[i].e1+M1[i].e2+M1[i].s1+M1[i].s2+M1[i].est1+M1[i].est2)
			return i

def realizar_secuencia(maquinas, secuencia):
	global xfitness
	global xsecuencia
	global ABC
	inicio=0
	siguiente=0

	for i in range(len(maquinas.M)):
		salida_estados = ""
		salida_numeros = ""
		M1 = ver(maquinas.M[i].linea)
		inicio = estado_inicial(M1)
		for num in range(len(secuencia)):
			if M1[inicio].e1 == secuencia[num] :
				#print(M1[inicio].est1, end='')
				salida_estados = salida_estados + M1[inicio].est1
				salida_numeros = salida_numeros + M1[inicio].s1
				inicio = ABC.index(M1[inicio].est1)
			else:
				#print(M1[inicio].est2, end='')
				salida_estados = salida_estados + M1[inicio].est2
				salida_numeros = salida_numeros + M1[inicio].s2
				inicio = ABC.index(M1[inicio].est2)

		maquinas.M[i].salida = salida_numeros

		fitness=0
		for j in range(len(secuencia)-1):

			if secuencia[j+1] == salida_numeros[j]:
				fitness+=1

		maquinas.M[i].fitness = fitness/40

def mostrar_parametros():
	file.write("Parametros:\n")
	file.write("Cantidad de individuos: "+str(individuos)+" \n")
	file.write("Cantidad Maxima de estados: "+str(estados)+"\n")
	file.write("Cantidad de iteraciones: "+str(iteraciones)+"\n")
	file.write("\n")	

def mostrar_poblacion(maquinas):
	for i in range(len(maquinas.M)):
		file.write(str(i+1)+") "+maquinas.M[i].linea+'\n')

def mostrar_fitness(maquinas,secuencia):
	for i in range(len(maquinas.M)):
		file.write(str(i+1)+") "+maquinas.M[i].linea+" - "+secuencia+" - "+maquinas.M[i].salida+" - "+str(maquinas.M[i].fitness)+'\n')

def mutaciones(Aleatorio):
	if 0<Aleatorio and Aleatorio<0.1:
		return 0
	elif 0.1<Aleatorio and Aleatorio<0.3:
		return 1
	elif 0.3<Aleatorio and Aleatorio<0.5:
		return 2
	elif 0.5<Aleatorio and Aleatorio<0.7:
		return 3
	elif 0.7<Aleatorio and Aleatorio<0.9:
		return 4
	else:
		return 5

def unir_machine(M):
	cadena = ""
	for i in range(len(M)):
		cadena = cadena+M[i].activo+M[i].e1+M[i].e2+M[i].s1+M[i].s2+M[i].est1+M[i].est2

	return cadena

def desactivar_estado(M, B_estado):
	global ABC

	if M[B_estado].activo == '2':
		M[B_estado].activo = '0'

		ini = random.randint(0,4)
		while ini==B_estado:
			ini = random.randint(0,4)
			
		if M[ini].activo == '1':
			M[ini].activo = '2'
			for i in range(len(M)):
				if i!=B_estado:
					if M[i].est1 == ABC[B_estado]:
						no_apuntar = random.randint(0,4)
						while no_apuntar == B_estado:
							no_apuntar = random.randint(0,4)
						M[i].est1 = ABC[no_apuntar]
				
					if M[i].est2 == ABC[B_estado]:
						no_apuntar = random.randint(0,4)
						while no_apuntar == B_estado:
							no_apuntar = random.randint(0,4)
						M[i].est2 = ABC[no_apuntar]

		elif M[ini].activo == '0':
			M[ini].activo = '2'
			for i in range(len(M)):
				if i!=B_estado:
					if M[i].est1 == ABC[B_estado]:
						no_apuntar = random.randint(0,4)
						while no_apuntar == B_estado:
							no_apuntar = random.randint(0,4)
						M[i].est1 = ABC[no_apuntar]
				
					if M[i].est2 == ABC[B_estado]:
						no_apuntar = random.randint(0,4)
						while no_apuntar == B_estado:
							no_apuntar = random.randint(0,4)
						M[i].est2 = ABC[no_apuntar]

	elif M[B_estado].activo == '1':
		M[B_estado].activo = '0'
		for i in range(len(M)):
			if i!=B_estado:
				if M[i].est1 == ABC[B_estado]:
					no_apuntar = random.randint(0,4)
					while no_apuntar == B_estado:
						no_apuntar = random.randint(0,4)
					M[i].est1 = ABC[no_apuntar]
				
				if M[i].est2 == ABC[B_estado]:
					no_apuntar = random.randint(0,4)
					while no_apuntar == B_estado:
						no_apuntar = random.randint(0,4)
					M[i].est2 = ABC[no_apuntar]

	cadena = unir_machine(M)

	#file.write(cadena+" mutado\n")
	return cadena
	#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

def cambiar_estado_inicial(M, B_estado):
	for i in range(len(M)):
		if M[i].activo == '2':
			M[i].activo = '1'
	M[B_estado].activo = '2'
	cadena = unir_machine(M)
	return cadena

def activar_estado(M, B_estado):
	global ABC
	if M[B_estado].activo=='0':
		M[B_estado].activo = '1'
		randd = random.randint(0,4)
		while randd == B_estado:
			randd = random.randint(0,4)
		randi = random.randint(0,1)
		if randi == 0:
			M[randd].est1 = ABC[B_estado]
		else:
			M[randd].est2 = ABC[B_estado]

	cadena = unir_machine(M)
	return cadena

def operar_mutaciones(tipo, machine, B_estado):
	global ABC
	M = ver(machine.linea)
	if tipo == 0:
		#Desactivar estado
		cadena = desactivar_estado(M,B_estado)
		return cadena
		#file.write(machine.linea+" mutado\n")

	elif tipo == 1:
		#Cambiar estado inicial
		cadena = cambiar_estado_inicial(M,B_estado)
		#print(cadena, '<<')
		return cadena
		#file.write(machine.linea+" mutado\n")
		#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

	elif tipo == 2:
		#Cambiar simbolo de entrada
		if M[B_estado].e1 == '1':
			M[B_estado].e1 = '0'
			M[B_estado].e2 = '1'
		else:
			M[B_estado].e1 = '1'
			M[B_estado].e2 = '0'
		cadena = unir_machine(M)
		return cadena
		#file.write(machine.linea+" mutado\n")
		#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

	elif tipo == 3:
		#Cambiar simbolo de salida
		randd = random.randint(0,1)
		if randd == 0:
			if M[B_estado].s1=='1':
				M[B_estado].s1 = '0'
			else:
				M[B_estado].s1 = '1'
		else:
			if M[B_estado].s2=='1':
				M[B_estado].s2 = '0'
			else:
				M[B_estado].s2 = '1'
		cadena = unir_machine(M)
		return cadena
		#file.write(machine.linea+" mutado\n")
		#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

	elif tipo == 4:
		#Cambiar estado de salida
		randd = random.randint(0,1)
		if randd == 0:
			cambio = M[B_estado].est1
			ran = random.randint(0,4)
			letra = ABC[ran]
			while letra == M[B_estado].est1:
				ran = random.randint(0,4)
				letra = ABC[ran]
			M[B_estado].est1 = letra
		else:
			cambio = M[B_estado].est2
			ran = random.randint(0,4)
			letra = ABC[ran]
			while letra == M[B_estado].est2:
				ran = random.randint(0,4)
				letra = ABC[ran]
			M[B_estado].est2 = letra
		cadena = unir_machine(M)
		return cadena
		#file.write(machine.linea+" mutado\n")
		#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

	elif tipo == 5:
		#Activar estado
		cadena  = activar_estado(M,B_estado)
		return cadena
		#file.write(machine.linea+" mutado\n")
		#print(M[B_estado].activo, M[B_estado].e1, M[B_estado].e2, M[B_estado].s1, M[B_estado].s2, M[B_estado].est1, M[B_estado].est2)

def mejores(new_maquinas, maquinas, secuencia):

	M22 = new_maquinas
	me1=[]
	me2=[]
	for i in range(len(new_maquinas.M)):
		temp1 = []
		temp2 = []
		temp1.append(i)
		temp1.append(new_maquinas.M[i].fitness)

		temp2.append(i)
		temp2.append(maquinas.M[i].fitness)

		me1.append(temp1)
		me2.append(temp2)

	me1.sort(key=lambda x:x[1])
	me2.sort(key=lambda x:x[1])

	#for x in range(len(me1)):
	#	print(me1[x][0],' << ',me1[x][1])

	file.write("\n")
	file.write("Mejores Ascendientes\n")
	for j in range(4):
		file.write(maquinas.M[me2[7-j][0]].linea+" - "+secuencia+" - "+maquinas.M[me2[7-j][0]].salida+" - "+str(maquinas.M[me2[7-j][0]].fitness)+"\n")

	file.write("\n")
	file.write("Mejores Descendientes\n")
	for y in range(4):
		file.write(new_maquinas.M[me1[7-y][0]].linea+" - "+secuencia+" - "+new_maquinas.M[me1[7-y][0]].salida+" - "+str(new_maquinas.M[me1[7-y][0]].fitness)+"\n")


	for i in range(0,4):
		#print(i, 'i')
		M22.M[i] = maquinas.M[me2[7-i][0]]

	for j in range(4,8):
		#print(j, ' j')
		M22.M[j] = new_maquinas.M[me1[7-j][0]]

	return M22

def inicio(individuos,estados,iteraciones):
	global ABC
	secuencia = "0111001010011100101001110010100111001010"
	m1 = Mach()
	m2 = Mach()
	m3 = Mach()
	m4 = Mach()
	m5 = Mach()
	m6 = Mach()
	m7 = Mach()
	m8 = Mach()

	m1.linea = "21011ED01000DC11011CA11011CE10111CD"
	m2.linea = "10101AD00101AA21011EC00111EC11011CC"
	m3.linea = "21001DC10101AC10101EE11011ED10111AD"
	m4.linea = "10100ED11001CC20101AC10111AC10111DA"
	m5.linea = "10110AE21011CC10100AB00110EB10110EA"
	m6.linea = "11001DA20100DC10100ED11001CB11011CE"
	m7.linea = "10101BB11010AE21011AC10101AB10100EB"
	m8.linea = "10101AC11011BE20110BC11010AD10101AC"

	maquinas = Machines()
	new_maquinas = maquinas
	
	maquinas.M.append(m1)
	maquinas.M.append(m2)
	maquinas.M.append(m3)
	maquinas.M.append(m4)
	maquinas.M.append(m5)
	maquinas.M.append(m6)
	maquinas.M.append(m7)
	maquinas.M.append(m8)

	realizar_secuencia(maquinas, secuencia)
	mostrar_parametros()
	file.write("Poblacion Inicial\n")
	mostrar_poblacion(maquinas)
	file.write("\nCalcular Aptitud de cada Individuo\n")
	mostrar_fitness(maquinas,secuencia)
	for i in range(iteraciones):
		file.write("\n###### Iteracion "+str(i+1)+" ######\n")
		for j in range(len(maquinas.M)):
			file.write("Mutacion"+str(j+1)+"\n")
			file.write(maquinas.M[j].linea+"\n")
			A = random.random()
			B = random.randint(0,4)
			
			valor = mutaciones(A)
			file.write("Aleatorio: "+str(A)+"\n")
			file.write(texto[valor]+"\n")

			file.write("Estado Seleccionado: "+ABC[B]+"\n")
			
			cadena = operar_mutaciones(valor,maquinas.M[j],B)
			#print(maquinas.M[j].linea, 'original')
			#print(cadena)
			new_maquinas.M[j].linea=cadena
			#print(new_maquinas.M[j].linea, 'mutado' )

			file.write(new_maquinas.M[j].linea+"\n")
			file.write("\n")

		file.write("Descencientes\n")	
		realizar_secuencia(new_maquinas,secuencia)
		mostrar_fitness(new_maquinas,secuencia)

		maquinas = mejores(maquinas,new_maquinas,secuencia)
		file.write("\n")
		file.write("Nueva Poblacion\n")
		mostrar_fitness(maquinas,secuencia)
	file.close()

########################################
 ###########    INICIO   ##############
########################################
#secuencia = "0 1 1 1 0 0 1 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 1 1 0 0 1 0 1 0"

individuos = 8
estados = 5
iteraciones = 200

inicio(individuos,estados,iteraciones)







