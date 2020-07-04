lista = [[],'oi', 'tchau',1.98,1,[1,2,3],{'agua':123},(),'fim']
for i in lista:
    if type(i)== str:
        print('tipo:  01' '- sting')
    elif type(i)== int:
        print('tipo:  02' '- inteiro')
    elif type(i)== float:
        print('tipo:  03' '- real')
    elif type(i)== list:
        print('tipo:  04' '- lista')
    elif type(i)== tuple:
        print('tipo:  05' '- tupla')
    elif type(i)== dict:
        print('tipo:  06' '- dicionário')
print(len(lista))