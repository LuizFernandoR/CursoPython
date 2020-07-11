# from datetime import date, time, datetime, timedelta
# from dateutil.relativedelta import relativedelta
# from time import sleep, asctime, time

# sleep tempo em segundos contador,cronômetro

#print(date.today() - date(2020,8,1))

# data1 = date(2020,7,11)
# data2 = date(2020,10,23)
# #print(data1-data2)

# dt = data1 + relativedelta(days=+3,months=+2)
# print(dt.strftime("%d/%m/%Y"))

# a = time()
# print('Luiz')
# sleep(3)
# print('Fernando')
# print(f'{a:.2f}')

# mltp = lambda num1,num2 : num1 * num2
# print(mltp(5,5))

# divisao = lambda n1,n2 : n1 / n2
# print(divisao(10,2))

# lista = [1,2,3,4,5,6,7,8,9,10]

# nova_lista = list(map (lambda x: x*3,lista))
# print(nova_lista)

# tempo =  [i for i in range(25)]
# montante = lambda t ,valor=200 , i=10 : round (valor * (1 +i/100)**t,2)
# resultado = list(map(montante,tempo))
# print(tempo)
# print(resultado)

# lista = [i for i in range(31)]
# filtro = lambda x :True if(x%3) == 0 else False
# resultado = list(filter(filtro,lista))
# print(lista)
# print(resultado)

# from random import randint
# lista = [randint(0,10) for i in range(20)]
# print(lista)

# num = [randint(0,100)]
# print(num)

# from functools import reduce
# lista = [i for i in range(10)]
# funcao = lambda x,y : x + y
# print(lista)
# print(reduce(funcao,lista))