# 1.Írjon programot, ami kiírja a 10x10-es szorzótáblát!
szorzotabla = list()
for row in range(1, 11):
    for col in range(1, 11):
        szorzotabla.append(row*col)

s = 0
e = 10
while s <= 90 and e <= 100:
    print(szorzotabla[s:e])
    s += 10
    e += 10

# 2.Írjon programot, ami egy mértani sorozat első 2 eleme alapján meghatározza és kiírja az N. elemet!
a1 = int(input("Adja meg a sorozat első tagját:"))
a2 = int(input("Adja meg a sorozat második tagját:"))
n = int(input("Adja meg hogy a sorozat hányadik tagját szeretné megkapni:"))

q = a2/a1

an = a1
while n > 0:
    an = an * q
    n -= 1

print("A sorozat n-edik tagja:", an)
# 3.Adja meg a Pascal-háromszög első N sorát!A Pascal-háromszög n.sorának k. elemének képlete: (n + 1 -k) / k
num = int(input("Adja meg n értékét:"))

matrix = [[0 for x in range(num)]
          for y in range(num)]

for n in range(0, num):
    for k in range(0, n + 1):
        if k == 0:
            matrix[n][k] = 1
        else:
            matrix[n][k] = (matrix[n - 1][k - 1] + matrix[n - 1][k])

i = 0
while i < num:
    print(matrix[i])
    i += 1

# 4. Kérjen be egy szöveget és döntse el, hogy palindrom-e! pl. radar
text = input("Adjon meg egy szót:")

chars = list()
for char in text:
    chars.append(letter)

if chars == chars[::-1]:
    print("A szöveg palidrom.")
else:
    print("A szöveg nem palidrom")