# 📊 Segmentação de Clientes com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)  
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Clustering-orange)  
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Projeto de Data Science focado em **segmentação estratégica de clientes**, utilizando **KMeans, análise exploratória, métricas de avaliação e dashboard executivo interativo**.

O objetivo é simular um cenário real de negócio onde a empresa precisa identificar perfis de clientes para direcionar estratégias de marketing, retenção e aumento de receita.

Este projeto foi desenvolvido como parte de portfólio para demonstrar habilidades em **engenharia de dados, modelagem não supervisionada, arquitetura de projeto e visualização executiva**.

---

## 🎯 Problema de Negócio

Empresas que possuem uma base de clientes heterogênea enfrentam desafios como:

- Comunicação ineficiente  
- Baixa conversão em campanhas  
- Estratégias genéricas que reduzem ROI  

**Pergunta central:**

> É possível identificar grupos distintos de clientes com base em idade e renda para apoiar decisões estratégicas?

---

## 🧠 Técnicas Utilizadas

- Limpeza e tratamento de dados  
- Padronização de variáveis  
- Clustering com KMeans  
- Método do Cotovelo  
- Métrica de Silhouette Score  
- Nomeação estratégica de clusters  
- Análise comparativa entre perfis  
- Geração automática de relatório executivo em PDF  
- Dashboard interativo com filtros dinâmicos  

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Plotly  
- Streamlit  
- ReportLab (geração de PDF)  
- Logging (estrutura profissional de projeto)  

---

## 📁 Estrutura do Projeto

```
Projeto 1 - customer-segmentation/
│
├── data/
│   ├── segmentation data legend.xlsx
│   ├── segmentation data_tratado.csv
│   └── segmentation data.csv
│
├── logs/
│   └── projeto.log
│
├── notebook/
│   └── Cluster.ipynb
│
├── outputs/
│   ├── boxplot_renda.png
│   ├── clusters.png
│   ├── distribuicao_idade.png
│   ├── distribuicao_renda.png
│   ├── elbow.png
│   ├── heatmap_clusters.png
│   ├── radar_clusters.png
│   └── relatorio_segmentacao_clientes.pdf
│
├── src/
│   ├── clustering.py
│   ├── conclusion.py
│   ├── data.py
│   ├── eda.py
│   ├── evaluation.py
│   ├── logger_config.py
│   ├── pipeline.py
│   ├── preprocessing.py
│   └── report.py
│
├── app.py
├── config.py
├── main.py
├── README.md
├── Relatorio.md
└── requirements.txt
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### 3️⃣ Ativar o ambiente

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 4️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔎 Executar Pipeline Completo

```bash
python main.py
```

O pipeline executa automaticamente:

- Pré-processamento  
- Clusterização  
- Avaliação do modelo  
- Geração de gráficos  
- Exportação de relatório em PDF  
- Salvamento do dataset clusterizado  

---

## 🌐 Executar Dashboard Interativo (Streamlit)

```bash
streamlit run app.py
```

### Funcionalidades do Dashboard

- Filtro lateral por cluster  
- Filtro por faixa de renda  
- Comparação média entre perfis  
- Radar chart comparativo  
- Boxplot por cluster  
- Distribuição de idade e renda  
- Visual profissional voltado para tomada de decisão executiva  

---

## 📈 Principais Insights

- Foram identificados **clusters distintos de clientes** com perfis claros.  
- Diferenças significativas de renda e idade entre grupos.  
- Segmentos com maior potencial de monetização foram identificados.  
- O Silhouette Score validou a separação dos grupos.  

---

## 📊 Métricas do Modelo

- Método do Cotovelo utilizado para definição de K  
- Silhouette Score calculado para validação da coesão dos clusters  
- Comparação média entre variáveis por perfil  

---

## 📄 Relatório Executivo Automático

O projeto gera automaticamente um **relatório profissional em PDF**, contendo:

- Resumo do problema  
- Metodologia aplicada  
- Gráficos estratégicos  
- Comparação entre clusters  
- Conclusões de negócio  

Ideal para simular entrega real para stakeholders.

---

## 📚 Notebook da Análise

O notebook com toda a análise exploratória está disponível em:

```
notebooks/analise_segmentacao_clientes.ipynb
```

---

## 🚀 Possíveis Melhorias Futuras

- Deploy do dashboard na nuvem (Streamlit Cloud ou Render)  
- Inclusão de novas variáveis comportamentais  
- Implementação de outros algoritmos (DBSCAN, Hierarchical Clustering)  
- Automação de ingestão de dados  
- Monitoramento contínuo de clusters  

---

## 👤 Autor

**Gabriel**  
📊 Data Analytics | Data Science | Machine Learning  
🌎 Interesse em oportunidades remotas e internacionais  

---

## 📄 Licença

Este projeto está sob a licença MIT.