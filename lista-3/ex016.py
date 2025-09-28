contadorAlunos = 0
idadeInt = 0
contMaioridade = 0
contAtedezoito = 0
listaIdades = []
sortedIdades = []

while True:

    idadeAlunos = input(f'Informe a idade do {contadorAlunos+1}. aluno: ')
    continuar = input(f'Deseja continuar? S/N ').lower()
    try:
        idadeInt = int(idadeAlunos)
        listaIdades.append(idadeInt)
        sortedIdades = sorted(listaIdades)
        continuar.isalpha
    except ValueError:
        print('Por favor, informe valores válidos.')

    if idadeInt > 18:
        contMaioridade +=1
    
    elif idadeInt <= 18:
        contAtedezoito += 1

    if len(listaIdades) % 2 == 0:
        metade_direita = len(listaIdades)//2
        metade_esquerda = metade_direita - 1
        mediana = (sortedIdades[metade_esquerda] + sortedIdades[metade_direita]) / 2

    else:
        metade = len(listaIdades) // 2
        mediana = sortedIdades[metade]

    if continuar == 's':
        contadorAlunos += 1
        continue
    elif continuar == 'n':
        break

print(f'A idade do aluno mais novo é {min(listaIdades)}.')
print(f'A idade do aluno mais velho é {max(listaIdades)}.')
print(f'A média aritimética da idade dos alunos é {sum(listaIdades)/len(listaIdades)}.')
print(f'As idades em ordem são {sortedIdades}.')
print(f'A mediana das idades é {mediana}.')