# list
# dict
# tuple
idade= 151
lista_idades=[18,19,50,41,25,36,58,57]
print(idade,'\n',lista_idades)

# Imprimindo um item especifico da lista

print(lista_idades[1])

# Removendo um item especifico da lista

lista_idades.remove(19)
print(lista_idades)

# Pop usa o index para excluir e o remove usa o valor que quer excluir
retorno_do_pop= lista_idades.pop(1)

print(lista_idades)
print(retorno_do_pop)

# Adicionando dados na lista

lista_idades.append(idade)
print(lista_idades)

# Mostrando o número de instancias do dado na lista

print(lista_idades.count(19))

# Mostrando o número totas de dados da lista

print(len(lista_idades))

# Fatiamento de lista.
# Imprimindo os três primeiros itens
print(lista_idades[:3]
# Inserindo dados em uma posição especifica

 lista_idades .insert (2,152)
 print(lista_idades)

 # Inserindo o número 153 apos o 152
 index= lista_idades.index(152)
 lista_idades.insert(index + 1,153)
 print(lista_idades)

