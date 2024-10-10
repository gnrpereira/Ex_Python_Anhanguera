tentativas = 0
while True:
    senha = input("Digite uma senha (deve conter dois '#'): ")
    tentativas += 1
    contador = 0
    for caractere in senha:
        if caractere == '#':
            contador += 1
    if contador >= 2:
        print(f"Senha válida! Foram necessárias {tentativas} tentativas.")
        break
