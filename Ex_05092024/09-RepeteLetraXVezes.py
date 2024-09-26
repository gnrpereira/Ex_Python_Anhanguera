"""
Exercício 09:
  Crie um programa que pergunte ao usuário quantas vezes ele deseja que uma letra seja 
  repetida, depois que o usuário responder, pergunte qual é a letra que deve ser escrita 
  repetidamente na tela, logo depois escreva na tela “Imprimindo” e imprima essa letra, 
  a quantidade de vezes solicitada na tela. Salve com o nome de 09-RepeteLetraXVezes. 
"""

quantidade = int(input("Quantas vezes deseja repetir a letra? "))

letra = input("Qual letra deseja que seja repetida? ")

print("Imprimindo")

for i in range(quantidade):
  print(letra)