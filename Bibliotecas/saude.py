import numpy as np
import pandas as pd

class Paciente:
      def __init__(self, nome, idade, sexo, peso, altura):
          self.nome = nome
          self.idade = idade
          self.sexo = sexo
          self.peso = peso
          self.altura = altura

paciente = {
      "Paciente 1": Paciente("Ana", 28, "F", 65, 1.70),
      "Paciente 2": Paciente("Bruno", 34, "M", 85, 1.80),
      "Paciente 3": Paciente("Carla", 45, "F", 70,  1.65),
      "Paciente 4": Paciente("Daniel", 50, "M", 90, 1.75),
      "Paciente 5": Paciente("Eva", 30, "F", 55, 1.60),
      "Paciente 6": Paciente("Felipe", 40, "M", 95, 1.85),
      "Paciente 7": Paciente("Gabriela", 29, "F", 60,  1.68),
}

l_pacientes = [p.__dict__ for p in paciente.values()]

print(l_pacientes)

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=paciente.keys())
# index=[f'Paciente{i+1}' for i in range(len(l_pacientes))]

df_pacientes['imc'] = df_pacientes.apply(lambda i: i.peso / (i.altura ** 2), axis=1)

media = np.mean(df_pacientes['imc'])

sobrepeso = df_pacientes[df_pacientes['imc'] > 25]

print(df_pacientes)


