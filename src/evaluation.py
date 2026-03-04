import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def metodo_cotovelo(X):
    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.title("Método do Cotovelo")
    plt.xlabel("Número de Clusters")
    plt.ylabel("WCSS")
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/elbow.png")
    plt.close()


def calcular_silhouette(X, clusters):
    score = silhouette_score(X, clusters)
    print("Silhouette Score:", score)