import matplotlib.pyplot as plt

produtos = ['Trigo', 'Soja', 'Abacaxi', 'Mandioca', 'Tomate']
quantidades = [int(input(f"Digite a produção de {produto}: ")) for produto in produtos]

plt.bar(produtos, quantidades)
plt.xlabel('Produtos')
plt.ylabel('Quantidade Produzida')
plt.title('Produção Agrícola')
plt.show()
