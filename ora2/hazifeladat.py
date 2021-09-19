import math 
#string exercise 2

text = "péntek van"

x = 0
while x < 7:
    print(text[0:6])
    x += 1

text = "Hiába a hegynyi anyag, a hallgató gyorsan halad."

word1 = "hegy"
word2 = "tananyag"

if word1 in text and word2 in text:
    print("A szöveg tartalmazza a szavakat")
else:
    print("A szöveg nem tartalmazza a szavakat")

word1 = "alma"
word2 = "Alma"

if word1 in word2:
    print("A szavak azonosak.")
else:
    print("A szavak nem azonosak")

print(word1 > word2)

#special characters

print("Specialiskarakter a backspace(\b), a sortores(\n), de van tabulator (\t), visszaperjel (\\), aposztrof(\') es idezojel(\") is. \n Az aposztrofotvisszaperjel nelkulis megadhatom ('), mert idezojelleljeloltema stringet.")
print("A kocsi visszatki ne hagyjuk (\r)")

#gomb térfogat

r = 5
volume = 4 * r**3 * 3.14 / 3
print(volume)

# 2 koordináta távolsága

a = (5, 2)
b = (4, 3)

distance = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
print(distance)

# szavak hossza és 10 karakternél hosszabbak

words = ["almaszár", "kerékgyártó", "Flóra-pihenő", "Malomvölgy", "Misina", "Égervölgyi tó", "Tenkes", "Zsolnay-kút"]

for word in words:
    numChar = str(len(word))
    print("A(z)" + word + " " + numChar + " karakterből áll.")

print("A 10 karakternél hoszabb szavak a kovetkezők:")
for word in words:
    numChar = len(word)
    if numChar > 10:
        print(word)

#festékes
roomArea = 75
bucketOfPaintArea = 15
bucketOfPaintPrice = 4300

if roomArea % bucketOfPaintArea == 0:
    paintNeeded = roomArea // bucketOfPaintArea
else:
    paintNeeded = roomArea // bucketOfPaintArea + 1

paintPriceSum = paintNeeded * bucketOfPaintPrice

print("A festőnek ", paintPriceSum, "FT értékben kell festéket vásárolnia")

speed = 60 / 13 #m2/h
hourRate = 2100

payForPaintingTheRoom = int(roomArea / speed * hourRate)

payWithTaxes = payForPaintingTheRoom * 1.27

print("Tibornak ", payForPaintingTheRoom, "Ft-ot kell fizetnie a munkáért, ez ", payWithTaxes,  "Ft adókkal együtt.")
