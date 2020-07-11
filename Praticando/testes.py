# texto= 'Luiz Fernando Reichert'
# texto= texto.replace('Luiz Fernando Reichert','Luana Pereira')
# print(texto)

# nome=input('Digite seu nome:')
# nome= nome.replace(nome,'Nome nulo')
# print(nome)

# lista=[10,'kk','55']

# for i in lista:
#     print(i,'-',lista)

# for i in lista:
#     print(i)
# ---------------------------------
# operacao= 's'

# while operacao == 's':
#     produto=input('Produto:')
#     valor_pdt=int(input('Valor do produto:'))
#     qtd_pdt=int(input('Quantidade do produto:'))

#     preco_total= valor_pdt * qtd_pdt
#     print('Pagamento dinheiro ou cartão?')
#     pagamento=(input('Dineheiro digite 1, cartão digite 2:'))

#     if pagamento == '1':
#         desconto = (preco_total * 10)  / 100 
#         preco_desconto= preco_total - desconto
#         print('Pagamento a vista tem 10% de desconto - este é o valor com o desconto',preco_desconto)
#     else:
#         print('total a pagar',preco_total)

#     print('Deseja fazer outa operação? s/n')
#     operacao= input('S/N')

# if operacao == 'n':
#     print('Fim operação!')

# nomes=[]
# qtd_hrs=[]
# valor_hrs=[]

# for i in range(3):
#     nome=input('Nome:')
#     nomes.append(nome)
#     qtd_hr=int(input('Quantidade horas:'))
#     qtd_hrs.append(qtd_hr)
#     valor_hr=float(input('Valor hora:'))
#     valor_hrs.append(valor_hr)
# print(nomes)
# print(qtd_hrs)
# print(valor_hrs)

# Declaração de funções

# def soma(a, b):

# tupla=(10,20,30,40,50,60,70)
# (tupla[2]) =10
# print(tupla)

# lista=[10,20,30,40,50,60,70]
# lista[2]=100
# print(lista)
# media = 0

# notas = [8,8,8,8]
# for i in notas:
#     media= media + i
# media_final= media / len(notas)

# print(media_final)
# ---------------------------------------------
# nomes= []
# funcoes = []
# def entrada():
#     nome = input('Digite seu nome:')
#     nomes.append(nome)
#     funcao = input('Digite sua fução na empresa:')
#     funcoes.append(funcao)


# opcao = ''
# while True:
#     opcao= input('Deseja cadastrar?S/N')
#     if opcao =='s':
#         entrada()
#     else:
#         print(nomes)
#         print(funcoes)
#         break

# lista= [1,2,3,4,5,6,7,8,9,10,12,13,
#         14,15,16,17,18,19,20]
# a_consultar = 0
# def consulta(lista):
#     a_consultar= int(input('Número a consultar: '))
# opcao = ''
# while True:
#     print('Deseja consultar lista?')
#     opcao = input('Digite opção S/N: ')
#     if opcao == 's':
#         consulta(lista)
#         for i in lista:
#             if i == a_consultar:
#                 print('Este número está na lista.',a_consultar)
#             else:
#                 print('Este número nõa esta na lista.')
#                 break
lista = [0,1,2,3,4,5,6]

print(min(lista))


