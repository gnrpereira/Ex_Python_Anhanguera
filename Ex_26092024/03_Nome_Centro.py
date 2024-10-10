import mysql.connector

connection = mysql.connector.connect(
    user='govalp68_aluno', password='Pitagoras@2024',
    host='srv236.prodns.com.br', database=' govalp68_pitagoras'
)

sql = connection.cursor()

sql.execute("SELECT nome FROM clientes WHERE bairro = 'Centro'")

resultados = sql.fetchall()

print(resultados)

sql.close()
connection.close()