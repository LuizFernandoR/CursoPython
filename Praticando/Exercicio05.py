continuar = 's'
compra= 0
cel=0
rel=0
ten=0
ocl=0
gin= 0
pcnt=0
valor_total= 0
while continuar =='s':
    print('''
    ----MENU----
   COD        PRODUTO          PREÇO
    ^            ^               ^
    1-------- CELULAR -------- 3000,00
    2-------- RELÓGIO -------- 900,00   
    3-------- TENIS ---------- 450,00
    4-------- ÓCULOS --------- 475,00
    5-------- GIN ------------ 110,00
    
--ESCOLHA O PRODUTO--
''')
    opcao = int(input('Digite o código do produto: '))
    if opcao == 1:
        compra= compra + 3000
        cel=  1
        pcnt+= cel * 10
    elif opcao == 2:
        compra= compra + 900
        rel=  1
        pcnt+= rel * 10
    elif opcao == 3:
        compra = compra + 450
        ten = 1
        pcnt+= ten * 10
    elif opcao == 4:
        compra = compra + 475
        ocl =  1
        pcnt+= (ocl * 10
    elif opcao == 5:
        compra = compra + 110
        gin =  1
        pcnt+= gin * 10
    
    valor_total += (compra * pcnt) / 100
    continuar = input('Deseja continuar comprando? S/N: ')
    if continuar == 's':
        continue
    else:
        print('Valor total com o desconto: ')
        

    

        

        
    
     
