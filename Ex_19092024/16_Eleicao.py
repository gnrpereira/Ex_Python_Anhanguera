import matplotlib.pyplot as plt

y1 = [float(input(f"Digite o valor de Y1 para LEO22 (coordenada {i+1}): ")) for i in range(4)]
y2 = [float(input(f"Digite o valor de Y2 para RENATO10 (coordenada {i+1}): ")) for i in range(4)]
y3 = [float(input(f"Digite o valor de Y3 para CORONEL22 (coordenada {i+1}): ")) for i in range(4)]
x = [1, 2, 3, 4]

plt.plot(x, y1, marker='o', linestyle='-', color='b', label='LEO22')
plt.plot(x, y2, marker='o', linestyle='-', color='r', label='RENATO10')
plt.plot(x, y3, marker='o', linestyle='-', color='g', label='CORONEL22')

plt.xlabel('Coordenadas X')
plt.ylabel('Intenção de Votos')
plt.title('Gráfico de Intenção de Votos')
plt.legend()
plt.grid(True)
plt.show()
