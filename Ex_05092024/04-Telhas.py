"""
Exercício 04:
  Um engenheiro precisa construir um telhado de uma casa, ele sabe que se gastam 20 
  telhas para cada metro quadrado, faça um programa que pergunte ao usuário quantos 
  metros quadrados tem a casa, e o programa deverá informar quantas telhas serão 
  necessárias para fazer o telhado da casa. Salve com o nome de 04-Telhas. 
"""

metros_quadrados_casa = float(input("Quantos metros quadrados tem o telhado da casa? "))

telhas_metro_quadrado = 20

telhas_suficientes = metros_quadrados_casa * telhas_metro_quadrado

print(f"Para cobrir o telhado da casa é preciso {telhas_suficientes} telhas.")
