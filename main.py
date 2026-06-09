import streamlit as st

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
"Vendas": [120, 145, 98, 200, 175, 230],
"Clientes": [40, 55, 35, 80, 70, 95],
})
st.title("Painel de Vendas" )
st.write("Resumo dos últimos 6 meses" )
# Exibe o dataframe interativa
st.subheader("Dados brutos" )
st.dataframe(df, use_container_width =True)