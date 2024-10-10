import mysql.connector

connection = mysql.connector.connect(
    user='govalp68_aluno', password='Pitagoras@2024',
    host='srv236.prodns.com.br', database=' govalp68_pitagoras'
)

mycursor = connection.cursor()

nome = input("Digite o seu nome")
endereco = input("Digite o seu endereço")
numero = input("Qual número da sua casa?")
bairro = input("Qual é o seu bairro?")
cidade = input("Qual é a sua cidade?")
estado = input("Qual é o seu estado?")
cep = input("Qual é o seu CEP?")

sql = "INSERT INTO clientes (nome, endereco, numero, bairro, cidade, estado, cep) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (nome, endereco, numero, bairro, cidade, estado, cep)

mycursor.execute(sql, val)

connection.commit()

print(mycursor.rowcount, "inserções")

resultados = mycursor.fetchall()

print(resultados)

mycursor.close()
connection.close()