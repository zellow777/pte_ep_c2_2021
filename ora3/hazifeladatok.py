#1.
print("Programozni tanulok".upper())

#2.
termekAr = int(input("Adja meg a termék eredeti árát:"))

if termekAr < 10000:
	kedvezmeny = 10
else:
	kedvezmeny = 20

print("A termék kedvezményes ára", termekAr * (1 - kedvezmény / 100), "Ft", kedvezmeny, "% kedvezménnyel")

#3.
nem = input("Adja meg a nemét (lány=f, fiú=m):")
if nem == "m":
	print("Nem játszhat a csapatban")
elif nem == "f":
	kor = input("Adja meg a korát:")
		if kor <= 12 or kor >=10:
			print("Játszhat a csapatban")
		else:
			print("Nem játszhat a csapatban")
else:
	print("Helytelen adatokat adott meg.")


