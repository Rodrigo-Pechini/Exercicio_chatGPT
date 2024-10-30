opc = input('Deseja inserir novos dados? [s/n]: ').lower().strip()

if opc == 's':
    print('Notas dos alunos')

    # Nome do aluno
    nome = str(input('Nome do aluno: ')).capitalize()

    # Quantidade de atividades feitas
    atividades = int(input(f'Quantas atividades o aluno {nome} fez: '))

    # Pedindo a nota dos alunos
    notas = []
    for i in range(atividades):
        notas.append(float(input(f'{i+1}° nota: ')))

    # Calculando a média das notas
    media = sum(notas) / len(notas)

with open('Registro_de_notas/arquivo.txt', 'a+') as arq:
    if opc == 's':
        # Gravando as notas separadas por vírgula
        arq.write(f'{nome}/{media:.2f}/' + ','.join(map(str, notas)) + '\n')
    arq.seek(0)

    # Lendo o arquivo e exibindo os dados
    for linha in arq:
        separado = linha.split('/')
        print(f'Aluno: {separado[0]} \t Média: {separado[1]} \t Notas: {separado[2].replace(",", ", ")}')
