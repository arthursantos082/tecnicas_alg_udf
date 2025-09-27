qtdNum = int(input('Quantos números serão lidos? '))
cont = 0
listaNum = []

while cont < qtdNum:
    num = int(input(f'Informe o {cont + 1} número inteiro: '))
    listaNum.append(num)
    cont += 1

media = sum(listaNum) / len(listaNum)

print(f'A soma dos números informados é: {sum(listaNum)}')
print(f'A média aritimética dos números é: {media}')