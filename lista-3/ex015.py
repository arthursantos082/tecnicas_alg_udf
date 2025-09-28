numerosDigitados = []

while True:
    entradaNumeros = input('Informe um valor real: ')
    try:
        numeros = float(entradaNumeros)
        numerosDigitados.append(numeros)
        if numeros == 0:
            numerosDigitados.sort()
            print(numerosDigitados)
            break
    except ValueError:
        print('Por favor, informe um valor válido.')
        break
