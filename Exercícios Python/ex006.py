#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int (input('Digite um número: '))
print('O número digitado foi: {}!'.format(n))
print('O dobro vale: {}'.format(n*2))
print('O triplo vale: {}'.format(n*3))
print('A raiz quadrada vale: {:.2f}'.format(n**(1/2)))