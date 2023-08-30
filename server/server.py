from enlace import *
import time
import numpy as np

serialName = "COM7"

def main():
    try:
        contador = 0

        print("Iniciou o main")
        com1 = enlace(serialName)
        
    
        com1.enable()
        print("Abriu a comunicação")
        


        print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))
        
            
        com1.sendData(np.asarray(txBuffer))
        
        
        


        txLen = len(txBuffer)
        rxBuffer, nRx = com1.getData(txLen)


        print("recebeu {} bytes" .format(len(rxBuffer)))
        
        for i in range(len(rxBuffer)):
            print("recebeu {}" .format(rxBuffer[i]))

            if contador == 0:
                txSize = com1.tx.getStatus()
                print('enviou = {}' .format(txSize))

            contador = 1
            print(contador)
        
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()