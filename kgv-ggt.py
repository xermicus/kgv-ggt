# Just a simple program in python :-)

print("Willkommen zu meinem einfach KGV / GGT Rechner.")

while True:
	op = str(input("Was gibt es zu tun? Gib k ein für KGV, g für GGT oder etwas anderes um zu beenden: "))
	if op == 'k':
		a = int(input("Ok, KGV. Die erste Zahl: "))
		b = int(input("Die zweite Zahl: "))
		
	elif str(op) == 'g':
		a = int(input("Ok, GGT. Die erste Zahl: "))
		b = int(input("Die zweite Zahl: "))
		
	else:
		print("Good bye.")
		break
	
