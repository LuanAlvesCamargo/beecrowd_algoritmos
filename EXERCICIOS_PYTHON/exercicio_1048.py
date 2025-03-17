# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


# Salário	Percentual de Reajuste
# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00

# 15%
# 12%
# 10%
# 7%
# 4%

# Leia o salário do funcionário e calcule e mostre o novo salário, 
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
# # (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

salary = float(input())

if salary <= 400.00:
    percentage = 15
elif salary <= 800.00:
    percentage = 12
elif salary <= 1200.00:
    percentage = 10
elif salary <= 2000.00:
    percentage = 7
else:
    percentage = 4

raise_amount = salary * percentage / 100
new_salary = salary + raise_amount

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {raise_amount:.2f}")
print(f"Em percentual: {percentage} %")

