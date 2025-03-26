import streamlit as st
#import webbrowser
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("NBA2k.csv", index_col=0)
    df_data = df_data.sort_values(by="rating", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# NBA 2K DATASET! 🏀")
st.sidebar.markdown("Desenvolvido por Cleomir Braga")


st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/cleomirbraga/base-de-dados-nba-2k")

st.markdown(
    """
    O conjunto de dados
    de jogadores de basquete da NBA fornece informações 
    abrangentes sobre jogadores de basquete profissionais.
    O conjunto de dados contém uma ampla gama stats gerais do jogador, características físicas, jersey, detalhes do contrato e 
    afiliações de franquias. 
    
    Com **mais de 400 registros**, este conjunto de dados oferece um recurso valioso para 
    curiosos e entusiastas de basquetes,
    pois permite estudar atributos de jogadores, métricas de 
    overall, avaliação de mercado, posicionamento de jogadores, draft
    e seus rankings de escolha.
"""
)
