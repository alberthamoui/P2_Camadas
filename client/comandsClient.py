from random import *


def sorteiaComando():
    espaco = 'fa'
    comeco = 'ac'
    final = 'af'
    contadorEspaco = 0

    espaco = bytes.fromhex(espaco)
    comeco = bytes.fromhex(comeco)
    final = bytes.fromhex(final)

    lista = []
    comandos = [bytes.fromhex("00 00 00 00"),bytes.fromhex("00 00 BB 00"),bytes.fromhex("BB 00 00"),bytes.fromhex("00 BB 00"),bytes.fromhex("00 00 BB"),bytes.fromhex("00 AA"),bytes.fromhex("BB 00"),bytes.fromhex("00"),bytes.fromhex("BB")]
    n = randint(10,31)
    lista.append(comeco)
    for i in range(n):
        lista.append(comandos[randint(0,8)])
        lista.append(espaco)
        contadorEspaco += 1
    lista.append(final)
    return lista, len(lista), len(lista)-contadorEspaco-2

print(sorteiaComando())





# b'\xac
# \x00\x00\x00\x00\x00\x00\x00
# \xfa
# \x00\x00\x00\x00\x00\xbb\x00
# \xfa
# \x00\x00\x00\xbb\x00\x00\x00
# \xfa
# \x00\x00\x00\xbb\x00\x00\x00
# \xfa
# \x00\x00\x00\xbb\x00\x00\x00
# \xfa
# \x00\x00\x00\x00\x00\xbb\x00
# \xfa
# \x00'