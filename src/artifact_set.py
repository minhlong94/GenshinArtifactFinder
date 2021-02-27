class DamageBonus:
    def __init__(self, normal=0, charged=0, plunged=0, burst=0, elemental_geo=0, elemental_cryo=0, elemental_pyro=0,
                 elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0, overall=0, crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0,
                 is_gladiator=False, is_wanderer=False):
        self.normal = normal
        self.charged = charged
        self.plunged = plunged
        self.burst = burst
        self.elemental_geo = elemental_geo
        self.elemental_pyro = elemental_pyro
        self.elemental_hydro = elemental_hydro
        self.elemental_cryo = elemental_cryo
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
                    plunged=self.plunged,
                    elemental_geo=self.elemental_geo,
                    elemental_pyro=self.elemental_pyro,
                    elemental_cryo=self.elemental_cryo,
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


ARTIFACT_SET_DETAILS = {
    "Bloodstained Chivary": {2: DamageBonus(physical=25), 4: None},
    "Gladiator's Finale": {2: DamageBonus(percentage_atk=18), 4: DamageBonus(normal=35, is_gladiator=True)},
    "Wanderer's Troupe": {2: None, 4: DamageBonus(charged=35, is_wanderer=True)},
    "Thundering Fury": {2: DamageBonus(elemental_electro=15), 4: None},
    "Viridescent Venerer": {2: DamageBonus(elemental_anemo=15), 4: None},
    "Archaic Petra": {2: DamageBonus(elemental_geo=15), 4: None},
    "Crimson Witch Of Flames": {2: DamageBonus(elemental_pyro=15), 4: DamageBonus(elemental_pyro=22.5)},
    "Noblesse Oblige": {2: DamageBonus(burst=20), 4: DamageBonus(percentage_atk=20)},
    "Blizzard Strayer": {2: DamageBonus(elemental_cryo=15), 4: DamageBonus(crit_rate=20)},
    "Heart Of Depth": {2: DamageBonus(elemental_hydro=15), 4: DamageBonus(normal=30, charged=30)},
    "Retracing Boilde": {2: None, 4: DamageBonus(normal=40, charged=40)},
    "Thunder Soother": {2: None, 4: DamageBonus(overall=35)},
    "Lava Walker": {2: None, 4: DamageBonus(overall=35)}
}

ARTIFACT_PIECE_NAME = [
    "Sand",
    "Feather",
    "Circlet",
    "Flower",
    "Goblet"
]

ARTIFACT_STATS = [
    "normal", "charged", "plunged", "burst", "elemental_geo", "elemental_cryo", "elemental_pyro", "elemental_hydro",
    "elemental_anemo", "elemental_electro", "physical", "overall", "crit_rate", "crit_dmg", "flat_atk", "percentage_atk"
]
