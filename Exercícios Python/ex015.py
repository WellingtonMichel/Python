#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Para saber quanto deverá pagar pelo carro alugado, preencha as seguintes informações:')
dia = int(input('Quantos dias alugados? '))
qkm = float(input('Quantos Km percorridos com o carro? '))
pago = (dia * 60) + (qkm * 0.15)
print('O preço total a pagar é de R${:.2f}'.format(pago))