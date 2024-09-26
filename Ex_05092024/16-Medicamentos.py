"""
Exercício 16:
   A rede de farmácias "Indiana" resolveu dar um aumento nos medicamentos e te 
    contrataram para desenvolver o programa que calculará os reajustes. Faça um 
    programa que recebe o valor do medicamento e o reajuste será de acordo com 
    seguinte critério, baseado valor do medicamento :  
    
    a. Medicamentos até R$ 249,99: aumento de 20%  
    
    b. Medicamentos até R$ 250,00 ate 289,99: aumento de 15% 
    
    c. Medicamentos até R$ 290,00 até 349,99: aumento de 10% 
    
    d. Medicamentos acima de 350,00 inclusive: aumento de 5% 
   
    Após o aumento ser realizado, informe na tela: O valor do medicamento, o valor do 
    reajuste, o percentual do ajuste e o valor do medicamento reajustado. Salve com o nome 
    de 16-Medicamentos. 
"""

valor_medicamento = float(input("Digite o valor do medicamento: R$ "))

if valor_medicamento <= 249.99:
    percentual_reajuste = 20
elif valor_medicamento <= 289.99:
    percentual_reajuste = 15
elif valor_medicamento <= 349.99:
    percentual_reajuste = 10
else:
    percentual_reajuste = 5

valor_reajuste = valor_medicamento * (percentual_reajuste / 100)

valor_reajustado = valor_medicamento + valor_reajuste

print(f"Valor do medicamento: R$ {valor_medicamento:.2f}")
print(f"Percentual de reajuste: {percentual_reajuste}%")
print(f"Valor do reajuste: R$ {valor_reajuste:.2f}")
print(f"Valor do medicamento reajustado: R$ {valor_reajustado:.2f}")