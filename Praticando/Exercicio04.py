lista = [1,2,30,4,5,6,7,8,95,10,11,12,13,55,15,16,10,18,19,20]
num_maior = -99999
for i in lista:
    if i > num_maior:
        num_maior = i
calculo= sum(lista)/num_maior
print('Maior número:',num_maior)
print('Soma da lista e divisão pelo maior número:',calculo)

    

    
