# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

valor_hora = int(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha no mês? "))

salario_bruto = (valor_hora * horas_mes)
print(f"+ Salário Bruto : R${salario_bruto}")

imposto = 0.11
imposto_desc = int((imposto * salario_bruto))
print(f"- IR (11%) : R${imposto_desc}")

inss = 0.08
inss_desc = int((inss * salario_bruto))
print(f"- INSS (8%): R${inss_desc}")

sindicato = 0.05
sindicato_desc = int((sindicato * salario_bruto))
print(f"- Sindicato (5%): R${sindicato_desc}")

salario_liquido = (salario_bruto - imposto_desc - inss_desc - sindicato_desc)
print(f"= Salário Liquido : R${salario_liquido}")