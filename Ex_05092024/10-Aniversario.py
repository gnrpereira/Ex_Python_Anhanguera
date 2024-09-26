"""
Exercício 10:
 Crie um programa que pergunte ao usuário o ano que ele nasceu e o programa vai 
  calcular a quantidade de anos que ele vai ter quando fizer aniversário no ano de 2024. 
  Salve com o nome de 10-Aniversario.
"""

ano_nascimento = int(input("Digite o ano em que você nasceu: "))

ano_atual = 2024

idade_em_2024 = ano_atual - ano_nascimento

print(f"Você terá {idade_em_2024} anos em {ano_atual}.")