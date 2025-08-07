#ALUNO: Roberto Araujo Batista, Matricula: 20251014050041
#ALUNO: Ryan Guilherme Costa De Moura, Matricula: 20242014050039
#PROFESSOR: Galileu Batista, CURSO: redes de computadores 2025.1, IFRN

'''
primeira parte:
1) (4 pontos) Faça um programa que permita o cadastramento de MAC adresses
vinculados a um CPF. O seu programa suportar as seguintes operações: a) cadastrar
CPF; b) adicionar MAC address a um CPF; c) remover um MAC address de um
CPF; d) remover o CPF (só permitir se não existirem MAC addresses vinculados);
e) listar os CPF cadastrados; f) listar os MAC adresses vinculados a um CPF; 


segunda parte:
g) salvar o “banco de dados” em um arquivo (perguntar o nome do arquivo);
h) ler o “banco de dados” de um arquivo (perguntar o nome do arquivo). 
Em todas as operações que requerem entrada de CPF e MAC adresses, valide-os
'''

'''
"banco de dados" será =
{
    cpf : [mac adress1, mac adress2, mac adress3]
    08333839495 : ['00:1A:2B:3C:4D:5E', '0-1A-2B-3C-4D-5E']
}
'''
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
    


   

    

'''
    if len(cpf) != 11: # Se o cpf tiver mais, ou menos, que 11 dígitos retorna False.
        print('O cpf só pode ter 11 dígitos. ex: 12345678901. ')
        return False
    if cpf.isnumeric() == False:
        print('O cpf só pode conter números.')
        return False
    
    soma = 0 # -- > necessária para os dígitos verificadores
'''

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
        input('')
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
        pos = 0
        while pos < len(dados[cpf]):
            print(f'{pos}. {mac}')
            pos = pos +1


# =========================================================================================================================
# Área do arquivo
import json

def salvar_banco(banco):
    
    try:
        with open(nome_arquivo, 'w') as arq:# -- >abre e fecha arquivo em modo write (criando ele no processo)
            for cpf, macs in banco.items():
                linha = cpf + ':' + ','.join(macs) + '\n' #
                arq.write(linha)
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


#=======================================================================
'''
EXEMPLO DE CÓDIGO
dados = dict()
cpf = '083338384895'
dados[cpf] = ['00:1A:2B:3C:4D:5E']
dados[cpf] = dados[cpf] + ['0-1A-2B-3C-4D-5E']

print(dados)
'''
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
    except:
        print('comando inválido')


    print(dados)
    #as funções irão atribuir um novo valor para a variável global
    if menu == 0:
        break
    if menu == 1:
        cpf = input('digite o cpf:')
        if cpf_valido(cpf) == True:
            cadastrar_cpf(dados)
        
        
    elif menu == 2:
        cpf = input('digite o cpf:')
        if cpf in dados:
            remover_cpf(dados)

    elif menu == 3:
        listar_cpf(dados)

    elif menu == 4:
        cpf = input('digite o cpf:')
        if cpf_valido(cpf):
            mac = input('digite o mac a ser adicionado: \n')
            adicionar_mac(dados)
        
    elif menu == 5:
        cpf = input('digite o cpf:')
        if cpf in dados:
            remover_mac()

    elif menu == 6:
        cpf = input('Digite o cpf: ')
        if cpf_valido(cpf):
            listar_mac()

    elif menu == 7:
        nome_arquivo = input('Digite o nome do arquivo para salvar (ex: dados.json): ')
        salvar_banco(dados)

    elif menu == 8:
        nome_arquivo = input('Digite o nome do arquivo para carregar (ex: dados.json): ')
        carregar_banco(dados)


    else:
        print('essa opção não existe')

# =========================================================================================================================