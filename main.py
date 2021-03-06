import pandas as pd
import streamlit as st
from src.artifact import *
from src.string_data import *
from src import SessionState
from src.artifact_set import ARTIFACT_SET_DETAILS, ARTIFACT_PIECE_NAME, ARTIFACT_STATS
from functools import partial
from hyperopt import fmin, tpe, hp, STATUS_OK, space_eval

st.set_page_config(layout="wide")
state = SessionState.get(id=99999, df=pd.DataFrame(columns=["type", "name"] + list(ARTIFACT_STATS) + ["base_atk"]),
                         SANDS=[], GOBLETS=[], CIRCLETS=[], WEAPONS=[], FEATHERS=[], FLOWERS=[])
st.title("GENSHIN IMPACT BEST ARTIFACT FINDER")
with st.beta_expander("INTRODUCTION (click here to collapse)", expanded=True):
    st.markdown(WELCOME)

with st.beta_expander("ARTIFACT TABLE (click here to collapse)", expanded=True):
    state.holder = st.empty()
    state.holder.dataframe(state.df)
    state.export_table = st.button("Export table to csv")
    if state.export_table:
        def get_table_download_link(df):
            import base64
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            return f'<a href="data:file/csv;base64,{b64}" download="artifact.csv">Click here to download csv file</a>'


        st.markdown(get_table_download_link(state.df), unsafe_allow_html=True)

with st.sidebar:
    st.title("Use this sidebar to input artifacts/weapons.")
    st.info("Note: you also have to input main stats, (i.e."
            "Base ATK of weapon, Flat ATK of feather, ATK% of Sands, etc.)\n\n"
            "You also have to input every type to have at least 1 piece, else it will throw an error.")
    state.gear_piece = st.selectbox("Artifact/Weapon piece: ", ARTIFACT_PIECE_NAME + ["Weapon"])
    if state.gear_piece == "Weapon":
        state.gear_name = st.text_input("Weapon name: ")
    else:
        state.gear_name = st.selectbox("Artifact name: ", list(ARTIFACT_SET_DETAILS.keys()))
    state.gear = eval(state.gear_piece)(name=state.gear_name)
    if state.gear_piece == "Weapon":
        state.geat_stats = st.multiselect("Substats: ", ARTIFACT_STATS + ["base_atk"])
    else:
        state.geat_stats = st.multiselect("Substats: ", ARTIFACT_STATS)
    for stat in state.geat_stats:
        var = st.number_input(f"{stat}: ")
        setattr(state.gear, stat, var)
    state.confirm_add_gear = st.button("Add gear")
    with st.beta_expander("Click here to run!", expanded=True):
        state.find_artifact = st.button("Find artifact!")

    if state.confirm_add_gear:
        if state.gear_piece == "Weapon":
            state.WEAPONS.append(state.gear)
        elif state.gear_piece == "Sand":
            state.SANDS.append(state.gear)
        elif state.gear_piece == "Feather":
            state.FEATHERS.append(state.gear)
        elif state.gear_piece == "Flower":
            state.FLOWERS.append(state.gear)
        elif state.gear_piece == "Circlet":
            state.CIRCLETS.append(state.gear)
        elif state.gear_piece == "Goblet":
            state.GOBLETS.append(state.gear)
        state.df = state.df.append(state.gear.get_stats(), ignore_index=True)
        state.holder.dataframe(state.df)

    with st.beta_expander("Click here to remove a row"):
        st.info("Use this below part to remove a row from the table, based on index")
        state.index_to_remove = st.selectbox("Index to remove:", state.df.index)
        state.confirm_remove = st.button("Remove")
        if state.confirm_remove:
            state.df = state.df.drop([state.index_to_remove]).reset_index(drop=True)
            state.holder.dataframe(state.df)

    with st.beta_expander("Click here to reset the table"):
        st.info("Use the Reset button to reset the table")
        state.confirm_reset_df = st.button("Reset table")
        if state.confirm_reset_df:
            state.df = pd.DataFrame(columns=["type", "name"] + list(ARTIFACT_STATS))
            state.holder.dataframe(state.df)
    with st.beta_expander("Project information"):
        st.markdown(
            """This project is open sourced at: [GitHub](https://github.com/minhlong94/GenshinArtifactFinder)""")

with st.beta_expander("VARIABLE DECLARATIONS (click here to collapse)", expanded=True):
    st.markdown(CONST_DECLARE)
    state.BASE_ATK = st.number_input("Base ATK: ", value=284)
    state.ADDITIONAL_CRIT_RATE = st.number_input("Additional crit rate: ", value=19.4)
    state.ADDITIONAL_CRIT_DMG = st.number_input("Additional crit damage: ", value=50)
    state.ADDITIONAL_FLAT_ATK = st.number_input("Additional flat attack: ", value=0)
    state.ADDITIONAL_PERCENTAGE_ATK = st.number_input("Additional percentage attack bonus: ", value=0)
    state.SKILL_MUL = st.number_input("Skill damage multiplier: ", value=349 + 77)
    state.ADDITIONAL_NORMAL_DMG_BONUS = st.number_input("Additional normal attack damage: ", value=0)
    state.ADDITIONAL_CHARGED_DMG_BONUS = st.number_input("Additional charged attack damage bonus: ", value=0)
    state.ADDITIONAL_BURST_DMG_BONUS = st.number_input("Additional burst attack damage bonus: ", value=0)
    state.ADDITIONAL_PLUNGED_DMG_BONUS = st.number_input("Additional plunged attack damage bonus: ", value=0)
    state.ADDITIONAL_ELEMENTAL_DMG_BONUS = st.number_input("Additional elemental damage bonus: ", value=0)
    state.ADDITIONAL_PHYSICAL_DMG_BONUS = st.number_input("Additional physical damage bonus: ", value=0)
    state.ADDITIONAL_OVERALL_DMG_BONUS = st.number_input("Additional overall damage bonus: ", value=0)
    state.CAN_USE_WANDERER_4 = st.selectbox("Can use Wanderer 4 set? ", [False, True], 0)
    state.CAN_USE_GLADIATOR_4 = st.selectbox("Can use Gladiator 4 set? ", [False, True], 0)
    state.DAMAGE_TYPE_1 = st.selectbox("Damage type 1: ", ["normal", "charged", "plunged", "burst"], 2)
    state.DAMAGE_TYPE_2 = st.selectbox("Damage type 2: ",
                                       ["geo", "anemo", "electro", "hydro", "cryo", "pyro", "physical"],
                                       1)
    state.MAX_EVALS = st.number_input("Max evals: ", value=500)

    if state.variable_dict is None:
        variable_dict = {
            "BASE_ATK": state.BASE_ATK,
            "ADDITIONAL_CRIT_RATE": state.ADDITIONAL_CRIT_RATE,
            "ADDITIONAL_CRIT_DMG": state.ADDITIONAL_CRIT_DMG,
            "ADDITIONAL_FLAT_ATK": state.ADDITIONAL_FLAT_ATK,
            "ADDITIONAL_PERCENTAGE_ATK": state.ADDITIONAL_PERCENTAGE_ATK,
            "SKILL_MUL": state.SKILL_MUL,
            "ADDITIONAL_NORMAL_DMG_BONUS": state.ADDITIONAL_NORMAL_DMG_BONUS,
            "ADDITIONAL_CHARGED_DMG_BONUS": state.ADDITIONAL_CHARGED_DMG_BONUS,
            "ADDITIONAL_BURST_DMG_BONUS": state.ADDITIONAL_BURST_DMG_BONUS,
            "ADDITIONAL_PLUNGED_DMG_BONUS": state.ADDITIONAL_PLUNGED_DMG_BONUS,
            "ADDITIONAL_ELEMENTAL_DMG_BONUS": state.ADDITIONAL_ELEMENTAL_DMG_BONUS,
            "ADDITIONAL_PHYSICAL_DMG_BONUS": state.ADDITIONAL_PHYSICAL_DMG_BONUS,
            "ADDITIONAL_OVERALL_DMG_BONUS": state.ADDITIONAL_OVERALL_DMG_BONUS,
            "CAN_USE_WANDERER_4": state.CAN_USE_WANDERER_4,
            "CAN_USE_GLADIATOR_4": state.CAN_USE_GLADIATOR_4,
            "OBJECTIVE_TYPE": state.DAMAGE_TYPE_1,
            "DMG_TYPE": state.DAMAGE_TYPE_2,
            "MAX_EVALS": state.MAX_EVALS
        }
        state.variable_dict = variable_dict


    def get_variable_as_pickle(pickle_file):
        import base64
        import pickle
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        file = pickle.dumps(pickle_file)
        b64 = base64.b64encode(file).decode()  # some strings <-> bytes conversions necessary here
        return f'<a href="data:file/pickle;base64,{b64}" download="variable.pickle">Click here to download pickle ' \
               f'file</a> '


    state.download_variable_as_pickle = st.button("Download variable as pickle")
    if state.download_variable_as_pickle:
        st.markdown(get_variable_as_pickle(variable_dict), unsafe_allow_html=True)
    st.write("When you finish, click the \"Find Artifact\" button in the sidebar!")


def objective_function(space, state_obj, objective_type, dmg_type, can_use_wanderer_4, can_use_gladiator_4,
                       evaluate=False):
    dictionary = dict(crit_rate=0, crit_dmg=0, flat_atk=0, percentage_atk=0, base_atk=0,
                      normal=0, charged=0, burst=0, plunged=0, elemental_geo=0, elemental_cryo=0,
                      elemental_hydro=0, elemental_pyro=0, elemental_anemo=0, elemental_electro=0, physical=0,
                      overall=0, is_gladiator=False, is_wanderer=False)
    artifact_sets = {}
    # Get artifact sets, if any
    for _, value in space.items():
        d = value.get_stats()
        del d["type"]
        if d["name"] not in artifact_sets:
            artifact_sets[d["name"]] = 1
        else:
            artifact_sets[d["name"]] += 1
        del d["name"]
        for stat_name, number in d.items():
            dictionary[stat_name] += number

    # Get artifact effects
    for name, cnt in artifact_sets.items():
        if cnt > 1:
            artifact = ARTIFACT_SET_DETAILS.get(name)
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

    dictionary["crit_rate"] += state_obj.ADDITIONAL_CRIT_RATE
    dictionary["crit_dmg"] += state_obj.ADDITIONAL_CRIT_DMG
    dictionary["flat_atk"] += state_obj.ADDITIONAL_FLAT_ATK
    dictionary["percentage_atk"] += state_obj.ADDITIONAL_PERCENTAGE_ATK
    dictionary["normal"] += state_obj.ADDITIONAL_NORMAL_DMG_BONUS
    dictionary["charged"] += state_obj.ADDITIONAL_CHARGED_DMG_BONUS
    dictionary["burst"] += state_obj.ADDITIONAL_BURST_DMG_BONUS
    dictionary["plunged"] += state_obj.ADDITIONAL_PLUNGED_DMG_BONUS
    if dmg_type != "physical":
        dictionary["elemental_" + dmg_type] += state_obj.ADDITIONAL_ELEMENTAL_DMG_BONUS
    else:
        dictionary["physical"] += state_obj.ADDITIONAL_PHYSICAL_DMG_BONUS
    dictionary["overall"] += state_obj.ADDITIONAL_OVERALL_DMG_BONUS

    if not can_use_wanderer_4 and dictionary["is_wanderer"]:
        dictionary["charged"] -= 35
    if not can_use_gladiator_4 and dictionary["is_gladiator"]:
        dictionary["normal"] -= 35

    ATK = (state_obj.BASE_ATK + dictionary["base_atk"]) * (1 + dictionary["percentage_atk"] / 100) + dictionary[
        "flat_atk"]

    WITH_CRIT = ATK * state_obj.SKILL_MUL / 100 * dictionary["crit_rate"] / 100 * (dictionary["crit_dmg"] / 100 + 1)
    WITHOUT_CRIT = ATK * state_obj.SKILL_MUL / 100 * (1 - dictionary["crit_rate"] / 100)

    DMG_TYPE_DICT = {}
    for x in ["geo", "anemo", "hydro", "pyro", "cryo", "physical"]:
        DMG_TYPE_DICT[x] = dict(normal=0, charged=0, burst=0, plunged=0)
    for dmg_type in ["geo", "anemo", "hydro", "pyro", "cryo", "physical"]:
        for atk_type in ["normal", "charged", "plunged", "burst"]:
            AVERAGE_DMG = (WITH_CRIT + WITHOUT_CRIT) * (dictionary[objective_type] / 100 + 1)
            DMG_TYPE_DICT[dmg_type][atk_type] = AVERAGE_DMG

    if evaluate:
        st.write(f"ATK: {ATK}")
        st.write(f"STATS: {dictionary}")
        st.write(f"ARTIFACT SETS: {artifact_sets}")
        st.write(f"AVERAGE DMG: {DMG_TYPE_DICT[dmg_type][objective_type]}")
        return None

    return {"loss": -DMG_TYPE_DICT[dmg_type][objective_type], "status": STATUS_OK}


space = {
    "Sand": hp.choice("Sands", state.SANDS),
    "Flower": hp.choice("Flowers", state.FLOWERS),
    "Feather": hp.choice("Feathers", state.FEATHERS),
    "Goblet": hp.choice("Goblets", state.GOBLETS),
    "Circlet": hp.choice("Circlets", state.CIRCLETS),
    "Weapon": hp.choice("Weapons", state.WEAPONS)
}

if state.find_artifact:
    fn = partial(objective_function, state_obj=state, objective_type=state.DAMAGE_TYPE_1, dmg_type=state.DAMAGE_TYPE_2,
                 can_use_wanderer_4=state.CAN_USE_WANDERER_4,
                 can_use_gladiator_4=state.CAN_USE_GLADIATOR_4, evaluate=False)
    best_params = fmin(fn=fn, space=space, algo=tpe.suggest, max_evals=state.MAX_EVALS)
    objective_function(space_eval(space, best_params), state, state.DAMAGE_TYPE_1, state.DAMAGE_TYPE_2,
                       state.CAN_USE_WANDERER_4, state.CAN_USE_GLADIATOR_4, evaluate=True)
    st.write("ARTIFACT DETAILS: ")
    for i in space_eval(space, best_params).values():
        st.write(i)
