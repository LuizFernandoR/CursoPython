def cadastrar_cliente():
    cod_cliente = int(input('Código do cliente: '))
    cpf_cliente = (input('CPF: '))
    nome_cliente = (input('Nome: '))
    dt_nasc_cliente = (input('Data de nascimento:'))
    estado = (input('Estado: '))
    cidade = (input('Cidade: '))
    cep = (input('Cep: '))
    bairro = (input('Bairro: '))
    rua = (input('Rua: '))
    num_casa = (input('Número da casa: '))
    complemento = (input('Complemento: '))

def cadastrar_Produtos():
    cod_bebida = int(input('Código da bebida: '))
    nome_bebida = input('Nome da bebida: ')
    tipo_bebida = input('Tipo da bebida: ')
    volume_bebida =  input('Volume da bebida: ')
    preco = int(input('Preço da bebida: '))

print(f'''
         MENU

    1 - CADASTRAR CLIENTE
    2 - CONSULTAR CLIENTE 
    3 - CONSULTAR PRODUTO
    4 - VER PRODUTOS CADASTRADO   
    5 - SAIR
 -------------------------------------
    ESCOLHA A OPÇÃO!   
  ''')
  opcao = int(input('Qual opção deseja? '))

