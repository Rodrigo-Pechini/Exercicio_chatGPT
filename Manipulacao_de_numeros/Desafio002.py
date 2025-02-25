'''O programa deve solicitar um número inteiro positivo e contar quantos 
números pares e ímpares existem de 1 até esse número.'''

num = int(input('Digite um numero: '))
par = 0
impar = 0
for n in range(0, num):
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Total de numeros pares: {par}')
print(f'Total de numeros impares: {impar}')
