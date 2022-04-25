# Programa que gera lista de números e se certifica de que o desvio padrão dessa lista é menor ou igual ao especificado

# Função que calcula média (media) de uma dada lista (lis)
def media(lis):
  """
  Função que calcula e retorna média aritmética de uma lista ou tupla (lis)
  """
  media = 0
  for n in lis:
    media += n
  media /= len(lis)
  return media

# Importando função que gera número pseudo-aleaório entre 0 e 1
from random import random

# Laço para garantir que o desvio padrão amostral será menor ou igual ao valor desejado
while True:
  # Atribuição de variáveis
  lista = list()
  cont = 0
  desvpad = 0
  
  # Gerando lista (lista) pseudo-aleatória
  while cont < 25:
    lista.append(random())
    cont += 1

  # Calculando média (medianum) da lista com função criada
  medianum = media(lista)

  # Calculando desvio padrão amostral (desvpad) da lista (lista)
  for i in lista:
    desvpad += (i - medianum)**2
  desvpad /= len(lista) - 1
  desvpad **= (1/2)

  # Se o desvio padrão calculado for menor ou igual ao valor desejado, encerrar laço
  if desvpad <= 0.15:
    break

# Imprimir na tela lista gerada (lista), média dos elementos da lista (média) e desvio padrão amostral dos elementos da lista (desvpad)
print(f'Lista: {lista}')
print()
print(f'Média: {medianum}')
print()
print(f'Desvio padrão amostral: {desvpad}')
print()
help(media)
