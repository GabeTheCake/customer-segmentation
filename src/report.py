from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import os
from datetime import datetime


def gerar_relatorio_pdf(df):

    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/relatorio_segmentacao_clientes.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)

    elements = []
    styles = getSampleStyleSheet()

    # ==============================
    # TÍTULO
    # ==============================
    elements.append(Paragraph("Relatório de Segmentação de Clientes", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    data_atual = datetime.now().strftime("%d/%m/%Y")
    elements.append(Paragraph(f"Data de geração: {data_atual}", styles["Normal"]))
    elements.append(Spacer(1, 0.5 * inch))

    # ==============================
    # PARTICIPAÇÃO
    # ==============================
    distribuicao = df["Perfil"].value_counts(normalize=True) * 100
    distribuicao = distribuicao.round(2)

    elements.append(Paragraph("Participação Percentual por Perfil:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    data_table = [["Perfil", "Percentual (%)"]]

    for perfil, perc in distribuicao.items():
        data_table.append([perfil, f"{perc}%"])

    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (1,1), (-1,-1), 'CENTER')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    # ==============================
    # MÉDIAS
    # ==============================
    resumo = df.groupby("Perfil")[["Age", "Income"]].mean().round(2)

    elements.append(Paragraph("Média de Idade e Renda por Perfil:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    data_table = [["Perfil", "Idade Média", "Renda Média"]]

    for perfil, row in resumo.iterrows():
        data_table.append([perfil, str(row["Age"]), f"{row['Income']}"])

    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (1,1), (-1,-1), 'CENTER')
    ]))

    elements.append(table)
    elements.append(PageBreak())

    # ==============================
    # GRÁFICOS
    # ==============================

    graficos = [
        "clusters.png",
        "boxplot_renda.png",
        "distribuicao_renda.png",
        "distribuicao_idade.png",
        "heatmap_clusters.png",
        "radar_clusters.png"
    ]

    for grafico in graficos:
        caminho = os.path.join("outputs", grafico)

        if os.path.exists(caminho):
            elements.append(Paragraph(grafico.replace(".png", "").replace("_", " ").title(), styles["Heading2"]))
            elements.append(Spacer(1, 0.2 * inch))

            img = Image(caminho, width=5.5 * inch, height=4 * inch)
            elements.append(img)
            elements.append(PageBreak())

    # ==============================
    # CONCLUSÃO
    # ==============================
    elements.append(Paragraph("Conclusão:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    texto_conclusao = (
        "A análise identificou segmentos distintos de clientes com base em idade e renda. "
        "Os resultados podem apoiar estratégias de segmentação, marketing direcionado "
        "e posicionamento estratégico."
    )

    elements.append(Paragraph(texto_conclusao, styles["Normal"]))

    doc.build(elements)

    print("\n📄 Relatório PDF completo gerado com sucesso em:", file_path)