import os

# função potência
def potencia(n):
    return n ** 2

# limpar o terminal do Windous
os.system('cls')

# Entrada do usuario
num_string = str(input('Digite numeros: ')).strip() #1 2 3 4 5

# Verificar se a entrada contém apenas números sem separação
if num_string.isdigit():
    # Separar cada caractere individualmente
    num_inteirios = list(map(int, num_string))
else:
    # Separar pelos espaços (ou outros delimitadores)
    num_inteirios = list(map(int, num_string.split()))

numeros_dobrados = list(map(lambda x: x*2, num_inteirios))
numeros_quadrado = list(map(potencia, num_inteirios))

print('Números dobrados: ', numeros_dobrados)
print(f'Números ao quadrado: {numeros_quadrado}')

