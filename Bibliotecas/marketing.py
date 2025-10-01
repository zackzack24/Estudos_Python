import matplotlib.pyplot as plt

class Campanha:
      def __init__(self, canal, investimento, cliques, conversoes):
            self.canal = canal
            self.investimento = investimento
            self.cliques = cliques
            self.conversoes = conversoes
            
      def custoporclique(self):
            return self.investimento / self.cliques if self.cliques != 0 else 0
      
campanhas = [
      Campanha("Google Ads", 1000, 5000, 200),
      Campanha("Facebook Ads", 800, 3000, 150),
      Campanha("Instagram Ads", 600, 2500, 100),
      Campanha("LinkedIn Ads", 1200, 4000, 250),     
      Campanha("Twitter Ads", 700, 2000, 80),
      Campanha("TikTok Ads", 500, 1500, 60),
      Campanha("YouTube Ads", 1100, 3500, 180),
]

canais = [c.canal for c in campanhas]
custos = [c.custoporclique() for c in campanhas]   

print(canais)   
print(custos)
   
plt.grid(True) # Adiciona o quadriculado ao gráfico
plt.bar(canais, custos)
media_custo = sum(custos) / len(custos)
plt.axhline(media_custo, label='Média custo por clique')
plt.show()


