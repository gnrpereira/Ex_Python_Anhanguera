import mysql.connector

connection = mysql.connector.connect(
    user='govalp68_aluno', password='Pitagoras@2024',
    host='srv236.prodns.com.br', database=' govalp68_pitagoras'
)

mycursor = connection.cursor()

#sql.execute("INSERT INTO clientes nome, endereco, numero, bairro VALUES 'Gabriel Pereira', 'Rua Sandalo', 32, 'Ipe'")
#sql.execute("SELECT * FROM clientes WHERE nome = 'Gabriel'")

sql = "INSERT INTO clientes (nome, endereco) VALUES (%s, %s)"
val = ("Gabriel", "Rua Sandalo")

mycursor.execute(sql, val)

connection.commit()

print(mycursor.rowcount, "inserções")

mycursor.execute("SELECT * FROM clientes WHERE nome = 'Barbara'")

resultados = mycursor.fetchall()

print(resultados)

mycursor.close()
connection.close()