import pandas as pd
import matplotlib.pyplot as plt

class Investimento :
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

# def calcular_retorno(self):
# return self.valor * (1 + self.taxa) ** self.periodo

investimento  = {
      "Investimento 1": Investimento("Ações", 1000, 0.07, 5),
      "Investimento 2": Investimento("Tesouro Direto", 2000, 0.04, 2),
      "Investimento 3": Investimento("CDB", 1500, 0.05, 3),
      "Investimento 4": Investimento("Fundos Imobiliários", 2500 , 0.06, 4),
}

l_investimentos = [i.__dict__ for i in investimento.values()]
df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimento.keys()) # index=[f'Investimento{i+1}' for i in range(len(l_investimentos))]
df_investimentos['Retorno'] =  df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis=1)

df_investimentos.plot(kind="bar", y="Retorno", legend="False")
plt.title("Retorno dos Investimentos")
plt.xlabel("Investimentos")
plt.ylabel("Retonro em Reais")
plt.show()
# print(df_investimentos)

