"""
Exercício 11:
 Crie um programa que vai solicitar ao usuário a digitação de um e-mail e de uma senha, 
  o usuário somente tem 3 tentativas para acertar a senha, que é “123456”, caso ele não 
  acerte na primeira tentativa o sistema tem que avisar pra ele que ele errou a senha, e 
  que ainda faltam 2 tentativas antes que ele bloqueie o sistema, permita que ele digite 
  novamente a senha, caso ele erre, avise ao usuário que ele errou novamente a senha 
  e que agora ele só tem uma tentativa para acertar, permita que ele digite novamente 
  a senha, caso ele erre, avise ao usuário que ele errou pela 3 vez e que o sistema será 
  bloqueado. Caso ele acerte a senha digitada em qualquer alternativa, o sistema ira 
  imprimir “Parabéns senha certa” e não vai mais precisar digitar a senha. Salve como o 
  nome de 11-Login3x.
"""

senha_correta = "123456"

email = input("Digite o seu e-mail: ")

tentativas = 3

while tentativas > 0:
    senha = input("Digite a sua senha: ")
    
    if senha == senha_correta:
        print("Parabéns, senha certa!")
        break
    else:
        tentativas -= 1
        
        
        if tentativas > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
        else:
            print("Você errou pela 3ª vez. O sistema será bloqueado.")