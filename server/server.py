from enlace import *
import time
import numpy as np

serialName = "COM7"
recebidos = []
comeco = b'\x0a'
final = b'\x0f'


def main():
    try:
        contador = 0

        print("Iniciou o main")
        com1 = enlace(serialName)
        
    
        com1.enable()
        print("Abriu a comunicação")
        
        # Sacrificio
        print("esperando 1 byte de sacrifício")
        tamanho, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)

        contador = 0
        bandeira = True

        while bandeira:
            if contador == 0:
               com1.rx.clearBuffer()
               com1.sendData(np.asarray(comeco))  
               com1.rx.clearBuffer()
               time.sleep(.1)
               print('comecou')
            else:
                numero = com1.getData(1)

                numeroint = int.from_bytes(numero[0], byteorder="big")
                print(numero)
                rxBuffer, nRx = com1.getData(numeroint)
                time.sleep(1)
                info = com1.getData(numeroint)
                print("recebeu {}".format(rxBuffer))

                if info == final:
                    com1.sendData(np.asarray(final))
                    break
            contador+=1
        
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
    print(recebidos)
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()