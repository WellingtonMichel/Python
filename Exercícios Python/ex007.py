#Desenvolva um programa que leia as duas notas de um aluno e mostre a sua média.

print('Escreva suas notas abaixo para saber sua média.')
n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
n = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é: {:.1f}'.format((n1), (n2), (n)))