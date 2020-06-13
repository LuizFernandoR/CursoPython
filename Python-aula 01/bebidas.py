print('*'*10,'Bebidas','*'*10)
print('\n')
nome:input('Digite seu nome:')
idade:int(input('Digite sua idade:'))

if idade >= 18:
    bebida:input('Digite qual bebida você deseja: ')
else:
    print('Compranão permitida')
print('\n')
print('Nome do cliente:',nome,"Compra:",bebida)