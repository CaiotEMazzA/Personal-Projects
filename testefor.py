from time import time
inicio = time()
for i in range(0, 10**7, 100):
    print(i)
print('\nTempo: {:.2f}s'.format(time() - inicio))
