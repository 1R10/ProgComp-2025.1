# Aluno: Ryan Guilherme Costa de Moura; 20242014050039
#ALUNO: Roberto Araujo Batista, Matricula: 20251014050041
#PROFESSOR: Galileu Batista, CURSO: redes de computadores 2025.1, IFRN


'''
2) Faça um programa que conta quantos números palíndromos existem entre
10 e 100000. Um número é palíndromo quando tem o mesmo valor se lido da
esquerda para a direita ou da direita para a esquerda. Ex: 98189 é palíndromo. Não
use strings na sua resposta.
'''


def identificar_palindromo(numero):
    novonumero = numero
    numeroInverso = 0
    while novonumero != 0:
        algarismo = novonumero % 10
        novonumero = novonumero //10
        numeroInverso = (numeroInverso *10) + algarismo
    if numeroInverso == numero:
        print(f'{numero} é palindromo')
        return True
    else:
        print(f'{numero} não é palindromo')
        return False


palindromos = 0
#o programa irá chamar a função de identificar palindromo no intervalo do range:
for num in range(10,100001):
    #a função retorna true para palindromo, então é só contar a quantidade de True's retornados
    if identificar_palindromo(num):
        palindromos = palindromos +1

print(f'A quantidade de palindromos entre o intervalo de 10 e 100000 é: {palindromos}')
