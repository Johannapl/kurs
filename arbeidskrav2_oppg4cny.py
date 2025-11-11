# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 01:27:23 2025

@author: Johanna

"""

data = {
        "Norge":  ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris",2.161],
        "Italia": ["Roma", 2.873]
        }
# Tar inn et land fra brukeren. #
land = input('Skriv inn et nytt land:')
# Tar inn hovedstad fra brukeren. #
hovedstad = input(f"Skriv inn hovedstaden i {land}:")
# Tar inn antall innbyggere fra brukeren. #
innbyggere = float(input(f"Skriv inn antall innbyggere i {hovedstad} i millioner:"))
data[land] = [hovedstad, innbyggere]
# Skriver ut oppdatert dictionary. #
print("Oppdatert dictionary:")
for land, info in data.items():
    hovedstad, innbyggere = info
print(data)




