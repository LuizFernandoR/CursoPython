import matplotlib.pyplot as plt

x= [i for i in range (1,7)]
y =[i for i in range (11,17)]
# mese =['Janeiro','Fevereiro','Março','Abril','maio','junho']
# valores= [105235, 107697, 110256, 108859, 109986]

plt.plot(x, y) # gráfico linha
plt.bar(x, y) # gráfico de barra
plt.scatter(x, y) # gráfico de pontos
plt.title ('Teste de reagente')
plt.xlabel ('Solvente')
plt.ylabel ('Produto resultante')

plt.show()
