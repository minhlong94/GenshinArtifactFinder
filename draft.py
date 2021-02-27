from functools import partial
from hyperopt import fmin, tpe, hp, STATUS_OK, space_eval


class DamageBonus:
    def __init__(self, normal=0, charged=0, burst=0, elemental_geo=0, elemental_cyro=0, elemental_pyro=0,
                 elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0, overall=0, crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0,
                 is_gladiator=False, is_wanderer=False):
        self.normal = normal
        self.charged = charged
        self.burst = burst
        self.elemental_geo = elemental_geo
        self.elemental_pyro = elemental_pyro
        self.elemental_hydro = elemental_hydro
        self.elemental_cyro = elemental_cyro
        self.elemental_anemo = elemental_anemo
        self.elemental_electro = elemental_electro
        self.physical = physical
        self.overall = overall
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.flat_atk = flat_atk
        self.percentage_atk = percentage_atk
        self.is_gladiator = is_gladiator
        self.is_wanderer = is_wanderer

    def get_stats(self):
        return dict(normal=self.normal,
                    charged=self.charged,
                    burst=self.burst,
                    elemental_geo=self.elemental_geo,
                    elemental_pyro=self.elemental_pyro,
                    elemental_cyro=self.elemental_cyro,
                    elemental_anemo=self.elemental_anemo,
                    elemental_hydro=self.elemental_hydro,
                    elemental_electro=self.elemental_electro,
                    physical=self.physical,
                    crit_rate=self.crit_rate,
                    crit_dmg=self.crit_dmg,
                    flat_atk=self.flat_atk,
                    percentage_atk=self.percentage_atk,
                    is_gladiator=self.is_gladiator,
                    is_wanderer=self.is_wanderer)


class BaseArtifact:
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0):
        self.artifact_set = artifact_set
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.flat_atk = flat_atk
        self.percentage_atk = percentage_atk

    def get_stats(self):
        return dict(artifact_set=self.artifact_set,
                    crit_rate=self.crit_rate,
                    crit_dmg=self.crit_dmg,
                    flat_atk=self.flat_atk,
                    percentage_atk=self.percentage_atk)

    def __repr__(self):
        return str(self.get_stats())


class Sand(BaseArtifact):
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0):
        super().__init__(artifact_set, crit_rate, crit_dmg, flat_atk, percentage_atk)


class Circlet(BaseArtifact):
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0):
        super().__init__(artifact_set, crit_rate, crit_dmg, flat_atk, percentage_atk)


class Goblet(BaseArtifact):
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0, elemental_geo=0, elemental_cyro=0, elemental_pyro=0,
                 elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0):
        super().__init__(artifact_set, crit_rate, crit_dmg, flat_atk, percentage_atk)
        self.elemental_geo = elemental_geo
        self.elemental_pyro = elemental_pyro
        self.elemental_hydro = elemental_hydro
        self.elemental_cyro = elemental_cyro
        self.elemental_anemo = elemental_anemo
        self.elemental_electro = elemental_electro
        self.physical = physical

    def get_stats(self):
        return dict(artifact_set=self.artifact_set,
                    crit_rate=self.crit_rate,
                    crit_dmg=self.crit_dmg,
                    flat_atk=self.flat_atk,
                    percentage_atk=self.percentage_atk,
                    elemental_geo=self.elemental_geo,
                    elemental_pyro=self.elemental_pyro,
                    elemental_cyro=self.elemental_cyro,
                    elemental_anemo=self.elemental_anemo,
                    elemental_hydro=self.elemental_hydro,
                    elemental_electro=self.elemental_electro,
                    physical=self.physical)


class Weapon(Goblet):
    def __init__(self, weapon_name="weapon", crit_rate=0, crit_dmg=0, base_atk=0,
                 flat_atk=0, percentage_atk=0, elemental_geo=0, elemental_cyro=0, elemental_pyro=0,
                 elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0):
        self.weapon_name = weapon_name
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.base_atk = base_atk
        self.flat_atk = flat_atk
        self.percentage_atk = percentage_atk
        self.elemental_geo = elemental_geo
        self.elemental_pyro = elemental_pyro
        self.elemental_hydro = elemental_hydro
        self.elemental_cyro = elemental_cyro
        self.elemental_anemo = elemental_anemo
        self.elemental_electro = elemental_electro
        self.physical = physical

    def get_stats(self):
        return dict(weapon_name=self.weapon_name,
                    crit_rate=self.crit_rate,
                    crit_dmg=self.crit_dmg,
                    base_atk=self.base_atk,
                    flat_atk=self.flat_atk,
                    percentage_atk=self.percentage_atk,
                    elemental_geo=self.elemental_geo,
                    elemental_pyro=self.elemental_pyro,
                    elemental_cyro=self.elemental_cyro,
                    elemental_anemo=self.elemental_anemo,
                    elemental_hydro=self.elemental_hydro,
                    elemental_electro=self.elemental_electro,
                    physical=self.physical)


class Flower(BaseArtifact):
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0):
        super().__init__(artifact_set, crit_rate, crit_dmg, flat_atk, percentage_atk)


class Feather(BaseArtifact):
    def __init__(self, artifact_set, crit_rate=0, crit_dmg=0,
                 flat_atk=0, percentage_atk=0):
        super().__init__(artifact_set, crit_rate, crit_dmg, flat_atk, percentage_atk)


ArtifactSets = {
    "Bloodstained Chivary": {2: DamageBonus(physical=25), 4: None},
    "Gladiator's Finale": {2: DamageBonus(percentage_atk=18), 4: DamageBonus(normal=35, is_gladiator=True)},
    "Wanderer's Troupe": {2: None, 4: DamageBonus(charged=35, is_wanderer=True)},
    "Thundering Fury": {2: DamageBonus(elemental_electro=15), 4: None},
    "Viridescent Venerer": {2: DamageBonus(elemental_anemo=15), 4: None},
    "Archaic Petra": {2: DamageBonus(elemental_geo=15), 4: None},
    "Crimson Witch Of Flames": {2: DamageBonus(elemental_pyro=15), 4: DamageBonus(elemental_pyro=22.5)},
    "Noblesse Oblige": {2: DamageBonus(burst=20), 4: DamageBonus(percentage_atk=20)},
    "Blizzard Strayer": {2: DamageBonus(elemental_cyro=15), 4: DamageBonus(crit_rate=20)},
    "Heart Of Depth": {2: DamageBonus(elemental_hydro=15), 4: DamageBonus(normal=30, charged=30)},
    "Retracing Boilde": {2: None, 4: DamageBonus(normal=40, charged=40)},
    "Thunder Soother": {2: None, 4: DamageBonus(overall=35)},
    "Lava Walker": {2: None, 4: DamageBonus(overall=35)}
}

# Xiao


SANDS = [
    Sand("Gladiator's Finale", crit_rate=6.2, flat_atk=29, percentage_atk=46.6),
]

FLOWERS = [
    Flower("Gladiator's Finale", crit_rate=10.5, crit_dmg=7, percentage_atk=9.3),
    Flower("Gladiator's Finale", crit_rate=6.6, crit_dmg=14.8),
    Flower("Viridescent Venerer", crit_dmg=21.8, flat_atk=14)
]

FEATHERS = [
    Feather("Gladiator's Finale", crit_rate=2.7, crit_dmg=21.0, flat_atk=311),
    Feather("Gladiator's Finale", crit_rate=3.1, crit_dmg=14.8, flat_atk=311),
    Feather("Viridescent Venerer", crit_dmg=18.7, flat_atk=311),
]

GOBLETS = [
    Goblet("Viridescent Venerer", crit_rate=7.4, flat_atk=31, percentage_atk=8.7, elemental_anemo=46.6),
    Goblet("Heart Of Depth", crit_dmg=14.8, flat_atk=18, percentage_atk=8.7, elemental_anemo=46.6),
]

CIRCLETS = [
    Circlet("Heart Of Depth", crit_rate=13.2, crit_dmg=62.2, percentage_atk=9.3),
    Circlet("Gladiator's Finale", crit_rate=31.1, percentage_atk=15.7),
    Circlet("Gladiator's Finale", crit_rate=9.3, crit_dmg=62.2, percentage_atk=8.7),
    Circlet("Retracing Boilde", crit_rate=11.3, crit_dmg=62.2, flat_atk=43),
]

WEAPONS = [
    Weapon("Gladiator", base_atk=427, crit_rate=33.5, percentage_atk=16),
    Weapon("Skyward Spine", base_atk=674, crit_rate=8)
]

# Xiao

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


def objective(space, objective_type, dmg_type, can_use_wanderer_4, can_use_gladiator_4, evaluate=False):
    dictionary = dict(crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0, base_atk=0,
                      normal=0, charged=0, burst=0, plunge=0, elemental_geo=0, elemental_cyro=0,
                      elemental_hydro=0, elemental_pyro=0, elemental_anemo=0, elemental_electro=0, physical=0,
                      overall=0,
                      is_gladiator=False, is_wanderer=False)

    artifact_sets = {}
    # Get artifact sets, if any
    for _, value in space.items():
        for stat, number in value.get_stats().items():
            if stat == "artifact_set":
                if number not in artifact_sets:
                    artifact_sets[number] = 1
                else:
                    artifact_sets[number] += 1
            elif stat == "weapon_name":
                pass
            else:
                dictionary[stat] += number

    # Get artifact effects
    for name, cnt in artifact_sets.items():
        if cnt > 1:
            artifact = ArtifactSets.get(name)
            if cnt >= 2:
                dmg_bonus = artifact[2]
                if dmg_bonus is not None:
                    for key, value in dmg_bonus.get_stats().items():
                        dictionary[key] += value
            if cnt >= 4:
                dmg_bonus = artifact[4]
                if dmg_bonus is not None:
                    for key, value in dmg_bonus.get_stats().items():
                        if key == "is_gladiator" and value is True:
                            dictionary[key] = True
                        elif key == "is_wanderer" and value is True:
                            dictionary[key] = True
                        else:
                            dictionary[key] += value

    dictionary["crit_rate"] += ADDITIONAL_CRIT_RATE
    dictionary["crit_dmg"] += ADDITIONAL_CRIT_DMG
    dictionary["flat_atk"] += ADDITIONAL_FLAT_ATK
    dictionary["percentage_atk"] += ADDITIONAL_PERCENTAGE_ATK
    dictionary["normal"] += ADDITIONAL_NORMAL_DMG_BONUS
    dictionary["charged"] += ADDITIONAL_CHARGED_DMG_BONUS
    dictionary["burst"] += ADDITIONAL_BURST_DMG_BONUS
    dictionary["plunge"] += ADDITIONAL_PLUNGE_DMG_BONUS
    if dmg_type != "physical":
        dictionary["elemental_" + dmg_type] += ADDITIONAL_ELEMENTAL_DMG_BONUS
    else:
        dictionary["physical"] += ADDITIONAL_PHYSICAL_DMG_BONUS
    dictionary["overall"] += ADDITIONAL_OVERALL_DMG_BONUS

    if not can_use_wanderer_4 and dictionary["is_wanderer"]:
        dictionary["charged"] -= 35
    if not can_use_gladiator_4 and dictionary["is_gladiator"]:
        dictionary["normal"] -= 35

    ATK = (BASE_ATK + dictionary["base_atk"]) * (1 + dictionary["percentage_atk"] / 100) + dictionary["flat_atk"]

    WITH_CRIT = ATK * SKILL_MUL / 100 * dictionary["crit_rate"] / 100 * (dictionary["crit_dmg"] / 100 + 1)
    WITHOUT_CRIT = ATK * SKILL_MUL / 100 * (1 - dictionary["crit_rate"] / 100)

    DMG_TYPE_DICT = {}
    for x in ["geo", "anemo", "hydro", "pyro", "cyro", "physical"]:
        DMG_TYPE_DICT[x] = dict(normal=0, charged=0, burst=0)
    for dmg_type in ["geo", "anemo", "hydro", "pyro", "cyro", "physical"]:
        for atk_type in ["normal", "charged", "plunge", "burst"]:
            AVERAGE_DMG = (WITH_CRIT + WITHOUT_CRIT) * (dictionary[objective_type] / 100 + 1)
            DMG_TYPE_DICT[dmg_type][atk_type] = AVERAGE_DMG

    if evaluate:
        print(f"ATK: {ATK}")
        print(f"STATS: {dictionary}\n")
        print(f"ARTIFACT SETS: {artifact_sets}")
        print(f"AVERAGE DMG: {DMG_TYPE_DICT[dmg_type][objective_type]}")
        return None

    return {"loss": -DMG_TYPE_DICT[dmg_type][objective_type], "status": STATUS_OK}


space = {
    "Sand": hp.choice("Sands", SANDS),
    "Flower": hp.choice("Flowers", FLOWERS),
    "Feather": hp.choice("Feathers", FEATHERS),
    "Goblet": hp.choice("Goblets", GOBLETS),
    "Circlet": hp.choice("Circlets", CIRCLETS),
    "Weapon": hp.choice("Weapons", WEAPONS)
}

fn = partial(objective, objective_type=OBJECTIVE_TYPE, dmg_type=DMG_TYPE, can_use_wanderer_4=CAN_USE_WANDERER_4,
             can_use_gladiator_4=CAN_USE_GLADIATOR_4, evaluate=False)
best_params = fmin(fn=fn, space=space, algo=tpe.suggest, max_evals=MAX_EVALS)

objective(space_eval(space, best_params), OBJECTIVE_TYPE, DMG_TYPE,
          CAN_USE_WANDERER_4, CAN_USE_GLADIATOR_4, evaluate=True)
print("ARTIFACT DETAILS: ")
for i in space_eval(space, best_params).items():
    print(i)