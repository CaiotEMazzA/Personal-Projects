# Programa que gera números pseudo-aleatórios e os apresenta de diferentes formas.

from random import randint
from os import system

def print_list(lista):
    for i in lista:
        if lista.index(i) < len(lista) - 1:
            print(f'{str(i)}, ', end='')
        else:
            print(f'{str(i)}.')

sorteados = list()
restantes = list()

while len(sorteados) < 54:
    atual = randint(1, 60)
    if atual not in sorteados:
        sorteados.append(atual)
for i in range(1, 61):
    if i not in sorteados:
        restantes.append(i)

welcome = 'Olá Augusto! Aqui estão seus números campeões ;D'
print('=' * len(welcome))
print(welcome)
print('=' * len(welcome))

print()
print('Aqui estão os números sorteados (na ordem de sorteio): ', end='')
print_list(sorteados)

print()
print('Aqui estão os números sorteados (na ordem crescente): ', end='')
print_list(sorted(sorteados))

print()
print('Aqui estão os números restantes: ', end='')
print_list(restantes)

system('pause')
