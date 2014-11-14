# Just a simple program in python :-)

# Hilfsfunktion, berechnet alle Primzahlen <= n
def primes(n):
	result = []
	for i in range(2, n+1):
		for j in range(2, int(i/2)+1):
			if i % j == 0:
				break
		else:
			result.append([i, 0])
	
	return result
	

# Berechnet das kgV anhand Primfaktorenzerlegung
def kgv(a, b):
	# Berechne die Primzahlen
	primesa = primes(max(a,b))
	primesb = primes(max(a,b))
		
	# Berechne die Primzahlzerlegung
	for i in range(0, len(primesa)):
		while a % primesa[i][0] == 0:
			primesa[i][1] += 1
			a /= primesa[i][0]	
	for i in range(0, len(primesb)):				
		while b % primesb[i][0] == 0:
			primesb[i][1] += 1
			b /= primesb[i][0]
	
	# Berechen des Resultats
	result = 1
	for i in range(0, len(primesa)):
		if primesa[i][1] != 0:
			if primesb[i][1] != 0:
				result *= primesa[i][0] ** max(primesa[i][1], primesb[i][1])
			else:
				result *= primesa[i][0] ** primesa[i][1]
		elif primesb[i][1] != 0:			
				result *= primesb[i][0] ** primesb[i][1]
	
	return result
	

# Berechnet den ggT
def ggt(a, b):
	while a % b != 0:
		c = a % b
		a = b
		b = c
		
	return b
	

def getnumbers(n):
	result  = []
	for i in range(0, n):
		while True:
			try:
				result.append(int(input("Zahl" + str(i+1) + ": ")))
				break
			except ValueError:
				print("Oops! Falsche Eingabe, bitte erneut versuchen.")
	return result
	
	
# Hauptprogramm
print("Willkommen zum KGV / GGT Rechner.")

while True:
	op = str(input("""\nWas gibt es zu tun? 
Gib k ein für KGV, g für GGT oder etwas anderes um zu beenden: """))

	if op == 'k':
		val = getnumbers(2)
		print("Das kgV von {0} und {1} ist: {2}".format(val[0], val[1], kgv(val[0], val[1])))
		
	elif str(op) == 'g':
		val = getnumbers(2)
		print("Der ggT von {0} und {1} ist: {2}".format(val[0], val[1], ggt(val[0], val[1])))
		
	else:
		print("Goodbye.")
		break
	

# Not needed:
'''def kgv_m(numbers):
	# Berechne die Primzahlen
	primz = []
	for i in range(0, len(numbers)):
		primz.append(primes(max(numbers)))
		
	#primesa = primes(max(a,b))
	#primesb = primes(max(a,b))
		
	# Berechne die Primzahlzerlegung
	for i in range(0, len(numbers)):
		for j in range(0, len(primz[i])):
			while numbers[i] % primz[i][j][0] == 0:
				primz[i][j][1] += 1
				numbers[i] /= primz[i][j][0]
				
	print(primz)
	
	result = 1	
	val = []			
	for i in range(0, len(primz)):
		for j in range(0, len(primz[0])):
			val.append(primz[j][i])
			
	print(val)
	
	for i in range(0, len(val)):
		result =  result * (val[i][0] ** max(val[i][1]))
	
	print (val)		
	
	# Berechen des Resultats
	
	
	return result'''
