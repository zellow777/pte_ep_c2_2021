width, lenght = 4, 5 #m
area = width * lenght

print("A szoba területe:", area, "m^2.")

lenght2 = 2 #m
area = width * lenght2
print("A szoba területe:", area, "m^2.")

width3 = lenght3 = 5 #m
area = width3 * lenght3

print("A szoba területe:", area, "m^2.")
# 1.feladat
days = 7
hoursInADay = 24
minutesInAnHour = 60
print("Egy hét", days*hoursInADay*minutesInAnHour, "percből áll.")
# 2. feladat
numStudents = 34
numApples = 124
applePerStudent = numApples // numStudents
applesLeft = numApples % numStudents
print("Egy diák ennyi almát kap:", applePerStudent, ". Ennyi alma marad a tanárnőnél: ", applesLeft, ".")
# 3.feladat
d = 24
r = d/2
Pi = 3.14

K = 2*r*Pi
T = (r**2)*Pi

print("A kör kerülete:", K, ", területe:", T, ".")
# 4.feladat
densityOlom = 11.34
densityRez = 8.69
terfogatOlom = 18
terfogatRez = 23
mOlom = densityOlom * terfogatOlom
mRez = densityRez * terfogatRez
if mRez > mOlom:
    print(terfogatRez, "m^3 réz nehezebb, mint", terfogatOlom, "m^3 ólom.")
else:
    print(terfogatRez, "m^3 réz könyebb, mint", terfogatOlom, "m^3 ólom.")
# 5. feladat
maxCapacity = 25 * 230
electricCircuit = 5 * 30 + 1500 + 1200 + 2000
if maxCapacity < electricCircuit:
    print("A megszakitó lekapcsolt.")
else:
    print("A megszakító nem kapcsolt le.")
# 6.feladat
speed = 48
distance = 64
timeInHours = distance / speed
timeInMinutes = timeInHours * 60
print("Az utat ", int(timeInMinutes), "percbe telik megtenni.")
# string műveletek
print("alma"[2:]*2)
# 7. feladat
print("python"[1])
print("python"[len("python")-1])
str = "Hiába a hegynyi anyag, a hallgató gyorsan halad"
strFind = "hallgató"
print(str[str.find(strFind):len(strFind)])

