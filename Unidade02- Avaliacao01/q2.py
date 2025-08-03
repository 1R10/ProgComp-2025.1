# Aluno: Ryan Guilherme Costa de Moura; 20242014050039
# =====================================================================================================
# Palíndromo 10 --> 100000


contador = 0

for numero in range(10, 100001): # Conjunto -- > for tem melhor uso.
    numero_temp = numero  # Cópia temporária para manter o valor original.
    numero_invertido = 0


 # Pega o último número de um e adiciona no final do outro (revertendo - o)
    while numero_temp > 0: # vai até ter algum valor na variavel 
        digito = numero_temp % 10 
        numero_invertido = numero_invertido * 10 + digito
        numero_temp = numero_temp // 10

    if numero == numero_invertido:
        contador += 1

print(f'A quantidade de palíndromos entre 10 e 100000 é {contador}.')
