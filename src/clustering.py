from sklearn.cluster import KMeans


def aplicar_kmeans(X, n_clusters=5):
    modelo = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = modelo.fit_predict(X)
    return modelo, clusters

def tamanho_percentual_clusters(df):
    distribuicao = df["Perfil"].value_counts(normalize=True) * 100
    distribuicao = distribuicao.round(2)
    print("\n📊 Participação percentual por perfil:\n")
    print(distribuicao)
    return distribuicao

def nomear_clusters(df):
    resumo = df.groupby("Cluster")[["Age", "Income"]].mean()
    q1_income = df["Income"].quantile(0.25)
    q3_income = df["Income"].quantile(0.75)

    nomes = {}

    for cluster, row in resumo.iterrows():
        # Classificação por idade
        if row["Age"] < 30:
            idade_label = "Jovens"
        elif row["Age"] <= 50:
            idade_label = "Adultos"
        else:
            idade_label = "Idosos"

        # Classificação por renda
        if row["Income"] < q1_income:
            renda_label = "Baixa Renda"
        elif row["Income"] <= q3_income:
            renda_label = "Renda Média"
        else:
            renda_label = "Alta Renda"

        nomes[cluster] = f"{idade_label} - {renda_label}"

    df["Perfil"] = df["Cluster"].map(nomes)

    print("\n📊 Perfil médio por cluster:\n")
    print(resumo)

    print("\n📌 Nomeação dos clusters:\n")
    for k, v in nomes.items():
        print(f"Cluster {k} → {v}")

    return df