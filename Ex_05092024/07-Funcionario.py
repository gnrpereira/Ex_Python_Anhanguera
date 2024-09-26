"""
Exercício 07:
  Crie um programa que questione o salário de um funcionário e calcule os impostos que 
  devem ser descontados de seu salário conforme abaixo: 
  
  a. Calcule INSS (é uma contribuição do trabalhador para a previdência social, que 
  é descontada diretamente da folha de pagamento): para calcular o INSS você 
  deve calcular neste momento 11% do valor do salário que o funcionário recebe; 
  
  b. Calculo o IR (imposto de Renda): para calcular o IR você deve calcular neste 
  momento 15% do salário do funcionário. 
  
  c. Imprima na tela, o valor do salário do funcionário, o valor do INSS calculado, o 
  valor do IR calculado, e o valor do salário líquido (para calcular o salário líquido 
  subtraia do salário do funcionário os impostos calculados anteriormente. 
  
  d. Salve com o nome de 08-Funcionário. 
"""

salario = float(input("Digite o salário do funcionário: "))

inss = salario * 0.11

ir = salario * 0.15

salario_liquido = salario - inss - ir

print(f"Salário Sem Desconto: R${salario:.2f}")
print(f"Desconto INSS: R${inss:.2f}")
print(f"Desconto IR: R${ir:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")