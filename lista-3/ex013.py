qtdReg = (input('Quantos registros serão lidos? '))
try:
    qtdReg = int(qtdReg)
except:
    print('Informe um valor válido.')

idadeMasc = []
idadeFem = []
regIdade = 0
regSexo = ''

for i in range(0, int(qtdReg)):
    regSexo = input(f'Informe o sexo (M/F) da {i+1} pessoa: ').lower()
    regIdade = (input(f'Informe a idade da {i+1} pessoa: '))

    try:
        regIdade = int(regIdade)
        regSexo.isalpha
    except:
        print('Por favor, informe valores válidos.')
        break

    if regSexo == 'm':
        idadeMasc.append(regIdade)
    
    elif regSexo == 'f':
        idadeFem.append(regIdade)
    
mediaMasc = sum(idadeMasc)/len(idadeMasc)
mediaFem = sum(idadeFem)/len(idadeFem)

print(f'A média de idade do sexo masculino é: {mediaMasc:.2f}, e a média de idade do sexo feminino é: {mediaFem:.2f}.')