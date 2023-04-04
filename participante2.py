from main import GraficoParticipante

dados_teste1 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Atenção': [15, 60, 51, 55, 55, 41, 77, 37, 80, 87, 100, 74, 69, 60, 41, 67, 65, 84, 65, 61, 55, 43, 93, 64, 97, 45, 77, 70, 58, 67, 55],
    'Distração': [80, 41, 73, 63, 79, 77, 100, 100, 100, 90, 100, 87, 58, 100, 73, 88, 100, 100, 90, 87, 83, 100, 100, 100, 100, 100, 86, 88, 71, 84, 100],
    'Gama 1': [7, 3, 17, 15, 7, 21, 10, 5, 7, 15, 10, 18, 26, 17, 10, 17, 28, 5, 7, 40, 15, 8, 10, 15, 20, 7, 17, 47, 11, 20, 30],
    'Gama 2': [3, 3, 3, 7, 7, 13, 7, 5, 9, 7, 7, 5, 15, 19, 13, 7, 17, 21, 8, 7, 23, 7, 13, 10, 12, 7, 8, 10, 17, 15, 22],
    'Meditação': [16, 51, 50, 77, 37, 64, 30, 34, 43, 61, 37, 70, 87, 53, 56, 70, 56, 20, 66, 67, 47, 48, 29, 35, 24, 38, 44, 56, 80, 84, 74]
}

dados_teste2 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Atenção': [18, 50, 50, 50, 55, 65, 54, 57, 50, 47, 40, 67, 84, 47, 37, 81, 55, 60, 57, 55, 75, 60, 70, 87, 60, 55, 73, 51, 37, 53, 57],
    'Distração': [98, 95, 85, 65, 90, 93, 100, 65, 85, 100, 85, 100, 100, 90, 80, 100, 100, 100, 97, 87, 100, 100, 100, 99, 97, 100, 90, 77, 85, 100, 99],
    'Gama 1': [10, 16, 24, 15, 12, 19, 26, 10, 13, 30, 13, 20, 32, 40, 25, 18, 36, 15, 10, 25, 32, 25, 20, 47, 37, 27, 27, 28, 34, 35, 33],
    'Gama 2': [7, 9, 25, 11, 5, 14, 14, 8, 8, 25, 10, 10, 22, 13, 16, 24, 35, 14, 10, 22, 23, 15, 35, 27, 20, 17, 20, 12, 18, 12, 23],
    'Meditação': [44, 67, 61, 80, 77, 69, 64, 81, 64, 60, 75, 77, 54, 24, 60, 75, 63, 48, 53, 63, 51, 40, 53, 60, 69, 57, 74, 64, 74, 30, 43]
}

dados_teste3 = {
    'Tempo (segundos)': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Atenção': [43, 43, 40, 57, 50, 50, 51, 47, 53, 57, 50, 48, 57, 48, 57, 53, 50, 63, 57, 69, 69, 50, 76, 75, 60, 70, 61, 60, 47, 45, 90],
    'Distração': [100, 60, 73, 95, 85, 92, 100, 96, 100, 80, 80, 85, 78, 96, 75, 72, 100, 87, 95, 100, 100, 88, 100, 100, 96, 100, 85, 78, 90, 100, 100],
    'Gama 1': [43, 20, 32, 17, 17, 38, 10, 27, 37, 23, 27, 33, 23, 27, 27, 10, 25, 25, 43, 23, 13, 23, 41, 42, 42, 32, 43, 33, 33, 30, 35],
    'Gama 2': [30, 12, 17, 17, 17, 15, 7, 25, 21, 22, 28, 20, 20, 23, 26, 5, 25, 25, 20, 15, 12, 15, 21, 30, 18, 23, 22, 17, 41, 17, 23],
    'Meditação': [50, 75, 74, 41, 78, 56, 50, 57, 40, 63, 69, 61, 67, 64, 66, 57, 48, 47, 34, 35, 40, 27, 48, 47, 35, 44, 40, 57, 70, 81, 44]
}

grafico_teste1 = GraficoParticipante(dados_teste1, 2, 1)
grafico_teste1.gerar_grafico()

grafico_teste2 = GraficoParticipante(dados_teste2, 2, 2)
grafico_teste2.gerar_grafico()

grafico_teste3 = GraficoParticipante(dados_teste3, 2, 3)
grafico_teste3.gerar_grafico()
