#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1,00 = R$:3,27

real = float(input('Quanto dinheiro você possui na carteira? R$'))
dolar = real / 4.86
print('Você possui R${:.2f}, portanto poderá comprar US${:.2f} dólares.'.format(real, dolar))