# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 21:15:24 2025

@author: Johanna

"""

import math
# Tar inn verdier frabrukeren. "
a = float(input(f"Skriv inn verdien av a:"))
b = float(input(f"Skriv inn verdien av b:"))
    # Areal retvinklet trekant: (g * h) / 2, der g = b og h = a #
areal_trekant = (a * b)/ 2
radius = a /2
    # Areal sirkel = pi * r^2, der r = a #
areal_halvsirkel = 0.5 * math.pi * radius ** 2
total_areal = areal_trekant + areal_halvsirkel
    
omkrets_halvsirkel = (2 * math.pi * radius) / 2
c = math.sqrt(a ** 2 + b ** 2)
omkrets = b + c + omkrets_halvsirkel
  # Skriver ut arealet og ytre omkrets. "  
print(f"Arealet av figuren er {total_areal:.2f}")
print(f"Ytre omkrets av figuren er {omkrets:.2f}")
    
    
    
    
    
    

