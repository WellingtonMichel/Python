#Faça um algoritmo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto.
p = float(input('Qual é o preço do produto? R$'))
d = p * 5 / 100
newp = p - d
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, newp))

