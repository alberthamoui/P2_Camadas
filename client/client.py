from comands import *
from enlace import *
import time
import numpy as np


# como fazer pra reconhecer comeco e final?
    # criar um negocio d bytes b'\x??' pra comeco e pra fim


#coloquei xfa como byte de espaco ja que o server vai receber tudo junto, n eh otimizado mas funciona
#ira ter byte de comeco e byte de final, pro server reconhecer (esta certo)

serialName = "COM7"
comeco = b'\xc'

final = b'\xf'

def main():
    try:
        contador = 0
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        print("Abriu a comunicação")



        txBuffer, tam = sorteiaComando() 
        print("O array de bytes len de {}" .format(tam))

        com1.sendData(np.asarray(txBuffer))  
        
        
        #acesso aos bytes recebidos
        txLen = len(txBuffer)
        rxBuffer, nRx = com1.getData(txLen)


        print("Salvando dados no arquivo :")
        print(" - {}".format(imagew))
        f = open(imagew, 'wb')
        f.write(rxBuffer)
        
        # Fecha arquivo de imagem
        f.close()


        print("recebeu {} bytes" .format(len(rxBuffer)))
        
        for i in range(len(rxBuffer)):
            print("recebeu {}" .format(rxBuffer[i]))

            if contador == 0:
                txSize = com1.tx.getStatus()
                print('enviou = {}' .format(txSize))
                # contador = 0

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