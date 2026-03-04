import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os

def resumo_geral(df):
    print("\n📌 HEAD\n")
    print(df.head())

    print("\n📌 INFO\n")
    print(df.info())

    print("\n📌 DESCRIBE\n")
    print(df.describe())


def distribuicao_categoricas(df):
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        print(f"\nDistribuição de {col}")
        print(df[col].value_counts())


def grafico_idade_renda(df):
    sns.scatterplot(data=df, x="Age", y="Income")
    plt.title("Relação Idade x Renda")
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/grafico_idade_renda.png")
    plt.close()

def plotar_clusters(df):
    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        data=df,
        x="Age",
        y="Income",
        hue="Cluster",
        palette="Set2",
        s=80
    )

    plt.title("Segmentação de Clientes")
    plt.legend(title="Cluster")
    plt.savefig("outputs/clusters.png")
    plt.close()

def boxplot_clusters(df):
    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(8,6))
    sns.boxplot(data=df, x="Perfil", y="Income")
    plt.xticks(rotation=45)
    plt.title("Distribuição de Renda por Perfil")
    plt.tight_layout()
    plt.savefig("outputs/boxplot_renda.png")
    plt.close()

def distribuicao_renda(df):
    plt.figure(figsize=(8,6))
    sns.histplot(data=df, x="Income", hue="Perfil", kde=True, element="step")
    plt.title("Distribuição de Renda por Perfil")
    plt.savefig("outputs/distribuicao_renda.png")
    plt.close()

def distribuicao_idade(df):
    plt.figure(figsize=(8,6))
    sns.histplot(data=df, x="Age", hue="Perfil", kde=True, element="step")
    plt.title("Distribuição de Idade por Perfil")
    plt.savefig("outputs/distribuicao_idade.png")
    plt.close()

def heatmap_clusters(df):
    os.makedirs("outputs", exist_ok=True)
    resumo = df.groupby("Perfil")[["Age", "Income"]].mean()
    plt.figure(figsize=(8,6))
    sns.heatmap(resumo, annot=True, cmap="YlGnBu", fmt=".0f")
    plt.title("Comparação Média por Perfil")
    plt.tight_layout()
    plt.savefig("outputs/heatmap_clusters.png")
    plt.close()

def radar_chart_clusters(df):
    os.makedirs("outputs", exist_ok=True)
    resumo = df.groupby("Perfil")[["Age", "Income"]].mean()
    categorias = list(resumo.columns)
    num_vars = len(categorias)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    plt.figure(figsize=(8,8))

    for index, row in resumo.iterrows():
        values = row.tolist()
        values += values[:1]
        plt.polar(angles, values, label=index)

    plt.xticks(angles[:-1], categorias)
    plt.title("Radar Chart por Perfil")
    plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.savefig("outputs/radar_clusters.png")
    plt.close()