''' Peça um número inteiro N e verifique se ele é um número perfeito.'''

# Meu código
num = int(input('Digite um numero: '))

divisor_proprio = []

for n in range(1, num):
    if num % n == 0:
        divisor_proprio.append(n)

if sum(divisor_proprio) == num:
    print(f'O numero {num}, é um um numero perfeito')
else:
    print(f'O numero {num}, não é um numero perfeito')

# Código do chatGPT
def numero_perfeito(n):
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return soma_divisores == n

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verificando se é perfeito
if numero_perfeito(numero):
    print(f"O número {numero} é perfeito.")
else:
    print(f"O número {numero} não é perfeito.")
