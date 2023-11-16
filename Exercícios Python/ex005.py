#Faça um programa que leia um numero inteiro e mostra na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('Você digitou o número {}!'.format(n))
print('O antecessor a este número é {}'.format(n-1))
print('O sucessor a este número é {}'.format(n+1))