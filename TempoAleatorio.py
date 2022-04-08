from random import randint
from time import time
from datetime import datetime

print('Início: {}'.format(datetime.now().time()))
inicio = time()
aleatorio = randint(0, 10**8)
cont = 0
i = 0

while i != aleatorio:

    i = randint(0, 10**8)
    cont += 1

print('Fim: {}'.format(datetime.now().time()))
print('Número aleatório: {}'.format(aleatorio))
print('Tentativas: {}'.format(cont))
tempo = time() - inicio
print('Tempo: {:.2f}s'.format(tempo))

if tempo >= 3600:
    horas = int(tempo // 3600)
    minutos = int((tempo % 3600) // 60)
    segundos = (tempo % 3600) % 60
elif tempo >= 60:
    horas = 0
    minutos = int(tempo // 60)
    segundos = tempo % 60
else:
    horas = 0
    minutos = 0
    segundos = tempo

print('Tempo: {}h {}min {:.2f}s'.format(horas, minutos, segundos))
