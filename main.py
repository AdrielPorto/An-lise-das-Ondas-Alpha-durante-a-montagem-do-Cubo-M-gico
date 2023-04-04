import matplotlib.pyplot as plt
import pandas as pd
import uuid

class GraficoParticipante:
    def __init__(self, dados, participante, teste, nome_arquivo=None):
        self.dados = dados
        self.participante = participante
        self.teste = teste
        self.nome_arquivo = nome_arquivo
    def gerar_grafico(self):
        # Gerando um nome de arquivo aleatório se não foi fornecido um nome
        if self.nome_arquivo is None:
            self.nome_arquivo = str(uuid.uuid4()) + '.png'

        # Criando uma figura
        fig, ax = plt.subplots(figsize=(10, 6))

        # Adicionando uma linha para cada conjunto de dados
        ax.plot(self.dados['Tempo (segundos)'], self.dados['Atenção'], label='Atenção')
        ax.plot(self.dados['Tempo (segundos)'], self.dados['Distração'], label='Distração')
        ax.plot(self.dados['Tempo (segundos)'], self.dados['Gama 1'], label='Gama 1')
        ax.plot(self.dados['Tempo (segundos)'], self.dados['Gama 2'], label='Gama 2')
        ax.plot(self.dados['Tempo (segundos)'], self.dados['Meditação'], label='Meditação')

        # Adicionando linhas tracejadas no fundo do gráfico
        ax.grid(linestyle='--')

        # Adicionando rótulos aos eixos x e y
        ax.set_xlabel('Tempo (segundos)')
        ax.set_ylabel('Valores')

        # Adicionando uma legenda
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

        # Adicionando título
        ax.set_title('Participante {} - Teste {}'.format(self.participante, self.teste))

        # Ajustando o tamanho da figura
        fig.set_size_inches(15, 8)

        # Salvando o gráfico como imagem
        plt.savefig(self.nome_arquivo, dpi=300, bbox_inches='tight')

        # Mostrando o gráfico
        plt.show()
