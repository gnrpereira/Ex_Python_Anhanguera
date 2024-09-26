"""
Exercício 17:
    Faça um programa para um CLINICO GERAL, que calcule o IMC de uma pessoa, e 
    baseado no IMC obtido informe ao médico a mensagem conforme a tabela abaixo, 
    pesquise na internet como é o cálculo do IMC, e o que o CLINICO GERAL deverá 
    perguntar para o PACIENTE na hora da consulta. Salve como 17-IMC.
"""

nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente em kg: "))
altura = float(input("Digite a altura do paciente em metros: "))

imc = peso / (altura ** 2)


if imc < 16.9:
    classificacao = "Muito abaixo do peso"
elif  17 >= imc < 18.4:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Acima do peso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f"\nNome do paciente: {nome}")
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")