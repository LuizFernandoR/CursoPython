print('='*10,'Vendas de bebidas alcoolicas','='*10)
nome= input('Digite seu nome: ')
idade= input('Digite sua idade: ')

if idade < 18:
    print('Venda não permitia.')
elif idade >= 18:
    bebida= input('Qual bebida vôce deseja:')

print('Nome do cliente:',nome,'Bebida comprada:',bebida)


