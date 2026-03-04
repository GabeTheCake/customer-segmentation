from src.data import carregar_dados_tratados, carregar_pdf_relatorio
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Segmentação de Clientes",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Executivo - Segmentação de Clientes")


# CARREGAMENTO
@st.cache_data
def load_data():
    return carregar_dados_tratados()

df = load_data()


# SIDEBAR - FILTROS
st.sidebar.header("🔎 Filtros")

perfis_disponiveis = sorted(df["Perfil"].unique())

perfil_selecionado = st.sidebar.multiselect(
    "Selecionar Perfil",
    perfis_disponiveis,
    default=perfis_disponiveis
)

renda_min = int(df["Income"].min())
renda_max = int(df["Income"].max())

faixa_renda = st.sidebar.slider(
    "Faixa de Renda",
    renda_min,
    renda_max,
    (renda_min, renda_max),
    format="$ %0.0f"
)

# Aplicando filtros
df_filtrado = df[
    (df["Perfil"].isin(perfil_selecionado)) &
    (df["Income"] >= faixa_renda[0]) &
    (df["Income"] <= faixa_renda[1])
]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
    st.stop()

# KPIs
st.subheader("📌 Indicadores Estratégicos")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Clientes Selecionados", len(df_filtrado))
col2.metric("Perfis Ativos", df_filtrado["Perfil"].nunique())
col3.metric("Renda Média", f"$ {df_filtrado['Income'].mean():,.0f}")
col4.metric("Idade Média", f"{df_filtrado['Age'].mean():.1f} anos")


# DISTRIBUIÇÃO PERCENTUAL
st.subheader("🥧 Distribuição Percentual por Perfil")

perfil_counts = df_filtrado["Perfil"].value_counts(normalize=True) * 100

fig_pie = px.pie(
    values=perfil_counts.values,
    names=perfil_counts.index,
    hole=0.4
)

st.plotly_chart(fig_pie, width='stretch')


# BOXPLOT
st.subheader("📦 Renda por Perfil")

fig_box = px.box(
    df_filtrado,
    x="Perfil",
    y="Income",
    color="Perfil"
)

st.plotly_chart(fig_box, width='stretch')


# DISTRIBUIÇÕES
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Distribuição de Renda")
    fig_renda = px.histogram(
        df_filtrado,
        x="Income",
        color="Perfil",
        barmode="overlay",
        nbins=30
    )
    st.plotly_chart(fig_renda, width='stretch')

with col2:
    st.subheader("📈 Distribuição de Idade")
    fig_idade = px.histogram(
        df_filtrado,
        x="Age",
        color="Perfil",
        barmode="overlay",
        nbins=30
    )
    st.plotly_chart(fig_idade, width='stretch')


# HEATMAP
st.subheader("🔥 Comparação Média entre Perfis")

cluster_means = df_filtrado.groupby("Perfil")[["Income", "Age"]].mean()

cluster_means_formatado = cluster_means.copy()
cluster_means_formatado["Income"] = cluster_means_formatado["Income"].map(lambda x: f"${x:,.0f}")
cluster_means_formatado["Age"] = cluster_means_formatado["Age"].map(lambda x: f"{x:.0f}")

fig, ax = plt.subplots(figsize=(6,3))
sns.heatmap(
    cluster_means,
    annot=cluster_means_formatado,
    fmt="",
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Média de Income e Age por Perfil")
plt.tight_layout()
st.pyplot(fig)


# RADAR CHART COMPARATIVO
st.subheader("🕸 Radar Comparativo")

features = ["Income", "Age"]

cluster_means_norm = (cluster_means - cluster_means.min()) / (cluster_means.max() - cluster_means.min())

fig_radar = px.line_polar()

for perfil in cluster_means.index:
    fig_radar.add_scatterpolar(
        r=cluster_means_norm.loc[perfil].values,
        theta=features,
        fill='toself',
        name=perfil
    )

fig_radar.update_layout(showlegend=True, polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
st.plotly_chart(fig_radar, width='stretch')


# INSIGHT AUTOMÁTICO
st.subheader("🧠 Insight Estratégico")

if len(cluster_means) > 0:
    perfil_maior_renda = cluster_means["Income"].idxmax()
    perfil_maior_idade = cluster_means["Age"].idxmax()

    st.info(
        f"""
        • O perfil com maior renda média é **{perfil_maior_renda}**.  
        • O perfil com maior idade média é **{perfil_maior_idade}**.  
        • Estratégia sugerida: campanhas premium direcionadas ao perfil de maior renda.
        """
    )


# DOWNLOAD PDF
st.subheader("📄 Relatório Executivo")

relatorio_clusterizacao = carregar_pdf_relatorio()
with open(relatorio_clusterizacao, "rb") as f:
    st.download_button(
        label="Baixar Relatório Completo em PDF",
        data=f,
        file_name="relatorio_clusterizacao.pdf",
        mime="application/pdf"
    )