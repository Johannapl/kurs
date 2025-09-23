# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:24:57 2025

@author: Johanna

"""
km_per_år = 10000 # antall kilometer per år

# Faste kostnader per år
forsikring_elbil = 5000
forsikring_bensinbil = 7500
trafikkforsikringsavgift = 3059

# Variable kostnader
strømpris = 2.00  # kr/kWh
strømforbruk = 0.2 # kWh/km
bensinpris = 1.0 # kr/km
bom_elbil= 0.1 # kr/km
bom_bensinbil = 0.3 # kr/km

# Totalkostnader per år
kostnader_elbil = (km_per_år*strømpris*strømforbruk*bom_elbil) + forsikring_elbil + trafikkforsikringsavgift
kostnader_bensinbil = (km_per_år*bensinpris*bom_bensinbil) + forsikring_bensinbil + trafikkforsikringsavgift

# Årlig kostnadsdifferanse
kostnadsdifferanse = kostnader_bensinbil - kostnader_elbil

# Beregninger
print("Årlige totalkostnader:")
print(f"elbil: {kostnader_elbil:} kr")
print(f"bensinbil: {kostnader_bensinbil:} kr")
print(f"kostnadsdifferanse: {kostnadsdifferanse:} kr")

