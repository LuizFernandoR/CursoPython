arquivo = open('python-Aula04/cadastro.txt','r')
import matplotlib.pyplot as plt
lista_cadastro = []
for pessoa in arquivo:
    pessoa = pessoa.strip() 
    pessoa = pessoa.split(';') # separador
    lista_cadastro.append(pessoa)

arquivo.close()
mulher = 0
for pessoa in lista_cadastro:
    if pessoa[3] == 'f':   
        mulher = mulher+1
homem = 0
for pessoa in lista_cadastro:
    if pessoa[3] == 'm':
        homem= homem + 1
print(homem,mulher)


