#Crie um programa que leia a temperatura graus celsius e converta para graus fahrenheit.

celcius = float(input('Informe a temperatura em °C: '))
fahrenheit = celcius * 1.8 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(celcius, fahrenheit))