# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 22:32:12 2025
@author: Johanna

"""

data = {
        "Norge":  ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris",2.161],
        "Italia": ["Roma", 2.873]
        }
# Tar inn et land fra brukeren. #
land = input('Skriv inn et land:')
if land in data:
    hovedstad, innbyggere = data[land]
# Skriver ut hovedstaden og antall innbyggere i angitt land. #
print(f"{hovedstad} er hovedstad i {land} og det er {innbyggere} innbyggere i {hovedstad}.")






      

