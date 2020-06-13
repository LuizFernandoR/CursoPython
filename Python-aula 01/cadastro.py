print('*'*15,'Cadastro do cliente','*'*15)
print('\n')
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
print('\n')
#Impressão multiplas linhas
#Interpolação de strings 'f' + {}
print(f'''==== Dados coletado ====

           Nome do cliente:{nome}
           Sobrenome:{sobrenome}
           Idade do cliente:{idade}
           ''')
print('\n')
print('-'*10,'FIM','-'*10)