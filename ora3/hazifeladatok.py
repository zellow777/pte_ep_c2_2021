#1.
print("Programozni tanulok".upper())

#2.
termekAr = int(input("Adja meg a term�k eredeti �r�t:"))

if termekAr < 10000:
	kedvezmeny = 10
else:
	kedvezmeny = 20

print("A term�k kedvezm�nyes �ra", termekAr * (1 - kedvezm�ny / 100), "Ft", kedvezmeny, "% kedvezm�nnyel")

#3.
nem = input("Adja meg a nem�t (l�ny=f, fi�=m):")
if nem == "m":
	print("Nem j�tszhat a csapatban")
elif nem == "f":
	kor = input("Adja meg a kor�t:")
		if kor <= 12 or kor >=10:
			print("J�tszhat a csapatban")
		else:
			print("Nem j�tszhat a csapatban")
else:
	print("Helytelen adatokat adott meg.")


