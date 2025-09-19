prova1 = float(input('Informe a nota da primeira prova: '))
prova2 = float(input('Informe a nota da segunda prova: '))
prova3 = float(input('Informe a nota da terceira prova: '))

peso1 = prova1 * 2
peso2 = prova2 * 3
peso3 = prova3 * 5

media = (peso1 + peso2 + peso3) / 10

if media > 6: 
    print(f'O aluno foi aprovado!')
else:
    print(f'O aluno não foi aprovado.')