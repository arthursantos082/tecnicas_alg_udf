#estabelece que um número maior o substituirá
maiorNum = 0
#estabelece que sempre um número menor o substituirá
menorNum = 100000

for i in range (0,10): 
    num = float(input(f'Informe o {i+1} valor: '))

    if num > maiorNum:
        maiorNum = num
    
    if num < menorNum: 
        menorNum = num
print(f'O maior número é {maiorNum} e o menor número é {menorNum}.')