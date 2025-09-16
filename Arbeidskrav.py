# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:24:57 2025

@author: Johanna
"""
km_per_år = 10000 # antall kilometer per år

# Faste kostnader
forsikring_elbil = 5000
forsikring_bensinbil = 7500
trafikkforsikringsavgift_per_år = 3059

# Variable kostnader
strømpris = 0.2  # kr/kWh
strømforbruk = 2.00 # kWh/km
bensinpris = 1.0 # kr/km
bom_elbil= 0.1 # kr/km
bom_bensinbil = 0.3 # kr/km

# Totalkostnader
kostnader_elbil = (km_per_år*strømpris*strømforbruk*bom_elbil) + forsikring_elbil + trafikkforsikringsavgift_per_år
kostnader_bensinbil = (km_per_år*bensinpris*bom_bensinbil) + forsikring_bensinbil + trafikkforsikringsavgift_per_år

# Kostnadsdifferanse
differanse = kostnader_bensinbil - kostnader_elbil

# Beregninger
print("Årlige totalkostnader:")
print(f"elbil: {kostnader_elbil:.2f} kr")
print(f"bensinbil: {kostnader_bensinbil:.2f} kr")
print(f"kostnadsdifferanse: {differanse:.2f} kr")

