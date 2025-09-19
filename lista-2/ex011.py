nome1 = input('Informe o nome da primeira pessoa: ')
nome2 = input('Informe o nome da segunda pessoa: ')

peso1 = float(input('Informe o peso da primeira pessoa: '))
peso2 = float(input('Informe o peso da segunda pessoa: '))

if peso1 > peso2:
    print(f'{nome1} é mais pesado que {nome2}')
else:
    print(f'{nome2} é mais pesado que {nome1}')