print("AUTOŠKOLA - CVIČNÝ TEST")
print("-----------------------")
def test():
    pocetBodu = 0
    pocetBoduMax = 5
    otazka1 = input("Odkud dává řidič přednost, pokud křižovatka není nijak zvláštně značena? Zleva/zprava")
    if otazka1.lower()=="zprava":
        print("Správně")
        pocetBodu+=1
    else:
        print("Špatně. Řidič musí dát přednost zprava")

    otazka2 = input("Jsou světelné signály podřízeny svislým dopravním značkám? Ano/ne")
    if otazka2.lower() == "ne":
        print("Správně")
        pocetBodu += 1;
    else:
        print("Špatně. Semafor je vždy nadřazen!")

    otazka3 = input("Přeškrtnutý kosočtverec znamená hlavní pozemní komunikace: konec/začátek")
    if otazka3.lower() == "konec":
        print("Správně")
        pocetBodu+=1;
    else:
        print("Špatně. Je to naopak!")

    otazka4 = input("Je řidič povinen při každé nehodě volat PČR? Ano/ne")
    if otazka4.lower() == "ne":
        print("Správně")
        pocetBodu+=1;
    else:
        print("Špatně. Musí volat pouze, pokud vznikla hmotná škoda převyšující 100 tis. Kč.")

    otazka5 = input("Podléhá přívesný vozík registraci? Ano/ne")
    if otazka5.lower() == "ano":
        print("Správně")
        pocetBodu += 1;
    else:
        print("Špatně. Podléhá, má vlastní SPZ")

    procenta = 100 * float(pocetBodu)/float(pocetBoduMax)
    print("Celkový počet bodů", pocetBodu)

    print("Procentuální výsledek:", procenta, "%")
    if(procenta>=85):
        print("Prospěl")
    else:
        print("Neprospěl")
test()