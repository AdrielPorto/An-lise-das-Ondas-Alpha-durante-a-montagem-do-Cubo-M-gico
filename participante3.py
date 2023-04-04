from main import GraficoParticipante

dados_teste1 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 55],
    'Atenção': [50, 14, 50, 40, 57, 45, 40],
    'Distração': [100, 57, 100, 98, 98, 80, 88],
    'Gama 1': [7, 35, 23, 23, 25, 15, 15],
    'Gama 2': [7, 19, 14, 11, 20, 10, 10],
    'Meditação': [43, 61, 38, 56, 63, 57, 40]
}

dados_teste2 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 60, 65],
    'Atenção': [58, 38, 40, 40, 25, 57, 47, 57],
    'Distração': [58, 80, 98, 86, 70, 88, 75, 68],
    'Gama 1': [14, 25, 20, 22, 27, 24, 20, 18],
    'Gama 2': [10, 25, 20, 14, 19, 14, 14, 29],
    'Meditação': [54, 75, 47, 80, 81, 63, 81, 66]
}

dados_teste3 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 55],
    'Atenção': [40, 40, 35, 35, 56, 34, 40],
    'Distração': [100, 72, 100, 76, 88, 68, 62],
    'Gama 1': [18, 25, 20, 18, 17, 35, 20],
    'Gama 2': [10, 20, 20, 15, 12, 18, 20],
    'Meditação': [35, 70, 56, 70, 50, 61, 69]
}

grafico_teste1 = GraficoParticipante(dados_teste1, 3, 1)
grafico_teste1.gerar_grafico()

grafico_teste2 = GraficoParticipante(dados_teste2, 3, 2)
grafico_teste2.gerar_grafico()

grafico_teste3 = GraficoParticipante(dados_teste3, 3, 3)
grafico_teste3.gerar_grafico()
