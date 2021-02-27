class BaseArtifact:
    def __init__(self, name, normal=0, charged=0, plunged=0, burst=0, elemental_geo=0, elemental_cyro=0,
                 elemental_pyro=0, elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0, overall=0, crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0):
        self.name = name
        self.normal = normal
        self.charged = charged
        self.plunged = plunged
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

    def get_stats(self):
        return dict(type=self.__class__.__name__,
                    name=self.name,
                    normal=self.normal,
                    charged=self.charged,
                    burst=self.burst,
                    plunged=self.plunged,
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
                    percentage_atk=self.percentage_atk)

    def __repr__(self):
        return str(self.get_stats())


class Sand(BaseArtifact):
    pass


class Circlet(BaseArtifact):
    pass


class Goblet(BaseArtifact):
    pass


class Flower(BaseArtifact):
    pass


class Feather(BaseArtifact):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flat_atk = 311


class Weapon:
    def __init__(self, name="weapon", normal=0, charged=0, plunged=0, burst=0, elemental_geo=0, elemental_cyro=0,
                 elemental_pyro=0,
                 elemental_hydro=0, elemental_anemo=0, elemental_electro=0,
                 physical=0, overall=0, crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0):
        self.name = name
        self.normal = normal
        self.charged = charged
        self.plunged = plunged
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

    def get_stats(self):
        return dict(name=self.name,
                    normal=self.normal,
                    charged=self.charged,
                    burst=self.burst,
                    plunged=self.plunged,
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
                    percentage_atk=self.percentage_atk)
