myList = [1, 2.5, "alma", False]

print(len(myList))

print("A lista tarlamazza-e a 2.5 értéket: ", 1.5 in myList)

try:
    print("A 2.5 érték pozíciója a listában: ", myList.index(2.5))
except ValueError:
    print("hiba")

print("A lista 4.elemének lekérdezése:", myList[3])

print("A lista 4.elemének lekérdezése:", type(myList[0]))
print("A lista 4.elemének lekérdezése:", type(myList[1]))
print("A lista 4.elemének lekérdezése:", type(myList[2]))
print("A lista 4.elemének lekérdezése:", type(myList[3]))

print("A lista elso 2 eleme:", myList[0:2])

myList[2] = "körte"
print(myList)

myList.append(5)
print(myList)

myList.append([1, 2, 3])
print(myList)

myList.extend([1, 2, 3])
print(myList)

myList.insert(0, "start")
print(myList)

del(myList[7])
print(myList)

while 1 in myList:
    myList.remove(1)
print(myList)

myList = [4, 12, 6, 13, 8, 9]
print(myList)

myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

mylist2 = sorted(myList)

print(myList)
print(mylist2)

