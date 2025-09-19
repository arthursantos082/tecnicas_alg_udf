salario_fixo = float(input('Digite o valor fixo do salário do vendedor: '))
total_vendas = float(input('Digite o total vendido no mês: '))
percentual_comissao = float(input('Digite o percentual de comissão (%): '))

comissao = (percentual_comissao /100) * total_vendas
salario_bruto = salario_fixo + comissao

print(f'O salaŕio bruto do vendedor é: R$ {salario_bruto:.2f}')