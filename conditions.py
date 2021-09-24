number = 10
if number < 10:
    print("Ez a szám kisebb, mint 10.")
else:
    print("Ez a szám nagyobb vagy egyenlő 10-el.")

if number < 100:
    print("Ez a szám kisebb, mint 100.")
else:
    print("Ez a szám nagyobb vagy egyenlő 100-al.")

if number % 2 == 1:
    print("A szám páratlan.")
else:
    print("A szám páros.")

number2 = 20
if number2 % number == 0:
    print("A number osztója a number2-nek.")
else:
    print("A number nem osztója a number2-nek.")

text = "Aabbaa"
if text[0] == text[-1]:
    print("A szöveg első és utolsó karaltere megegyezik")
else:
    print("A szöveg első és utolsó karaltere nem egyzik meg.")

if number == 0:
    print("A szám nulla.")
elif number % 2 == 1:
    print("A szám páratlan.")
else:
    print("A szám páros")

if text[0] == text.upper()[0]:
    print("A szöveg nagybetüvel kezdődik.")
else:
    print("A szöveg nem nagybetüvel kezdődik")

text2 = "aakkaaaa"
if text[0:5] == text2[0:5]:
    print("A szöveg első 5 karaktere megegyezik.")
else:
    print("A szöveg első 5 karaktere nem egyzik meg.")


