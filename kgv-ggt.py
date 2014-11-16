# kgv-ggt.py	

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
	

# Hilfsfunktion für den Input
def getnumbers():
	result  = []
	while True:
		try:
			result.append(int(input("Zahl: ")))
		except ValueError as v:
			if str(v)[-1] + str(v)[-2] == "''":
				if not result:
					continue
				return sorted(result)
			print("Oops! Falsche Eingabe, bitte erneut versuchen.")


# Berechnet das kgV anhand der Primfaktorzerlegung
def kgv(numbers):
	result = 1
	primz = []
	for i in range(0, len(numbers)):
		primz.append(primes(max(numbers)))
		for j in range(0, len(primz[i])):
			while numbers[i] % primz[i][j][0] == 0:
				primz[i][j][1] += 1
				if primz[i][j][1] > primz[0][j][1]:
					primz[0][j][1] = primz[i][j][1]
				numbers[i] /= primz[i][j][0]
			if i == len(numbers) - 1:
				result *= primz[0][j][0] ** primz[0][j][1]
					
	return result


# Berechnet den ggT nach euklidschem Algorithmus
def ggt(numbers):
	rest = 0	
	for i in range(0, len(numbers)-1):
		while numbers[0] % numbers[1] != 0:
			rest = numbers[0] % numbers[1]
			numbers[0] = numbers[1]
			numbers[1] = rest
		numbers[0] = numbers[1]
		numbers[1] = numbers[i+1]
	
	return rest

	
# Hauptprogramm
print("Willkommen zum kgV / ggT Rechner.")

while True:
	op = str(input("\nGib k ein für kgV, g für ggT oder etwas anderes um zu beenden: "))
	if op == 'k':
		print("kgV: Bitte gib ein paar Zahlen ein. Lass die Eingabe leer um fortzufahren.")
		print("Das kgV deiner Zahlen lautet: " + str(kgv(getnumbers())))		
	elif str(op) == 'g':
		print("ggT: Bitte gib ein paar Zahlen ein. Lass die Eingabe leer um fortzufahren.")
		print("Der ggT deiner Zahlen lautet: " + str(ggt(getnumbers())))		
	else:
		print("Goodbye.")
		break
