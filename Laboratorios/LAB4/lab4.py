

class Individuo:
	lista = ""
	fitness = 0
	num = []
	signo = []

class Poblacion:
	P = []

def convertir(PopT):

	for i in range(len(PopT.P)):
		tmp = ""
		for j in xrange(1,len(PopT.P[i].lista)):
			if PopT.P[i].lista[j] != '|':
				tmp = tmp + PopT.P[i].lista[j]
			else:
				
				

def inicio_prog_genetica():
	l1="|-1.0|+|-2.0|*|1.0|*|X|"
	l2="|-3.0|-|3.0|*|2.0|+|2.0|"
	l3="|-4.0|-|X|-|X|-|2.0|"
	l4="|-3.0|/|X|*|X|/|4.0|"
	l5="|1.0|+|-2.0|-|4.0|/|4.0|"
	l6="|-1.0|-|1.0|-|1.0|/|X|"
	l7="|3.0|/|-1.0|/|X|-|X|"
	l8="|-1.0|-|X|+|2.0|/|-3.0|"

	PopT = Poblacion()

	ind1 = Individuo()
	ind2 = Individuo()
	ind3 = Individuo()
	ind4 = Individuo()
	ind5 = Individuo()
	ind6 = Individuo()
	ind7 = Individuo()
	ind8 = Individuo()

	ind1.lista = l1
	ind2.lista = l2
	ind3.lista = l3
	ind4.lista = l4
	ind5.lista = l5
	ind6.lista = l6
	ind7.lista = l7
	ind8.lista = l8

	PopT.P.append(ind1)
	PopT.P.append(ind2)
	PopT.P.append(ind3)
	PopT.P.append(ind4)
	PopT.P.append(ind5)
	PopT.P.append(ind6)
	PopT.P.append(ind7)
	PopT.P.append(ind8)




########################################
 ###########    INICIO   ##############
########################################



inicio_prog_genetica()
