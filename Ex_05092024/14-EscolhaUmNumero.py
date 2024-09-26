"""
Exercício 14:
   Crie um aplicativo que você solicita para o usuário digitar um número de 1 a 4, depois 
    que ele digitar, você deve testar o número que ele digitou: 
    • Se for o número 1, você deve imprimir “Você digitou 1, Seja bem vindo” 
    • Se for o número 2, você deve imprimir “Você digitou 2, muito bem” 
    • Se for o número 3, você deve imprimir “Você digitou 3, perfeito” 
    • Se for o número 4, você deve imprimir “Você digitou 4, Excelente” 
    • Se não for nenhum desses números você deve imprimir “Você não presta 
    atenção no que eu mandei você digitar”. 
    Salve esse aplicativo com o nome de 14-EscolhaUmNumero 
"""

numero = int(input("Digite um número de 1 a 4: "))

if numero == 1:
    print("Você digitou 1, Seja bem vindo")
elif numero == 2:
    print("Você digitou 2, muito bem")
elif numero == 3:
    print("Você digitou 3, perfeito")
elif numero == 4:
    print("Você digitou 4, Excelente")
else:
    print("Você não presta atenção no que eu mandei você digitar.")