# RankValorant.py
from enum import Enum
import math

__all__ = ['Rank_Method_One_Valorant', 'Rank_Method_Two_Valorant', 'Rank_Method_Three_Valorant']

# Ranking Method 1 VALORANT
class Rank_Method_One_Valorant(Enum):
    U = -math.inf
    I3 = 50
    I2 = 100
    I1 = 150
    B3 = 300
    B2 = 400
    B1 = 500
    S3 = 700
    S2 = 800
    S1 = 900
    G3 = 1150
    G2 = 1300
    G1 = 1450
    P3 = 1600
    P2 = 1750
    P1 = 1900
    D3 = 2050
    D2 = 2200
    D1 = 2350
    A3 = 2500
    A2 = 2650
    A1 = 2800
    Im3 = 2950
    Im2 = 3100
    Im1 = 3250
    R = 3400

# Ranking Method 2 VALORANT
class Rank_Method_Two_Valorant(Enum):
    U = -math.inf
    I3 = 100
    I2 = 200
    I1 = 350
    B3 = 550
    B2 = 750
    B1 = 950
    S3 = 1200
    S2 = 1450
    S1 = 1700
    G3 = 1950
    G2 = 2200
    G1 = 2450
    P3 = 2700
    P2 = 2950
    P1 = 3200
    D3 = 3450
    D2 = 3700
    D1 = 3950
    A3 = 4200
    A2 = 4450
    A1 = 4700
    Im3 = 4950
    Im2 = 5200
    Im1 = 5450
    R = 5700

# Ranking Method 3 VALORANT
class Rank_Method_Three_Valorant(Enum):
    U = 0
    I3 = 100
    I2 = 200
    I1 = 300
    B3 = 400
    B2 = 500
    B1 = 600
    S3 = 700
    S2 = 800
    S1 = 900
    G3 = 1000
    G2 = 1100
    G1 = 1200
    P3 = 1300
    P2 = 1400
    P1 = 1500
    D3 = 1600
    D2 = 1700
    D1 = 1800
    A3 = 1900
    A2 = 2000
    A1 = 2100
    Im3 = 2200
    Im2 = 2300
    Im1 = 2400
    R = 2500