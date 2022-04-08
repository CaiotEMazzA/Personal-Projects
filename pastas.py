import os

lista_pastas = os.listdir()

print(lista_pastas)

for i in lista_pastas:
    if os.path.isdir(i):
        pass
    else:
        lista_pastas.remove(i)

f = open('pastasnestediretório.txt', 'w')

for i in lista_pastas:
    if lista_pastas.index(i) < len(lista_pastas) - 1:
        f.write(f'{i}\n')
    else:
        f.write(i)

f.close()

print(lista_pastas)

os.system('pause')
