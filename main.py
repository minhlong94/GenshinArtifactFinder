import pandas as pd
import streamlit as st
from src.artifact import *
from src.button_confirmation import *
from src.artifact_set import ARTIFACT_SET_DETAILS, ARTIFACT_PIECE_NAME, ARTIFACT_STATS


def render_data(col2, holder, df):
    with col2:
        holder.table(df)


def main():
    df = pd.DataFrame(columns=["type", "name"] + list(ARTIFACT_STATS))
    st.title("Genshin Impact best artifact finder")
    st.info("This program finds the best artifact combination for you!")
    WEAPONS, SANDS, FEATHERS, GOBLETS, CIRCLETS, FLOWERS = [], [], [], [], [], []
    col1, col2 = st.beta_columns(2)
    with col1:
        artifact_set = st.selectbox("Artifact set: ", list(ARTIFACT_SET_DETAILS.keys()))
        artifact_piece = st.selectbox("Artifact piece: ", ARTIFACT_PIECE_NAME)
        artifact = eval(artifact_piece)(name=artifact_set)
        artifact_stats = st.multiselect("Substats: ", ARTIFACT_STATS)
        for stat in artifact_stats:
            var = st.number_input(f"{stat}: ")
            setattr(artifact, stat, var)
        # clicked = st.button("Create artifact!")
    with col2:
        holder = st.empty()
        holder.table(df)

    @cache_on_button_press('Create')
    def confirm_click():
        return True
    if confirm_click:
        if artifact_piece == "Sand":
            SANDS.append(artifact)
        elif artifact_piece == "Circlet":
            CIRCLETS.append(artifact)
        elif artifact_piece == "Feather":
            FEATHERS.append(artifact)
        elif artifact_piece == "Flower":
            FLOWERS.append(artifact)
        elif artifact_piece == "Goblet":
            GOBLETS.append(artifact)
        df = df.append(artifact.get_stats(), ignore_index=True)
        render_data(col2, holder, df)

main()