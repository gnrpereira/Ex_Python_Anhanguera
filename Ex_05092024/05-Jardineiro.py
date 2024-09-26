"""
Exercício 05:
  Faça um programa para descobrir quantas horas serão necessárias para um jardineiro 
  plantar flores em um lote, sabendo que ele gasta 2 horas por metro quadrado para 20
  preparar o solo e plantar as flores. Para isso você deverá perguntar para o usuário qual 
  a largura do lote e o comprimento, e assim imprimir quantas horas serão necessárias. 
  Salve com o o nome de 05-Jardineiro. 
"""

largura = float(input("Digite a largura do lote: "))
comprimento = float(input("Digite o comprimento do lote: "))

area_do_lote = largura * comprimento

horas_metro_quadrado = 2

horas_suficientes = area_do_lote * horas_metro_quadrado

print(f"Para preparar o solo e plantar as flores serão preciso {horas_suficientes} horas")