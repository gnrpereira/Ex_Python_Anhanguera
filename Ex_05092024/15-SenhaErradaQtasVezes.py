"""
Exercício 15:
   Escreva um aplicativo que pergunte a sua senha, depois você vai verificar se a senha 
    digitada foi “Senh@24”, caso não for essa senha que ele digite, você deve informar 
    para ele que a senha está errada e que ele pode digitar mais uma vez a senha. Somente 
    vai parar de perguntar a senha quando ele digitar a senha corretamente. Nesse caso 
    depois que ele acertar a senha você deve escrever a mensagem “Voce errou X vezes a 
    senha antes de digitar ela corretamente”. Onde X será número de tentativas erradas. 
    Salve o aplicativo com o nome de 15-SenhaErradaQtasVezes.  
"""

senha_correta = "Senh@24"

tentativas_erradas = 0

while True:
    senha = input("Digite a sua senha: ")
    
    if senha == senha_correta:
        print(f"Você errou {tentativas_erradas} vez(es) antes de digitar a senha corretamente.")
        break 
    else:
        tentativas_erradas += 1 
        print("Senha errada. Tente novamente.")