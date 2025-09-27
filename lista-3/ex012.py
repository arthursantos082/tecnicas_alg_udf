qtdNum = int(input('Quantos registros serão lidos? '))
idadeMaisvelho = 0
nomeMaisvelho = ''

for i in range(0, qtdNum):
    nome = input(f'Informe o nome da {i+1} pessoa: ')
    idade = int(input(f'Informe a idade da {i+1} pessoa: '))

    if idade > idadeMaisvelho:
        nomeMaisvelho = nome
        idadeMaisvelho = idade

print(f'A pessoa mais velha é: {nomeMaisvelho} e sua idade é: {idadeMaisvelho}')