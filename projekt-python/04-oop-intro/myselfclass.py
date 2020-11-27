import math # importovaná knihovna math pro funkce jako např. math.pi atd.

# Definice třídy Kuzel
class Kuzel:
    # Atributy na úrovni třídy
    jednotka = "metr"
    zkratka_jednotky = "m"

    # Inicializační metoda __init__ deklaruje kontruktor, čili inicializuje objekt (v tomto případě Kužel)
    def __init__(self, polomer, vyska, vyska_steny):
        # Atributy na úrovni objektu
        self.r = polomer
        self.v = vyska
        self.s = vyska_steny

    # Magická metoda pro výpis textové informace o objektu
    def __str__(self):
        return f'({self.r}, {self.v}, {self.s})'

    # Magická metoda, která zjistí, jestli jsou dva kužely totožné
    def __eq__(self, other):
        return self.r == other.r and self.v == other.v and self.s == other.s

    # Magická metoda, která zjistí, který z objektů má větší výšku stěny
    def __gt__(self, other):
        return self.s > other.s

    def __add__(self, other):
        # Sečte parametry a vrátí úplně nový objekt
        return Kuzel(self.r + other.r, self.v + other.v, self.s + other.s)

    # Magická metoda, která odečtením dvou objektů zjistí, o kolik je jeden kužel vyšší než druhý
    def __sub__(self, other):
        # Pokud uživatel mylně zadá, že se odečítá vyšší kužel, tak to program automaticky přetransformuje
        if self.v > other.v:
            return self.v - other.v
        else:
            return other.v - self.v

    # Statická metoda pro kontrolu parametru, tzn. kužel nemůže existovat se zápornými hodnotami, to je nonsens
    @staticmethod
    def platnost_parametru(parameter):
        # Pokud je parameter menší nebo roven nule, nelze považovat stranu za kužel, takže parametr nevyhovuje
        if parameter <= 0:
            raise Exception('Nevyhovujici parametr!')
        # Jinak se přes to přenese, a jde se dál (True)
        else:
            return True

    # Metoda třídy pro výpis jednotek
    @classmethod
    def vypis_jednotek(cls):
        print('Jednotka: ', cls.jednotka, ', ', 'zkratka: ', cls.zkratka_jednotky)

    # Vrácení hodnoty poloměru prostřednictvím dekorátoru property, "zvenčí"
    @property
    def polomer(self):
        return self.r

    # Nastavení hodnoty poloměru prostřednictvím dekorátoru @.setter
    @polomer.setter
    def polomer(self, hodnota):
        # Validace hodnoty, zdali odpovídá požadovanému číslu a funkci platnost_parametru
        try:
            hodnota = float(hodnota)
            self.platnost_parametru(hodnota)
            self.r = hodnota
        except:
        # Pakliže neplatí, hodí chybovou hlášku
            raise ValueError("Špatně zadaná hodnota pro nastavení poloměru.")


    # Metoda pro výpočet objemu objektu kuželu
    def objem(self):
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.v):
            return (math.pi * (self.r ** 2) * self.v)/3

    # Metoda pro výpočet povrchu objektu kuželu
    def povrch(self):
        # Nejprve (před samotným výpočtem) provede kontrolu platnosti čísla - zdali je vyšší od nuly
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.s):
            return math.pi * self.r * (self.r + self.s)

# Definice potomka třídy Kuzel
class Komoly_kuzel(Kuzel):

    # Výchozí kontruktor s předanými + dodanými parametry výchozího objektu
    def __init__(self, polomer, polomer2, vyska, vyska_steny):
        # Metoda super() nám umožňuje přistupovat k hodnotám (spíše metodám) předka - třídy Kuzel
        super().__init__(polomer, vyska, vyska_steny)
        # Nový parametr r2, jenž představuje poloměr vrchní kružnice komolého kuželu
        self.r2 = polomer2

    # Metoda pro výpočet objemu komolého kuželu
    def objem(self):
        # Převezmeme veškeré metody od předka třídy
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.v) and self.platnost_parametru(self.r2):
            # Zde akorát přepíšeme returnovací funkci z předka, abychom mohli vypočítat objem komolého kuželu
            return (math.pi * self.v * (self.r ** 2 + self.r*self.r2 + self.r2 ** 2)) / 3

    # Metoda pro výpočet povrchu komolého kuželu
    def povrch(self):
        # Převezmeme veškeré metody od předka třídy
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.s):
            # Zde akorát přepíšeme returnovací funkci z předka, abychom mohli vypočítat povrch komolého kuželu
            return (math.pi * self.r ** 2) + (math.pi * self.r2 ** 2) + (math.pi*(self.r + self.r2) * self.s)

# Vytvoření objektu kužele k1
k1 = Kuzel(5, 1, 2)

# Nastavení hodnoty polomeru u objektu k1 na základě setteru @polomer.setter
k1.polomer = 5.2
# Vypsání hodnoty poloměru
print(k1.polomer)

# Vytvoření objektu kužele k2
k2 = Kuzel(5, 2, 1)

# Vytvoření objektu komolého kuželu k3 z dedičnosti toho původního
k3 = Komoly_kuzel(5, 2, 3, 2)

# Ověříme, zdali je objekt k1 instancí třídy Kuzel
print(isinstance(k1, Kuzel))

# Funkčnost magických metod:
print("Ověření funkčnosti magických metod:")
print("-----------------------------------")

# Převedení objektu na textový řetězec
print(str(k1), ',', str(k2))

# Kontrola, jestli jsou kužely totožné
print(k1 == k2)

# Kontrola, jestli je objekt k1 větší než objekt k2
print(k1 > k2)

# Sečte objekty a vrátí nový objekt
print(k1 + k2)

# Odečte objekty, a zjistí, o kolik je nejvyšší kužel vyšší
print(k1 - k2)

# Výpočet objemu kužele:
print('Objem kužele je: ',round(k1.objem(), 2), 'm')

# Výpočet povrchu kužele:
print('Povrch kužele je: ',round(k1.povrch(), 2), 'm')

# Zavolám metodu třídy Kuzel, která vypíše jednotky používané v této třídě
Kuzel.vypis_jednotek()
print("\n")

# Ověříme, jestli objekt k3 je instancí třídy Komoly_kuzel, jež je potomkem třídy Kuzel
print(isinstance(k3, Komoly_kuzel))

# Výpočet objemu komolého kuželu k3
print('Objem komolého kuželu je: ', round(k3.objem(), 2), 'm3')

# Výpočet povrchu komolého kuželu k3
print('Povrch komolého kuželu je:', round(k3.povrch(), 2), 'm2')
