# Programa que extrai anexos, imagens e texto de arquivos '.msg'.
# Para utilizar, copie este programa para dentro da pasta que contém os arquivos
# '.msg'.

# Importando bibliotecas utilizadas no programa.
import os, extract_msg, pathlib

# Gerando lista com nomes dos arquivos dentro da pasta e lendo o caminho da
# pasta atual completo.
listaarq = os.listdir()
pastaatual = str(pathlib.Path().absolute()).replace("\\", "/")

# Obtendo apenas o nome da pasta atual, e não o caminho completo.
cont = 0
for carac in range(-1, -(len(pastaatual)), -1):
    if pastaatual[carac] != '/':
        cont += 1
    else:
        break
pastaatual = pastaatual[-(cont)::]

# Se não houver uma pasta com o mesmo nome da atual, cria-se uma.
# Dentro do laço, se o arquivo considerado no momento tiver o nome diferente do
# nome deste programa (extractmsg.py) e for um arquivo '.msg', salva-se os
# anexos dele dentro da pasta criada.
if pastaatual not in listaarq:
    os.mkdir(pastaatual)
    for i in listaarq:
        if i != 'extractmsg.py' and i[-4::] == '.msg':
            print(i)
            msg = extract_msg.openMsg(i)
            msg.save(customPath = pastaatual)
# Caso já exista uma pasta com o nome da pasta a ser criada, é exibida a
# mensagem de erro.
else:
    print(f'Já existe uma pasta chamada {pastaatual}! Por favor, exclua esta pasta e rode o programa novamente.')

# Pede para o usuário pressionar qualquer tecla para encerrar o programa.
os.system('pause')
