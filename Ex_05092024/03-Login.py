"""
Exercício 03:
 Fazer um programa que pergunte o login e a senha do usuário, depois o programa 
  devera testar se a senha digitada é “123456”, caso seja imprimir na tela SENHA 
  CORRETA, caso não seja, imprimir VOCÊ ERROU A SENHA. Salve com o nome de 03
  Login.
"""

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if senha == "123456":
  print("SENHA CORRETA")
else:
  print("VOCÊ ERROU A SENHA")

