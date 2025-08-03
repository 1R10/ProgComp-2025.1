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

f_verde    = '\033[42m' # f = fundo
f_amarelo  = '\033[43m'
padrao     = '\033[0m' 


# =====================================================================================================
# Parte principal.

rodou()
while True:
    
    termo = (input('Escreva uma palavra de 5 dígitos: ')) # Pede o termo.
    
    l_termo = [0, 1, 2, 3, 4]
    for let in range(0,5):
        if termo[let] == segredo_1[let]:
            print(f_verde, let, padrao)
        elif termo[let] in segredo_1:
            print(f_amarelo, let, padrao)
        else:
            print(let)





# =====================================================================================================
