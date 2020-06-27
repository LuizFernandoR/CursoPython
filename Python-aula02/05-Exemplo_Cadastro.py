lista_alunos=[]

for i in range(2):
dict_aluno = {}
dict_aluno['nome'] = input('Digite o nome:')
dict_aluno['sobrenome'] = input('Digite o sobrenome: ')
dict_aluno['idade'] = input('Digite sua idade:')
lista_alunos.append(dixt_aluno)
for a in lista_alunos:
    print('Usuario cadastrados:',a['nome'],a['sobrenome'],a['idade'])