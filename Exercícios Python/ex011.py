#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade da tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = (float(input('Digite a largura da parede em metros: ')))
altura = (float(input('Digite a altura da parede em metros: ')))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))