# Aluno: Ryan Guilherme Costa de Moura; 20242014050039
# =====================================================================================================
# Checklist
#
#   Lista.....................OK
#   Tratamento de erros......NOK
#   Cores....................NOK
#   Tratamento de cores......NOK

def rodou():
    print('Código rodando...')

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
print(segredo_1)

# =====================================================================================================
# Cores

f_verde    = '\033[42m' # Verde   = Letra certa, lugar certo
f_amarelo  = '\033[43m' # Amarelo = Letra certa, lugar errado
f_preto    = '\033[40m' # Preto   = Letra não existente
padrao     = '\033[0m'  # Resetar


# =====================================================================================================
# Parte principal.
rodou()

tentativas = 7

while tentativas > 0:
    
    termo = (input('Escreva uma palavra de 5 dígitos: ')).upper() # Pede o termo.
    
    #l_palavras = [[],[]]

    for let in range(len(termo)):
        if termo[let] == segredo_1[let]:
            print(f_verde, termo[let], padrao, end='')

        elif termo[let] in segredo_1:
            print(f_amarelo, termo[let], padrao, end='')

        else:
            print(f_preto, termo[let], padrao, end='')







# =====================================================================================================
