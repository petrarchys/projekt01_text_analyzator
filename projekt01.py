"""
projekt_1.py: první projekt do Engeto Online Datový analytik s Pythonem
author: Petr Ssychra
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

cara = "-" * 33
mozne_volby = [1,2,3] 

uzivatel = input("username:")
heslo = input("password:")

# ověření uživatele
if uzivatel in uzivatele.keys() and heslo == uzivatele.get(uzivatel):
    print(cara)
    print(f"Vítejte v aplikaci, {uzivatel}")
else:
    print("neregistrovaný uživatel, ukončení programu..")
    sys.exit()

print("Máme 3 texty k analýze.", cara, sep="\n")

cislo_textu = input("Zadejte číslo mezi 1 a 3 pro výběr:")

# ověření volby
if not cislo_textu.isdigit():
    print("Chybná volba :-(. Končím..")
    sys.exit()
elif int(cislo_textu) not in mozne_volby:
    print("Chybná volba :-(. Končím")
    sys.exit()
else: 
    print("Tady bude statistika")