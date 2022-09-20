import numpy as np

chave = np.array([2,1,-1,4])
chave = np.resize(chave,(2,2))
chave_inversa = np.linalg.inv(chave)

def cifrar(palavra, chave):
    if (len(palavra) % 2 != 0):
        palavra += ' '

    matriz_cifrada = []
    matriz = []

    for i in range(len(palavra)):
        if i % 2 == 0:
            linha = []
            linha.append(ord(palavra[i]))
            linha.append(ord(palavra[i+1]))
            matriz.append(linha)

    for i in range(len(matriz)):
        linha = []
        linha = np.dot(chave, matriz[i])
        matriz_cifrada.append(linha) 
    matriz_cifrada = np.array(matriz_cifrada)

    return matriz_cifrada

def decifrar(matriz_cifrada, chave_inversa):
    matriz_decifrada = []
    for i in range(len(matriz_cifrada)):
        linha = []
        linha = np.dot(chave_inversa,matriz_cifrada[i])
        matriz_decifrada.append(linha)
    matriz_decifrada = np.array(matriz_decifrada)

    return matriz_decifrada

def retornar_mensagem(matriz_decifrada):
    msg_decifrada = ''
    for i in range(len(matriz_decifrada)):
        for j in range(len(matriz_decifrada[i])):
            if int(matriz_decifrada[i][j]) != matriz_decifrada[i][j]:
                msg_decifrada += chr(int(matriz_decifrada[i][j]) + 1)
            else:
                msg_decifrada += chr(int(matriz_decifrada[i][j]))
    
    return msg_decifrada