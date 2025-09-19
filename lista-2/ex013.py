num1 = float(input('Informe o primero valor: '))
num2 = float(input('Informe o segundo valor: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
elif num1 == num2:
    print(f'Os valores informados são iguais.')