from random import randint
from time import time
from datetime import datetime

print('Início: {}'.format(datetime.now().time()))
inicio = time()
aleatorio = randint(0, 10**7)
cont = 0
i = 0

print('Número aleatório: {}'.format(aleatorio))

while i != aleatorio:

    i = randint(0, 10**7)
    cont += 1

print('Tentativas: {}'.format(cont))
print('Fim: {}'.format(datetime.now().time()))
tempo = time() - inicio

if tempo >= 3600:
    horas = int(tempo // 3600)
    minutos = int((tempo % 3600) // 60)
    segundos = (tempo % 3600) % 60
else:
    if tempo >= 60:
        horas = 0
        minutos = int(tempo // 60)
        segundos = tempo % 60
    else:
        horas = 0
        minutos = 0
        segundos = tempo

print('Tempo: {:.2f}s ---> {}h {}min {:.2f}s'.format(tempo, horas, minutos, segundos))
