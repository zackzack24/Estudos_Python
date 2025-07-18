import json

pessoas = [
    {'nome': 'Isaac', 'telefone': '(12) 9 3456 7891', 'cidade': 'Rocinha'},
    {'nome': 'Joao', 'telefone': '(12) 9 4567 7891', 'cidade': 'Sao Paulo'},
    {'nome': 'Maria', 'telefone': '(12) 9 9472 5837', 'cidade': 'Xique Xique'},
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)