import pandas as pd
from pathlib import Path

def salvar_dados(df):
    caminho = 'data/segmentation data_tratado.csv'
    df.to_csv(caminho, index=False)
    resposta = f"Dados salvos com sucesso em: {caminho}"
    return resposta

def carregar_dados():
    base_dir = Path(__file__).parent.parent.resolve()
    data_path = base_dir / 'data' / 'segmentation data.csv'
    df = pd.read_csv(data_path)
    return df

def carregar_dados_tratados():
    base_dir = Path(__file__).parent.parent.resolve()
    data_path = base_dir / 'data' / 'segmentation data_tratado.csv'
    df = pd.read_csv(data_path)
    return df

def carregar_pdf_relatorio():
    base_dir = Path(__file__).parent.parent.resolve()
    pdf_path = base_dir / 'outputs' / 'relatorio_segmentacao_clientes.pdf'
    return pdf_path