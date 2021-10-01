# 1.
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# 2.
for i in range(1, 13, 2):
    print(i)

# 3.
a1 = 0
a2 = 1
print(a1, a2, end=" ")
while i < 8:
    an = a1 + a2
    a1 = a2
    a2 = an
    print(an, end=" ")
    i += 1
# 4.

# 5.
text = input("Adjon meg egy szöveget:")
num = 0
for i in text:
    if i == "e":
        num += 1
print("Ennyi e betüt tartalmaz: ", num)
