"""
Exercício 01:
  Fazer um programa para capturar 5 números quaisquer inteiros, e depois de digitar o 
  último número deverá ser apresentado na tela, a soma desses cinco números e a 
  média. Salve o arquivo com o nome de 01-Somando_e_Media. 
"""

numeros = []

for i in range(5):
  num = int(input("Digite o número inteiro: "))
  numeros.append(num)
  
soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
