class Categoria:
      def __init__(self, tipo):
            self.tipo = tipo

      def taxaAgua(self, consumo):
            match self.tipo:
                  case "Cínica" : return consumo * 1
                  case "Restaurante" : return consumo * 2
                  case "Hotel" : return consumo * 2.5
class Imovel:
      imposto = 0.2

      def __init__(self, nome, quartos, suites):
            self.nome = nome
            self.quartos = quartos
            self.suites = suites
            self.categoria = Categoria

      # soma um objeto com outro
      def __add__(self, other):
            somaSelf = self.quartos + self.suites
            somaOther = other.quartos + other.suites
            return somaSelf + somaOther
      
      # gt = greather than > maior que
      def __gt__(self, other):
            somaSelf = self.quartos + self.suites
            somaOther = other.quartos + other.suites
            return somaSelf > somaOther
      
      # lt = leasther than < menor que
      def __lt__(self, other):
            somaSelf = self.quartos + self.suites
            somaOther = other.quartos + other.suites
            return somaSelf < somaOther
      
      # substitui o __dict__ convetendo em String
      def __str__(self):
            return str(self.__dict__)
            
      def detalhar(self):
            return self.__dict__

      def somarAposentos(self):
            return self.quartos + self.suites
      
      @classmethod
      def metodoEstatico():
            print("Chamou o método estático sem criar um objeto")
      @classmethod
      def metodoClasse():
            print("Método de Classe para Imposto")

casarao = Imovel("Casarao", 3, 4)
mansao = Imovel("Mansão", 4, 5)

categoria = Categoria("Hotel")
hotel = Imovel("Hotel do Chico", 0, 150)
hotel.categoria = categoria
print(hotel)
print(categoria.taxaAgua(300))

'''
Imovel.metodoEstatico()
Imovel.metodoClasse()

Imovel.metodoEstatico()

casa = Imovel("casa", 6, 3)
# print(casa.__dict__)

mansao = Imovel("Mansão", 13, 5)
# print(mansao.__dict__)

soma = casa + mansao
print(soma)
print(casa > mansao)
print(casa < mansao)

print(casa)
print(mansao)
'''