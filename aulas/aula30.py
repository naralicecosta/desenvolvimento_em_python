'''imprecisão de números de ponto flutuante + round e decimal.Decimal'''
import decimal

numero_1 = decimal.Decimal(0.1)
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2}')
print(round(numero_3, 2))