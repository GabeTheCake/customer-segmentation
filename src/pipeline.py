from config import CLUSTER_COLUMNS, N_CLUSTERS, RANDOM_STATE
from src.data import carregar_dados, salvar_dados
from src.preprocessing import limpar_dados, transformar_variaveis, padronizar_features
from src.eda import resumo_geral, plotar_clusters, boxplot_clusters, distribuicao_renda, distribuicao_idade, heatmap_clusters, radar_chart_clusters
from src.clustering import aplicar_kmeans, nomear_clusters, tamanho_percentual_clusters
from src.evaluation import metodo_cotovelo, calcular_silhouette
from src.conclusion import gerar_conclusao
from src.report import gerar_relatorio_pdf

class CustomerSegmentationPipeline:

    def __init__(self, logger):
        self.logger = logger
        self.df = None
        self.X_scaled = None
        self.modelo = None

    def carregar(self):
        self.logger.info("Carregando dados...")
        self.df = carregar_dados()

    def eda(self):
        self.logger.info("Executando EDA...")
        resumo_geral(self.df)

    def preprocessar(self):
        self.logger.info("Executando pré-processamento...")
        self.df = limpar_dados(self.df)
        self.df = transformar_variaveis(self.df)
        self.X_scaled, _ = padronizar_features(self.df, CLUSTER_COLUMNS)

    def avaliar(self):
        self.logger.info("Aplicando método do cotovelo...")
        metodo_cotovelo(self.X_scaled)

    def clusterizar(self):
        self.logger.info("Executando KMeans...")
        self.modelo, clusters = aplicar_kmeans(
            self.X_scaled,
            n_clusters=N_CLUSTERS
        )
        self.df["Cluster"] = clusters
        self.df = nomear_clusters(self.df)
        tamanho_percentual_clusters(self.df)
        plotar_clusters(self.df)
        calcular_silhouette(self.X_scaled, clusters)
        boxplot_clusters(self.df)
        distribuicao_renda(self.df)
        distribuicao_idade(self.df)
        heatmap_clusters(self.df)
        radar_chart_clusters(self.df)
        gerar_relatorio_pdf(self.df)

    def salvar(self):
        self.logger.info("Salvando dados tratados...")
        salvar_dados(self.df)

    def concluir(self):
        self.logger.info("Gerando conclusão...")
        gerar_conclusao(self.df)

    def run(self):
        self.carregar()
        self.eda()
        self.preprocessar()
        self.avaliar()
        self.clusterizar()
        self.salvar()
        self.concluir()