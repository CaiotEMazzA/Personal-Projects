from random import randint
from os import system

sorteados = list()
restantes = list()

while len(sorteados) < 54:
    atual = randint(0, 60)
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
for i in sorteados:
    if sorteados.index(i) < len(sorteados) - 1:
        print(f'{str(i)}, ', end='')
    else:
        print(f'{str(i)}.')

print()
print('Aqui estão os números sorteados (na ordem crescente): ', end='')
for i in sorted(sorteados):
    if sorted(sorteados).index(i) < len(sorteados) - 1:
        print(f'{str(i)}, ', end='')
    else:
        print(f'{str(i)}.')

print()
print('Aqui estão os números restantes: ', end='')
for i in restantes:
    if restantes.index(i) < len(restantes) - 1:
        print(f'{str(i)}, ', end='')
    else:
        print(f'{str(i)}.')

system('pause')

