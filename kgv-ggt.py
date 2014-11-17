# kgv-ggt.py	

# Hilfsfunktion, berechnet alle Primzahlen <= n
# Diese Funktion wurde von untenstehendem Link entnommen und leicht angepasst, besten Dank:
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes2(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)            
    return [[2,0]] + [[2*i+1,0] for i in range(1,n//2) if sieve[i]]
	

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
	primz = primes2(max(numbers)+1)
	
	for i in range(0, len(numbers)):
		for j in range(0, len([p[0] for p in primz if p[0] < numbers[i]+1])):
			c = 0
			while numbers[i] % primz[j][0] == 0:
				c += 1
				numbers[i] /= primz[j][0]
			if c > primz[j][1]:
				primz[j][1] = c	
	for i in [ r[0] ** r[1] for r in primz if r[1] > 0]:
		result *= i
		
	return result
	

# Berechnet das kgV nach euklidschem Algorithmus
def ggt(numbers):
	for i in range(0, len(numbers)-1):
		while numbers[1]:      
			numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
		numbers[1] = numbers[i+1]
		
	return numbers[0]

	
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
