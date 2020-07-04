dinheiro = [100,50,20,10,5,2,0.5,0.25,0.1,0.05,0.01]
valor= float(input('Valor: '))
for pila in dinheiro:
    quantidade = valor // pila
    #valor = valor -(pila * quantidade)
    valor = round (valor % pila,2)
    print(f'dinheiro{pila} x {quantidade} = {pila*quantidade}')
        



