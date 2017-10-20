import base64
import os
import sys
from time import sleep

# Verifica o SO
so = sys.platform
if 'win' in so:
    limpa = 'cls'
else:
    limpa = 'clear'

while True:
    print('\t\tEncode|Decode by: KrioK')
    print('\t 1 - Encode\n')
    print('\t 2 - Decode\n')
    print('\t 3 - Quit\n')
    op = input('Escolha uma opção: ')
    if op == '2':
        decrypt = ''
        data = input('Hash: ')
        bit_decrypt = base64.b64decode(data)
        bit_decrypt = str(bit_decrypt)

        for j in range(1, len(bit_decrypt)):
            if bit_decrypt[j] == "'":
                pass
            else:
                decrypt += bit_decrypt[j]
        print('\n')
        print(decrypt)
        input('Enter para sair...')
        os.system(limpa)
    elif op == '1':
        encrypt = ''
        data = input('Mensagem: ')
        encoded = data.encode('ascii')
        bit_encrypt = base64.b64encode(encoded)
        bit_encrypt = str(bit_encrypt)

        for i in range(1, len(bit_encrypt)):
            if bit_encrypt[i] == "'":
                pass
            else:
                encrypt += bit_encrypt[i]

        print('\n')
        print(encrypt)
        input('Enter para sair...')
        os.system(limpa)

    elif op == '3':
        sleep(2)
        exit()
        os.system(limpa)
    else:
        print('Erro na escolha da opção....')
        sleep(5)
        os.system(limpa)