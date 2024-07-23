"""
projekt_1.py: první projekt do Engeto Online Datový analytik s Pythonem

author: Petr Sychra
email: psychra@seznam.cz
discord: petrsychra
"""

import sys

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

cara = "-" * 40
mozne_volby = [1,2,3]
statistika = dict(
    pocet_slov = 0,
    zacinajici_velkym = 0,
    slova_velkym = 0,
    slova_malym = 0,
    pocet_cisel = 0,
    soucet_cisel = 0
)

delky_vsech_slov = []

uzivatel = input("username:")
heslo = input("password:")

# ověření uživatele
if uzivatel in uzivatele.keys() and heslo == uzivatele.get(uzivatel):
    print(cara)
    print(f"Welcome to the app, {uzivatel}")
else:
    print("unregistered user, terminating the program..")
    sys.exit()

print("We have 3 texts to be analyzed.", cara, sep="\n")

cislo_textu = input("Enter a number btw. 1 and 3 to select:")

# ověření volby
if not cislo_textu.isdigit() or int(cislo_textu) not in mozne_volby:
    print("bad choice, terminating the program..")
    sys.exit()

text_k_nalyze = TEXTS[int(cislo_textu) - 1].strip()

# vyplnení statistických údajů 
for slovo in text_k_nalyze.split():
    delky_vsech_slov.append(len(slovo))
    statistika["pocet_slov"] += 1

    if slovo.istitle():
        statistika["zacinajici_velkym"] += 1
    elif slovo.isupper():
        statistika["slova_velkym"] += 1
    elif slovo.islower():
        statistika["slova_malym"] += 1
    elif slovo.isdigit():
        statistika["pocet_cisel"] += 1
        statistika["soucet_cisel"] += int(slovo)
    
print(f"""{cara}
There are {statistika["pocet_slov"]} words in the selected text. 
There are {statistika["zacinajici_velkym"]} titlecase words. 
There are {statistika["slova_velkym"]} uppercase words.
There are {statistika["slova_malym"]} lowercase words.
There are {statistika["pocet_cisel"]} numeric strings.
The sum of all the numbers {statistika["soucet_cisel"]}.
{cara}"""
)

delky_vsech_slov.sort()
delky_slov = set(delky_vsech_slov)  # získání jedinečných délek

# výpis grafu
hlavicka_grafu = "{:<3} | {:<18} | {:<3}"
print(hlavicka_grafu.format("LEN", "OCCURENCES", "NR."))
print(cara)

for delka in delky_slov:
    pocet = delky_vsech_slov.count(delka)
    cetnost_graf = "*" * pocet
    print(f"{delka:>3} | {cetnost_graf:<18} | {pocet:<3}")
else:
    print(cara)
