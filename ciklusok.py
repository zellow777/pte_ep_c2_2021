# while ciklus
i = 1
while i <= 5:
    print(i)
    i += 1

# even or odd
try:
    num = int(input("Please give me an integer: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
except ValueError:
    print("The input is not an integer")

# for ciklus
for i in [1, 2, 3, 4, 5]:
    print(i)

