import streamlit as st

st.set_page_config(
    page_title="Jogadores",
    page_icon="⛹🏽‍♂️",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["team"].value_counts().index
club = st.sidebar.selectbox("Franquia", clubes)

df_filtered = df_data[(df_data["team"] == club)].set_index("full_name")

st.image(df_filtered.iloc[0]["team_photo"])
st.markdown(f"## {club}")

columns = ["age", "players_photo", "team_photo", "rating", 'salary', 'position', 'jersey', 
           'height', 'weight',
           'draft_round', 'draft_peak']

st.dataframe(df_filtered[columns],
             column_config={
                 "rating": st.column_config.ProgressColumn(
                     "Overall", format= "%d", min_value=0, max_value=100
                 ),

                 "players_photo": st.column_config.ImageColumn(),
                 "team_photo": st.column_config.ImageColumn()
             })
