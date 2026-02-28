import EchoBase as eb
import random

def buildOneCostEcho(name: str, set : str):
    main_stats = {
        "ATK%": 3.6,
        "HP%": 4.5,
        "DEF%": 3.6,
        
    }
    main_stat = random.choice(list(main_stats.keys()))
    flat_hp = 456
    return eb.EchoBase(name, set, 1, main_stat, main_stats[main_stat], "HP", flat_hp, [])

def buildThreeCostEcho(name: str, set : str):
    main_stats = {
        "ATK%": 6.0,
        "HP%": 6.0,
        "DEF%": 7.6,
        "GlacioDmgBonus%": 6.0,
        "FusionDmgBonus%": 6.0,
        "ElectroDmgBonus%": 6.0,
        "AeroDmgBonus%": 6.0,
        "SpectroDmgBonus%": 6.0,
        "HavocDmgBonus%": 6.0,
        "EnergyRegen%": 6.4,
        
    }
    main_stat = random.choice(list(main_stats.keys()))
    flat_atk = 20
    return eb.EchoBase(name, set, 3, main_stat, main_stats[main_stat], "ATK", flat_atk, [])

echo = buildOneCostEcho("Test Echo", "Test Set")
print(echo.__dict__)
echo = buildThreeCostEcho("Test Echo", "Test Set")
print(echo.__dict__)