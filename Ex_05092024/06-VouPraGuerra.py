"""
Exercício 06:
  Faça um programa que pergunte ao aluno o sexo dele. Se o sexo dele for “F” o programa 
  deve avisar ao aluno “Você não precisa se alistar”, mas se o sexo for “M” você deve 
  perguntar a idade desse aluno. Se o aluno tiver menos que 18 anos, o programa vai 
  imprimir que ele foi “Dispensado”, porém se ele tiver idade de 18 anos ou superior até 
  50 anos, o programa deve informar “Você foi selecionado para ir para a Ucrânia”,  caso   
  a idade seja maior que 51 anos, avise “Você vai para Israel”. Salve como 06
  VouPraGuerra.
"""

sexo = input("Digite o seu sexo - M para Masculino - F para Feminino: ")


if sexo == "F" or sexo == "f":
  print("Você não precisa se alistar.")
  
elif sexo == "M" or sexo == "m":
  idade = int(input("Digite a sua idade: "))
  
  if idade < 18:
    print("Você foi dispensado")
  elif 18 <= idade <= 50:
    print("Você foi selecionado para ir a Ucrania")
  elif idade > 51:
    print("Você vai para Israel")
