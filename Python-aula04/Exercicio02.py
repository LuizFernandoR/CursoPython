notas = [2,5,10,20,50,100]
valor= float(input('Valor: '))
cont= 0
for i in notas:
    if valor == i:
        cont+= 1
        print('Quantidade de notas:',cont,'valor:',valor)
        break




