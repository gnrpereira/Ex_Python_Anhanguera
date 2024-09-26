"""
Exercício 13:
   Crie um aplicativo que vai perguntar o nome do Aluno, a idade, e o Sexo, depois vai 
    perguntar a nota da prova e o número de faltas. Baseado nessas informações o 
    aplicativo vai calcular se o aluno passou de ano ou não nessa disciplina. Para saber isso 
    você deve levar em consideração o seguinte: 
    
    a. Se ele tiver mais que 40 pontos ele já está aprovado, independentemente do 
    número de faltas que ele tiver. 
    
    b. Caso ele tenha 40 pontos ou menos vamos ter que verificar o número de faltas 
    que ele possui. Caso ele possua menos de 10 faltas ele está aprovado, caso 
    contrário ele está reprovado 
    
    c. Salve com o nome 13-AprovadoOuNao.
"""

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
sexo = input("Digite o sexo do aluno (M/F): ")
nota = float(input("Digite a nota da prova: "))
faltas = int(input("Digite o número de faltas: "))

if nota > 40:
    resultado = "Aprovado"
else:
    if faltas < 10:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

print(f"Aluno: {nome}, Idade: {idade}, Sexo: {sexo}")
print(f"Nota: {nota}, Faltas: {faltas}")
print(f"Resultado: {resultado}")