#ALUNO: Roberto Araujo Batista, Matricula: 20251014050041
#ALUNO: Ryan Guilherme Costa De Moura, Matricula: 20242014050039
#PROFESSOR: Galileu Batista, CURSO: redes de computadores 2025.1, IFRN
# =========================================================================================================================
# Área do CPF
from cpf import cpf_valido

def cadastrar_cpf(banco):
    global dados
    banco = dados

    #requisitos do cpf: ter 11 dígitos
    #se for a entrada de um inteiro ele corta o 0 inicial
    

    if cpf in banco.keys():
        print(f'esse cpf já está cadastrado no banco de dados.')
        input('pressione enter')
    else:
        input(f'pronto, {cpf} cadastrado \npressione enter para seguir no menu principal')
        banco[cpf] = []
        return banco
    

def formatar_cpf():
    global cpf
    cpf = cpf.replace(".", "").replace("-", "")
    print(cpf)
    return cpf
    

def remover_cpf(banco):
    #remover cpf apenas se a lista estiver vazia
    global dados
    
    if cpf in dados.keys():
        if dados[cpf] == []: #se a lista de mac adrresses estiver vazia, você pode excluir cpf
            
            while True:
                try:
                    opcao = int(input(f'você tem certeza que deseja remover esse cpf? \n1.Sim\n2.Não\nEscolha: '))
                    if opcao == 1:
                        del dados[cpf]
                        return dados
                    
                    elif opcao == 2:
                        print('operacao cancelada')
                        break
                    else:
                        print('escolha uma opcao válida')
                except:
                    print('erro de digitação')
        else:
            print('Para excluir o cpf, você precisa excluir os endereços MAC vinculados a ele')
    else:
        print('Esse CPF não existe no banco de dados')

def listar_cpf(dados):
    print('lista de CPF no banco de dados: ')
    if len(dados) == 0:
        print('a lista está vazia')
    else: 
        for cpf in dados.keys():
            print(cpf)
        input('pressione enter para voltar ao menu principal')    


# =========================================================================================================================
# Área do Mac
        

def adicionar_mac(banco):
    global dados

    if cpf in dados.keys():
        print(dados[cpf])

        dados[cpf] = dados[cpf] + [mac]
        print(dados[cpf])
        input('Pressione enter para continuar.')
    else:
        input('esse cpf não está no banco de dados, pressione enter para voltar ao menu principal')



def remover_mac():
    global dados
    
    
    #exibir os macs do cpf
    pos = 0
    while pos < len(dados[cpf]):
        mac = dados[cpf][pos]
        print(f'{pos}. {mac}')
        pos = pos +1
    pos = int(input('Qual mac você deseja remover?'))

    del dados[cpf][pos]
    print(dados[cpf])




def listar_mac():
    global dados
    
    
    if dados[cpf] == []:
        print('a lista está vazia')
    #exibir os macs do cpf
    
    else:
        print('Macs cadastrados no cpf:')
        pos = 0
        while pos < len(dados[cpf]):
            print(f'{pos}. {mac}')
            pos = pos +1

def mac_valido(mac: str):
    #EX mac valido -- > 00:1B:C9:4B:E3:57
    if type(mac) != str:
        input('mac inválido(Não str).\nPressione enter para continuar')
        return False
    mac = mac.replace(':', '')
    if mac.isalnum() == False:
        input('mac inválido.(Não é alphanumérico)\nPressione enter para continuar.')
        return False
    
    
    return True

# =========================================================================================================================
# Área do arquivo


def salvar_banco(banco):
    
    try:
        with open(nome_arquivo, 'w') as arq:# -- >abre e fecha arquivo em modo write (criando ele no processo)
            for cpf, macs in banco.items():
                linha = cpf + ':' + ','.join(macs) + '\n' # -- > Formata a linha em um "dict" usando   
                arq.write(linha) # -- > escreve as linhas no arquivo
        print(f'Banco de dados salvo com sucesso em "{nome_arquivo}"')
    except:
        print(f'Erro ao salvar o arquivo.')     


def carregar_banco(banco):
    try:
        with open(nome_arquivo, 'r') as arq: # -- >abre e fecha arquivo em modo read
            banco.clear() # --> limpar o atual pra receber o novo banco
            for linha in arq:
                linha = linha.strip()
                if ':' in linha:
                    cpf, macs_str = linha.split(':', 1)
                    macs = macs_str.split(',') if macs_str else []
                    banco[cpf] = macs
        print(f'Banco de dados carregado com sucesso de "{nome_arquivo}"')
    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
    except:
        print(f'Erro ao ler o arquivo.')


# =========================================================================================================================
# Código principal


dados = dict() #dicionario que irá receber o banco de dados

while True: 
    try: 
        #criar primeiro um menu para saber para onde o usuário irá e por onde começar a programar

        #cadastrar cpf, remover cpf, listar cpf, adicionar mac, remover mac, listar mac
        print('''
        MENU PRINCIPAL
        1.Cadastrar CPF
        2.Remover CPF
        3.Lista de CPF cadastrados
        4.Adicionar um Mac
        5.remover um Mac
        6.Listar Mac por CPF
        7.Salvar banco de dados em arquivo
        8.Ler banco de dados de um arquivo
        0.Sair
        ''')
        menu = int(input('digite uma opção: '))
    except ValueError:
        print('Escolha um número.')

    except:
        print('comando inválido')


        print(dados)
        #as funções irão atribuir um novo valor para a variável global
        if menu == 0:
            break
        if menu == 1:
            cpf = input('digite o cpf:')
            formatar_cpf()
            if cpf_valido(cpf) == True:
                cadastrar_cpf(dados)
            
            
        elif menu == 2:
            cpf = input('digite o cpf:')
            formatar_cpf(cpf)
            if cpf in dados:
                remover_cpf(dados)

        elif menu == 3:
            listar_cpf(dados)

        elif menu == 4:
            cpf = input('digite o cpf:')
            
            if cpf_valido(cpf):
                mac = input('digite o mac a ser adicionado: \n')
                if mac_valido(mac):
                    adicionar_mac(dados)

            else:
                input('cpf inválido.\n Pressione enter para continuar.')
            
        elif menu == 5:
            cpf = input('digite o cpf:')
            formatar_cpf(cpf)
            if cpf in dados:
                remover_mac()

        elif menu == 6:
            cpf = input('Digite o cpf: ')
            
            if cpf in dados.keys():
                listar_mac()
                input('Pressione enter para continuar.')
            else:
                input('cpf inválido!\nPressione enter para prosseguir.')
                

        elif menu == 7:
            nome_arquivo = ''
            while not(nome_arquivo.isalnum()):
                nome_arquivo = input('Digite o nome do arquivo para salvar (ex dados): ')
            salvar_banco(dados)

        elif menu == 8:
            nome_arquivo = input('Digite o nome do arquivo para carregar (ex: Banco1): ')
            carregar_banco(dados)


        else:
            print('essa opção não existe')

# =========================================================================================================================
