import os
import pyaes

## Abrir o arquivo criptrografado

filename = 'teste.txt.ransomwaretroll'
file = open(filename, 'rb')
filedata = file.read()
file.close()

## Setar a chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decryptdata = aes.decrypt(filedata)

## Remover o arquivo criptografado

os.remove(filename)

## Criar novo arquivo descriptografado

newfile = 'teste.txt'
newfile = open(f'{newfile}', 'wb')
newfile.write(decryptdata)
newfile.close()
