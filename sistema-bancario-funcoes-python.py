
historico_depositos = []
historico_sacados = []
movimentacoes = []
LIMITE_SAQUES = 3
quantidade_de_saques = 1
lista_usuarios = []
lista_contas = []



def main():

    while True:
        print('')
        print('-------------- MENU --------------')
        print('')
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Extrato')
        print('[4] Criar usuário')
        print('[5] Buscar usuário')
        print('[6] Criar CC')
        print('[7] Buscar CC')
        print('[0] Sair')
        print('')        
        main = input('=> Opção: ')        
       
        if main == '1':
            print('')  
            print('------------ DEPÓSITO ------------')
            print('')
            valor_deposito = int(input('Insira um valor: '))
            depositar(valor_deposito)  
          
        elif main == '2':
            print('')  
            print('------------- SAQUE --------------')
            print('') 
            if quantidade_de_saques > LIMITE_SAQUES:
                print('Não é possível realizar mais de 3 saques diários!')                
                continue
            elif sum(historico_depositos) - sum(historico_sacados) == 0:
                print('Você não tem recursos para saque!')                
                continue  
            else: 
                valor_saque = int(input('Insira um valor: ')) 
                sacar(valor_saque)                 

        elif main == '3':
            print('')  
            print('------------ EXTRATO -------------')
            print('') 
            extrato()
           
        elif main == '4':
            print('')  
            print('--------- CRIAR USUÁRIO ----------')
            print('')              
            usuario_cpf = input('Insira CPF: ')
            criar_usuario(usuario_cpf)        

        elif main == '5':
            buscar_usuario()
        
        elif main == '6':
            print('')  
            print('---------- CRIAR CONTA -----------')
            print('')              
            usuario_cpf = input('Insira CPF: ')            
            criar_conta(usuario_cpf)







        elif main == '7':
            buscar_conta()
        elif main == '0':
            break
        else:
            print('Selecione uma opção válida!')
            continue


def saldo():
    saldo_em_conta = sum(historico_depositos) - sum(historico_sacados) 
    print('')
    print('----------------------------------')
    print(f'Saldo em conta atual: R${saldo_em_conta:.2f}')
    print('----------------------------------')          

def depositar(valor_deposito): 
    if valor_deposito > 0:
        historico_depositos.append(valor_deposito)  
        movimentacoes.append(valor_deposito)    
        print('')
        print('Valor depositado com sucesso')
        saldo()
        main()                   
    else:
        print('')
        print('Inserir valor superior a 0!')
        print('')
        main()

def sacar(valor_saque):
    if valor_saque > 500:
        print('')
        print('Não é possível sacar valor superior a R$500,00!')
        print('')
        main()
    elif sum(historico_depositos) - sum(historico_sacados) < valor_saque:
        print('')
        print('Você não possui saldo em conta suficiente!')
        print('')
        main()     
    historico_sacados.append(valor_saque)    
    movimentacoes.append(int('-' + str(valor_saque)))
    print('')
    print('Valor sacado com sucesso!')
    saldo()    
    main()

def extrato():
    cont = 1
    for cada_deposito in movimentacoes:
        if cada_deposito < 0:
            cada_deposito = '-R$' + str(cada_deposito).replace('-','')
        else:
            cada_deposito = ' R$' + str(cada_deposito)
        print(f'{cont}ª movimentação: {cada_deposito}')
        cont +=1
    saldo()
    main()

def criar_usuario(usuario_cpf):    
    usuario_ja_cadastrado = True      
    lista_cpfs = []
    for usuario in lista_usuarios:        
        lista_cpfs.append(usuario['cpf']) 
    if usuario_cpf in lista_cpfs:
        usuario_ja_cadastrado = True                                  
    else:
        usuario_ja_cadastrado = False      
    if usuario_ja_cadastrado == False or len(lista_usuarios) == 0:
        usuario_nome = input('Nome: ')
        usuario_nascimento = input('Nascimento: ')
        usuario_endereço = input('Endereço: ')    
        lista_usuarios.append({'cpf': usuario_cpf, 'nome': usuario_nome, 'nascimento': usuario_nascimento, 'endereço': usuario_endereço})   
        print('')
        print('Usuários cadastrado com sucesso!') 
        print(lista_usuarios) 
        main()
    elif usuario_ja_cadastrado == True:        
        print('')
        print('Usuário já cadastrado!') 
        main()   
            
def criar_conta(usuario_cpf):    
    usuario_ja_cadastrado = True      
    lista_cpfs = []
    for usuario in lista_usuarios:        
        lista_cpfs.append(usuario['cpf']) 
    if usuario_cpf in lista_cpfs:
        usuario_ja_cadastrado = True                                  
    else:
        usuario_ja_cadastrado = False  
    if usuario_ja_cadastrado == False or len(lista_usuarios) == 0: 
        print('')
        print('Usuário não cadastrado!')        
        main()
    elif usuario_ja_cadastrado == True:
        numero_conta = '0001-'+ str(len(lista_contas)+1)
        lista_contas.append({'agencia': '0001', 'conta': numero_conta, 'cpf': usuario_cpf})  
        print('')
        print('Conta criada com sucesso!') 
        print(lista_contas)
        main()   
        



  
     




main()