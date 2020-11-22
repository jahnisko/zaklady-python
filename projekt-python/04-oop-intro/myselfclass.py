import math # importovaná knihovna math pro funkce jako např. math.pi atd.
class Kuzel:
    # Atributy na úrovni třídy
    jednotka = "metr"
    zkratka_jednotky = "m"

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
        if parameter <= 0:
            return False
        else:
            return True

    # Metoda třídy pro výpis jednotek
    @classmethod
    def vypis_jednotek(cls):
        print('Jednotka: ', cls.jednotka, ', ', 'zkratka: ', cls.zkratka_jednotky)

    # Metoda pro výpočet objemu objektu kuželu
    def objem(self):
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.v):
            return (math.pi * (self.r ** 2) * self.v)/3

    # Metoda pro výpočet povrchu objektu kuželu
    def povrch(self):
        # Nejprve (před samotným výpočtem) provede kontrolu platnosti čísla - zdali je vyšší od nuly
        if self.platnost_parametru(self.r) and self.platnost_parametru(self.s):
            return math.pi * self.r * (self.r + self.s)

k1 = Kuzel(5, 8, 2)
k2 = Kuzel(5, 2, 1)

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
print(k1 -k2)

# Výpočet objemu kužele:
print('Objem kužele je: ',round(k1.objem(), 2), 'm')

# Výpočet povrchu kužele:
print('Povrch kužele je: ',round(k1.povrch(), 2), 'm')

# Zavolám metodu třídy Kuzel, která vypíše jednotky používané v této třídě
Kuzel.vypis_jednotek()