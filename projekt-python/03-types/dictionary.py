'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# Kolekce, která je neuspořádaná, měnitelná a indexována.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# V Pythonu jsou slovníky psány s vlnitými závorkami a mají klíče a hodnoty.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota a případné vypsání její hodnoty
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
automobilky = {
  'skoda_auto': {
    'sidlo' : 'Mladá Boleslav, Česká republika',
    'datum_zalozeni' : '1895',
    'koncern' : True,
    'zakladatele' : {"Václav Laurin", "Václav Klement"},
    'dcerinne_spolecnosti' : ['Škoda Auto India Private', 'Limited', 'Škoda Auto DigiLab', 'Smart City Lab'],
    'zamestnanci' : 33696
  },
    'volkswagen' : {
      'sidlo' : 'Wolfsburg, Německo',
      'datum_zalozeni' : '1937',
      'koncern' : True,
      'zakladatele' : {"státní firma"},
      'dcerinne_spolecnosti' : ['Audi AG', 'Škoda-auto a. s.', 'SEAT', 'Bentley', 'Lamborghini'],
      'zamestnanci' : 304174
    },
    'ford' : {
      'sidlo' : 'Dearborn, Michigan, USA',
      'datum_zalozeni' : '1903',
      'koncern' : True,
      'zakladatele' : {"Henry Ford"},
      'dcerinne_spolecnosti' : ['Otosan', 'Ford Air Transport Service', 'Ford Global Technologies', 'Mercury'],
      'zamestnanci' : 159000
    }
}
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
del automobilky['ford']
automobilky['seat'] = {
      'sidlo' : 'Municipality of Martorell, Španělsko',
      'datum_zalozeni' : '1950',
      'koncern' : False,
      'zakladatele' : {"Instituto Nacional de Industria"},
      'dcerinne_spolecnosti' : ['LISEAT', 'FISEAT', 'SEAT Sport'],
      'zamestnanci' : 159000
}
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
print("automobilky")
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
print('název automobilky                  sídlo                                                                    rok založení                                                            součást koncernu                                                                         zakladatelé                                                                     dceřinné společnosti                                                            počet zaměstnanců\n')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
for i, j in automobilky.items():
  print(f'{i}'.ljust(30), end="")
  for k,b in j.items():
    if len(str(b)) > 20:
      print(f"{b}".ljust(80), end="")
    else:
      print(f"{b}".ljust(80), end="")
  print('\n')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''