WELCOME = """
## Author: AerysS#5558

**Last update: 27/02/2021**

I make a simple best artifact finder using naive DMG calculation by this formula:

`AVERAGE_DMG = ATK * SKILL_MUL * CritRate * (1 + CritDMG) * (1 + DMGBonus) + ATK * SKILL_MUL * (1 - CritRate) * (1+ DMGBonus)`

where:

- `ATK`: Character's ATK (Base ATK + Additional ATK)

- `SKILL_MUL`: skill damage multiplier

- `DMGBonus`: Damage bonus from ascension and/or sets. Calculates Normal, Charged and Burst separately depends on your objective.

I use `hyperopt` to find the optimized result. However, if there are very few artifact combinations, it is the same as doing a Grid Search.

Limits:
- Only works with ATK-based characters
- Does not check if the value range is right
- Does not check character's dmg type. For example, if you find it for Ganyu, assume that we only care about the cryo dmg output, so DO NOT PUT PHYSICAL GOBLET HERE PLEASE!
- Does not consider Elemental Mastery
- Does not consider resistance reduction
- Does not consider some (useless/underwhelming/hard to do) stats:
    - Elemental reaction dmg (of every type)
    - Bloodstained Chivary 4 set
    - Viridescent Venerer 4 set
    - HP-based character (Zhongli, Hu Tao, etc)
    - Icebreaker 4 set additional 20% crit rate to frozen enemies. However this is customizable.
"""

CONST_DECLARE = """
## Constants declaration
Declare additional numbers here:
- `BASE_ATK`: Character's base ATK
- `ADDITIONAL_CRIT_RATE`: base crit rate + additional crit rate (from resonance, talent, etc)
- `ADDITIONAL_CRIT_DMG`: base crit dmg + ascension crit dmg
- `ADDITIONAL_FLAT_ATK`: additional Flat ATK from other sources (Bennet's ultimate)
- `ADDITIONAL_PERCENTAGE_ATK`: additional ATK from other sources (Pyro's resonance)
- `SKILL_MUL`: skill dmg multiplier that we want to evaluate
- `ADDITIONAL_X_DMG_BONUS`: additional X dmg type bonus from other sources (resonance, etc.)
- `CAN_USE_WANDERER_4`: boolean, `True` if character can use Wanderer 4 set effect (Charged atk for Catalyst/Bow user), else `False`
- `CAN_USE_GLADIATOR_4`: boolean, `True` if character can use Gladiator 4 set effect (Normal atk for GS, Spear, Sword user), else `False`
- `OBJECTIVE_TYPE`: string, one in `["normal", "charged", "plunge", "burst"]`
- `DMG_TYPE`: string, one in `["geo", "anemo", "electro", "hydro", "cryo", "pyro", "physical"]`
- `MAX_EVALS`: number of iterations to find. The higher the better, but remember if there are few artifact combinations, raising this one will not help.

A template for Xiao is provided below, lv80 with Ascension 6:
```Python
BASE_ATK = 284
ADDITIONAL_CRIT_RATE = 19.4
ADDITIONAL_CRIT_DMG = 50
ADDITIONAL_FLAT_ATK = 0
ADDITIONAL_PERCENTAGE_ATK = 0
SKILL_MUL = 349 + 77
ADDITIONAL_NORMAL_DMG_BONUS = 0
ADDITIONAL_CHARGED_DMG_BONUS = 0
ADDITIONAL_BURST_DMG_BONUS = 0
ADDITIONAL_PLUNGE_DMG_BONUS = 0
ADDITIONAL_ELEMENTAL_DMG_BONUS = 0
ADDITIONAL_PHYSICAL_DMG_BONUS = 0
ADDITIONAL_OVERALL_DMG_BONUS = 0
CAN_USE_WANDERER_4 = False
CAN_USE_GLADIATOR_4 = True
OBJECTIVE_TYPE = "plunge"
DMG_TYPE = "anemo"
MAX_EVALS = 500
```
"""
