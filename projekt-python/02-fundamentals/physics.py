'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
RYCHLOST_SVETLA_SKLO = 200000 #? rychlost světla ve skle
''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def vypocet_grav_sily_zeme(hmotnost):
    """
    Tato funkce na vypočítá gravitační sílu
    vzhledem k tělesu o nějaké hmotnosti v g
    """
    return print(hmotnost * EARTH_GRAVITY, "N")


def vypocet_grav_sily_mesice(hmotnost):
    """
    Vypočítá gravitační sílu tělesa o nějaké hmotnosti
    na měsíci. Například Neil Armstrong váží dejme tomu
    80 kg, tak jakou gravitační sílou je přitahován jako
    první člověk na měsíci? :)
    """
    return print(round(hmotnost * MOON_GRAVITY, 2), "N")


def index_lomu_skla(rychlost):
    """
    Funkce vypočítá index lomu skla
    dle vzorce RYCHLOST SVĚTLA VE VZDUCHU/RYCHLOST SVĚTLA VE SKLE
    """
    n = SPEED_OF_LIGHT // rychlost
    return print("%.2f" % round(n, 2))


def vzdalenost_ozvena(cas):
    """
    Tato funkce demonstruje výpočet vzdálenosti
    nějakého objektu v závislosti na čase odezvy ozvěny.
    Například stojím na vrcholu skály a volám a "stopnu" čas ozvěny.
    Poté dosadím do mé funkce a mám vypočítáno :).
    """
    s = SPEED_OF_SOUND * cas
    return print("%.2f" % round(s, 2), "m")
