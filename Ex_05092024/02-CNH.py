"""
Exercício 02:
  Fazer um programa que pergunte a idade do cidadão, se ele tiver menos de 18 informe 
  que ele não pode ter Carteira de Habilitação. Salve esse aplicativo com o nome de 02
  CNH. 
"""

idade = int(input("Digite a sua idade: "))

if idade < 18:
  print("Você não pode ter Carteira de Habilitação")