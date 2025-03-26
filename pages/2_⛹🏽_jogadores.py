import streamlit as st


st.set_page_config(
    page_title="Jogadores",
    page_icon="⛹🏽‍♂️",
    layout="wide"
)
df_data = st.session_state["data"]


clubes = df_data["team"].value_counts().index
club = st.sidebar.selectbox("Franquia", clubes)

df_players = df_data[(df_data["team"] == club)]
players = df_players["full_name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["full_name"] == player].iloc[0]

st.image(player_stats["players_photo"], width=200)
st.title(player_stats["full_name"])

st.markdown(f"**Franquia:** {player_stats['team']}")
st.markdown(f"**Posição:** {player_stats['position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['age']}")
col2.markdown(f"**Altura:** {player_stats['height']}")
col3.markdown(f"**Peso:** {player_stats['weight']}")
st.divider()

st.subheader(f"Overall {player_stats['rating']}")
st.progress(int(player_stats["rating"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Salário", value=f"{player_stats['salary']}")
col2.metric(label="Jersey", value=f" {player_stats['jersey']}")
