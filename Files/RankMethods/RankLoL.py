# RankLoL.py
from enum import Enum
import math

__all__ = ['Rank_Method_One_LoL', 'Rank_Method_Two_LoL', 'Rank_Method_Three_LoL']

# Ranking Method 1 LoL
class Rank_Method_One_LoL(Enum):
    U = -math.inf
    I4 = 50
    I3 = 100
    I2 = 150
    I1 = 200
    B4 = 300
    B3 = 400
    B2 = 500
    B1 = 600
    S4 = 700
    S3 = 800
    S2 = 900
    S1 = 1000
    G4 = 1150
    G3 = 1300
    G2 = 1450
    G1 = 1600
    P4 = 1800
    P3 = 2000
    P2 = 2200
    P1 = 2400
    E4 = 2700
    E3 = 3000
    E2 = 3300
    E1 = 3600
    D4 = 4000
    D3 = 4400
    D2 = 4900
    D1 = 5400
    M = 6000
    GR = 7000
    C = 8500

# Ranking method 2 LoL
class Rank_Method_Two_LoL(Enum):
    U = -math.inf
    I4 = 100
    I3 = 200
    I2 = 300
    I1 = 450
    B4 = 650
    B3 = 850
    B2 = 1100
    B1 = 1400
    S4 = 1750
    S3 = 2100
    S2 = 2450
    S1 = 2800
    G4 = 3150
    G3 = 3500
    G2 = 3850
    G1 = 4200
    P4 = 4550
    P3 = 4900
    P2 = 5250
    P1 = 5600
    E4 = 5950
    E3 = 6300
    E2 = 6650
    E1 = 7000
    D4 = 7350
    D3 = 7700
    D2 = 8050
    D1 = 8400
    M = 8750
    GR = 9100
    C = 9450

# Ranking Method 3 LoL
class Rank_Method_Three_LoL(Enum):
    U = 0
    I4 = 100
    I3 = 200
    I2 = 300
    I1 = 400
    B4 = 500
    B3 = 600
    B2 = 700
    B1 = 800
    S4 = 900
    S3 = 1000
    S2 = 1100
    S1 = 1200
    G4 = 1300
    G3 = 1400
    G2 = 1500
    G1 = 1600
    P4 = 1700
    P3 = 1800
    P2 = 1900
    P1 = 2000
    E4 = 2100
    E3 = 2200
    E2 = 2300
    E1 = 2400
    D4 = 2500
    D3 = 2600
    D2 = 2700
    D1 = 2900
    M = 3000
    GR = 3100
    C = 3200
