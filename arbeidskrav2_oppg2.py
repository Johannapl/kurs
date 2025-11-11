# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:24:57 2025

@author: Johanna

"""
import math
# Tar inn antall elever fra brukeren. #
antall_elever = int(input("Skriv inn antall elever:"))
antall_pizzaer = antall_elever * 0.25
pizzaer = math.ceil(antall_pizzaer)
# Skriver ut antall pizaer som et heltall. #
print(f"Det må handles inn {pizzaer} pizzaer til festen")

 