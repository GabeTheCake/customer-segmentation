def gerar_conclusao(df):
    print("\n📌 CONCLUSÃO:\n")
    print("Foram identificados diferentes segmentos de clientes com base em idade e renda.")
    print("A segmentação pode auxiliar estratégias de marketing e posicionamento.")
    print("\nDistribuição por cluster:")
    print(df["Cluster"].value_counts())
    print("\nMédia por cluster:")
    print(df.groupby("Cluster")[["Age", "Income"]].mean())