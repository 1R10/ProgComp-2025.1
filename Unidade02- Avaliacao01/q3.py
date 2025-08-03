# Aluno: Ryan Guilherme Costa de Moura; 20242014050039
# =====================================================================================================
# Checklist
#
#   Lista....................NOK
#   Tratamento de erros......NOK
#     --> Tamanho............NOK
#     --> Palavra válida.....NOK
#     --> Tentativas.........NOK...?
#   Cores.................... OK
#   Tratamento de cores...... OK
#   Encerramento por pontos..NOK


# =====================================================================================================
# Parte de gerenciamento de palavras

import random


palavras = ( 
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)


segredo_1 = palavras[random.randint(0,len(palavras))] # Escolhe do index 0 ao fim da lst.
segredo_2 = palavras[random.randint(0,len(palavras))]

while segredo_2 == segredo_1: # Caso as palavras sejam iguais, é gerado um looping até não serem mais.
    segredo_1 = palavras[random.randint(0,len(palavras))]
print(segredo_1, segredo_2)

# =====================================================================================================
# Cores:

f_verde    = '\033[42m' # Verde   = Letra certa, lugar certo
f_amarelo  = '\033[43m' # Amarelo = Letra certa, lugar errado
f_preto    = '\033[40m' # Preto   = Letra não existente
padrao     = '\033[0m'  # Resetar



def formatar(palavra):
    for fundo, letra, padrao in palavra:
        print(f'{fundo}{letra}{padrao}', end='')
    

# =====================================================================================================
# Tentativas:

tentativas = 0

d_tentativas = {1:'Impossível',
                2:'Ninja',
                3:'Impressionante',
                4:'Interessante',
                5:'Pode melhorar',
                6: 'Foi por pouco',
                7:f'Palavras: {segredo_1}, {segredo_2}'}


# =====================================================================================================
# Parte principal:

l_segredos = []
while tentativas != 7:
    l_palavra = [[],[]] # resetar toda vez para a palavra não entrar na outra lista novamente.
    while True:
        termo = (input('Escreva uma palavra de 5 dígitos: ')).upper() # Pede o termo.
        if len(termo) == 5 and termo.isalpha() and termo in palavras:
            break
        else:
            print('Termo inválido.')

        
    
#   --------------------------------------------------------------------------------
    # Vai comparar letra por letra e salvar numa lista.
    for let in range(len(termo)): 
        if termo[let] == segredo_1[let]:
            l_palavra[0].append((f_verde, termo[let], padrao))

        elif termo[let] in segredo_1:
            l_palavra[0].append((f_amarelo, termo[let], padrao))

        else:
            l_palavra[0].append((f_preto, termo[let], padrao))

    print(' ', end='')

    for let in range(len(termo)):
        if termo[let] == segredo_2[let]:
            l_palavra[1].append((f_verde, termo[let], padrao))

        elif termo[let] in segredo_2:
            l_palavra[1].append((f_amarelo, termo[let], padrao))

        elif termo[let] not in segredo_2[let]:
            l_palavra[1].append((f_preto, termo[let], padrao))
#   ---------------------------------------------------------------------------------    
    formatar(l_palavra[0])
    print(' ', end='')
    formatar(l_palavra[1])
    print('\n'*2)












































    tentativas += 1
print(f'{d_tentativas[tentativas]}')



# =====================================================================================================
'''

[('\x1b[42m', 'G', '\x1b[0m'),
('\x1b[42m', 'E', '\x1b[0m'),
('\x1b[42m', 'N', '\x1b[0m'), 
('\x1b[42m', 'I', '\x1b[0m'),
('\x1b[42m', 'O', '\x1b[0m')] 
- 
[('\x1b[40m', 'G', '\x1b[0m'),
('\x1b[42m', 'E', '\x1b[0m'), 
('\x1b[42m', 'N', '\x1b[0m'), 
('\x1b[40m', 'I', '\x1b[0m'), 
('\x1b[42m', 'O', '\x1b[0m')]

'''