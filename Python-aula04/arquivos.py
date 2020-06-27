# R read ler arquivo
# A append adicionar nova informação
# W write escrever arquivo, apaga o arquivo pronto.
# lista.index(parametro) busca pela posição
#upper()  retorna a letra  maiuscula
arquivo = open('python-Aula04/cadastro.txt','r')
lista_cadastro = []
for pessoa in arquivo:
    pessoa = pessoa.strip() 
    pessoa = pessoa.split(';') # separador
    lista_cadastro.append(pessoa)

arquivo.close()
mulher = []
for pessoa in lista_cadastro:
    if pessoa[3] == 'f':   
        mulher.append(pessoa)

arquivo = open("python-Aula04/mulher.txt",'w')
for pessoa in mulher:
    pessoa_str = ';'.join(pessoa) +'\n'
    arquivo.write(pessoa_str)
arquivo.close()

homem = []
for pessoa in lista_cadastro:
    if pessoa[3] == 'm':
        homem.append(pessoa)

arquivo = open('Python-aula04/homem.txt','w')
for pessoa in homem:
    homem_str = ';'.join(pessoa) + '\n'
    arquivo.write(homem_str)
arquivo.close()


    # if '1'in pessoa[0] or 'A' in pessoa[1]:
    #     print(pessoa)



