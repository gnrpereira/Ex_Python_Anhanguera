tentativas = 0
while True:
    senha = input("Digite uma senha (deve conter dois '#'): ")
    tentativas += 1
    if senha.count('#') >= 2:
        print(f"Senha válida! Foram necessárias {tentativas} tentativas.")
        break