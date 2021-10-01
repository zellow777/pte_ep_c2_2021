menuCommand = ""
while menuCommand != "0":
    menuCommand = input("""Kérlek válassz a menüpontok közül:
    0-kilépés
    1-összeadás
    2-kivonás
    3-szorzás
    4-osztás
    """)
    if menuCommand == "1":
        isNumber = False
        a = 0
        b = 0
        while not isNumber:
            try:
                a = float(input("Adjon meg egy számot: "))
                isNumber = True
            except ValueError:
                print("A megadott érték nem szám")
            try:
                b = float(input("Adjon meg egy másik számot: "))
                isNumber = True
            except ValueError:
                print("A megadott érték nem szám")
        print(a + b)

print("Viszlát!")
