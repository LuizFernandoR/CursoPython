lista = []
opcao = ''
resposta = 0
for i in range(5):
    entrada=int(input('Digte um número: '))
    lista.append(entrada)
print(lista)

opcao= input('Deseja alterar algum elemento?S/N: ')
if opcao == 's':
    numero_alterar=int(input('Qual número deseja alterar na lista: '))
    alterar=int(input('Digite um número para alterar na lista: '))
for i in lista:
    if i == numero_alterar:
        lista.remove(numero_alterar)
        lista.append(alterar)
        print('nome ')
        print('numeros')


    



    


