num = int(input('Digite um número inteiro: '))
multiplo = int(input('Informe qual é o múltiplo que deseja verificar: '))

if num % multiplo == 0:
    print(f'O número digitado é múltiplo de {multiplo}')
else:
    print(f'O número digitado não é múltiplo de {multiplo}')