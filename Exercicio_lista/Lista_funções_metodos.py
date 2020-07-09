# n = [1,2,3,4,5]
# l = ['a','b','c','d','e']
# print({1 in n})
# print({'h' in l})

# print({'a' in 'amem'})
# h = [1,2,3]
# i = [4,5,6]
# print(id(h))
# print(id(i))

lista = [1,2,3]
l = lista
# print(f'id(lista): {id(l)}')
# print(f'lista == l: {l==lista}' )
# print(f'lista is l: {l is lista}')
# print(f'Minha lista é: {lista}')
nl = lista.copy()
print(f'nl={id(nl)}')
print(f'l= {id(l)}')
print(f'id n == id nl: {nl is l}')
