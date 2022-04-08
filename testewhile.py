from time import time
inicio = time()
i = 0
while i < 10**7:
    print(i)
    i += 100
print('\nTempo: {:.2f}s'.format(time() - inicio))
