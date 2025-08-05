'''
3) Faça um programa que implementa o termo (www.term.ooo) na sua
versão dueto. Nessa versão existem duas palavras a serem descobertas. Em cada
rodada o usuário informa uma palavra, que é confrontada com as duas a serem
descobertas. O usuário vence quando descobre as duas palavras em até sete
tentativas. Mostre as palavras com as mesmas cores do referido sítio e crie uma lista
com as palavras válidas (se o usuário digitar outra, não será aceita).
'''


# Aluno: Ryan Guilherme Costa de Moura; 20242014050039
# Aluno: Roberto Araujo Batista; 20251014050041
# =====================================================================================================
# Checklist
#
#   Tratamento de erros......NOK
#     --> Palavra válida.....NOK
#     --> Palavra Repetida....OK
#     --> Tamanho.............OK
#     --> Tentativas..........OK
#   Cores.....................OK
#   Tratamento de cores.......OK
#   Encerramento..............OK
    
'''sites_palavras = ( # Sites, do próprio termo, para validar as palavras.
                    'https://raw.githubusercontent.com/fserb/pt-br/refs/heads/master/palavras'             ,
                    'https://raw.githubusercontent.com/fserb/pt-br/refs/heads/master/conjuga%C3%A7%C3%B5es',
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/verbos'                          ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/paises'                          ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/municipios'                      ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/estados'                         ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/dicio'                           ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/data'                            ,
                    'https://github.com/fserb/pt-br/raw/refs/heads/master/continentes'                      )'''


import termoo #import do programa feito pelo professor com as palavras a serem selecionadas como segredo

# =====================================================================================================
#FUNÇÕES
def selecionar_segredos():
#variáveis que serão para comparação
    segredo_1 = termoo.palavras() # Escolhe do index 0 ao fim da lst.
    segredo_2 = termoo.palavras()

    while segredo_2 == segredo_1: # Caso as palavras sejam iguais, é gerado um looping até não serem mais.
        segredo_2 = termoo.palavras()
    return segredo_1, segredo_2


# Vai comparar letra por letra, colorir e salvar numa lista (cada palavra).
def comparar_palavra(entrada, segredo):
    palavra = []
    for letra in range(len(entrada)): 
        if entrada[letra] == segredo[letra]: # se letra está na pos certa, fica verde
            palavra.append((f_verde, entrada[letra], padrao))

        elif entrada[letra] in segredo: # se letra na palavra, fica amarelo
            palavra.append((f_amarelo, entrada[letra], padrao))

        else: # não muda
            palavra.append((f_preto, entrada[letra], padrao))
    return palavra

#vai exibir a palavra na formatação correta
def exibir(palavra): # Puxa cada lista que vai ser criada com a palavra e cor e formata num print/for.
    for fundo, letra, padrao in palavra: #como a lista tem 3 elementos, o for irá para de 3 em 3
        print(f'{fundo}{letra}{padrao}', end='')






#VARIÁVEIS
# =====================================================================================================
# Cores:

f_verde    = '\033[42m' # Verde   = Letra certa, lugar certo
f_amarelo  = '\033[43m' # Amarelo = Letra certa, lugar errado
f_preto    = '\033[40m' # Preto   = Letra não existente
padrao     = '\033[0m'  # Resetar

# =====================================================================================================
# Tentativas:

tentativas = 0

def func_tentativas(tentativas):    
    d_tentativas = { # Dict para formatar a mensagem final com base na quantidade de tentativas.
                    1:'Impossível'    ,
                    2:'Ninja'         ,
                    3:'Impressionante',
                    4:'Interessante'  ,
                    5:'Pode melhorar' ,
                    6: 'Foi por pouco',
                    7:f'Palavras: {segredo_1}, {segredo_2}'}
    return d_tentativas[tentativas]


# =====================================================================================================


# CÓDIGO MAIN()

segredo_1, segredo_2 = selecionar_segredos()  #variáveis que o usuário deve adivinhar
print(segredo_1, segredo_2)

l_resposta = [[segredo_1], [segredo_2]]
l_segredos = [[], []]

entradas_palavras = list()

while tentativas != 7:
    l_palavra = [[],[]] # resetar toda vez para a palavra não entrar na outra lista novamente.
    while True:
        print(f'você tem {tentativas+1}/7 chances')
        termo = (input('Escreva uma palavra de 5 letras: ')).upper() # Pede o termo.

        if (len(termo) == 5) and (termo.isalpha()) and not(termo in entradas_palavras): #verifica se é uma letra do alfabeto e se é repetida
            entradas_palavras = entradas_palavras + [termo]
            break
        else:
            print('Termo inválido.')


    tentativas += 1 # Palavra válida = tentativa gasta.
    
#   --------------------------------------------------------------------------------
    #l_palavra são variáveis apenas para exibição de saída    
    l_palavra[0] = comparar_palavra(termo, segredo_1)
    l_palavra[1] = comparar_palavra(termo, segredo_2)
    #exibição com as cores corretas
    exibir(l_palavra[0])
    print(' ', end='')
    exibir(l_palavra[1])
    print('\n'*2)



# ------------------------------------------------------------------------------------

#   condição de vitória: se as listas forem iguais o jogo acaba.
    if termo == segredo_1:
        l_segredos[0].append(termo)
    if termo == segredo_2:
        l_segredos[1].append(segredo_2)
    if l_segredos == l_resposta:
        break

print(f'\033[44m{func_tentativas(tentativas)} {padrao}')