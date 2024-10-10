import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 8, 6, 9]

plt.plot(x1, y1, marker='o', linestyle='-', color='b')
plt.plot(x2, y2, marker='o', linestyle='-', color='r')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Gráfico de Linha')
plt.grid(True)
plt.show()
