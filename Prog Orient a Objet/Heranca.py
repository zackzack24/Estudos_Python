class Imovel:
      def __init__(self, nome, uf, valor, endereco = '', area = ''):
          self.nome = nome
          self.uf = uf
          self.valor = valor
          self.endereco = endereco
          self.area = area

      def detalhar(self):
           print(self.__dict__)

      def calcularImposto(self):    
           return self.valor  * 0.02
      
class ImovelResidencial(Imovel):
    ...

class ImovelComercial(Imovel):
    ...

casa = ImovelResidencial('Casa Trator', 'DF', 300000, 'Rua das Flores, 123', '150 m²')
casa.detalhar()

clinica = ImovelComercial('Clinica do Bem', 'DF', 800000, 'Avenida Central, 456', '300 m²')
clinica.detalhar()
    
     
# Imovel = Imovel('Solar do Cerrado', 'DF', 500000,) 
# Imovel.endereco = 'Rua das Flores, 123'
# Imovel.area = '200 m²'
# print(