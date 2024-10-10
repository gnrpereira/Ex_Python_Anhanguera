while True:
    email = input("Digite um e-mail: ")
    if '@' in email:
        print("E-mail válido.")
        break
    else:
        print(f"O e-mail '{email}' não é válido, tente novamente.")
