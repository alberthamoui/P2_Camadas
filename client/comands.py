from random import *


def sorteiaComando():
    espaco = 'fa'
    espaco = bytes.fromhex(espaco)
    final = []
    comandos = [bytes.fromhex("00 00 00 00"),bytes.fromhex("00 00 BB 00"),bytes.fromhex("BB 00 00"),bytes.fromhex("00 BB 00"),bytes.fromhex("00 00 BB"),bytes.fromhex("00 AA"),bytes.fromhex("BB 00"),bytes.fromhex("00"),bytes.fromhex("BB")]
    n = randint(10,31)
    for i in range(n):
        final.append(comandos[randint(0,8)])
        final.append(espaco)
    return final, len(final)

print(sorteiaComando())