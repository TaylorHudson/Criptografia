from criptografia import *
import os

def formatar_entrada(numeros):
    lista_numeros = numeros.split(", ")
    matriz_criptografada = []
    for i in range(len(lista_numeros)):
        if (i % 2 == 0):
            linha = []
            linha.append(int( lista_numeros[i] ))
            linha.append(int( lista_numeros[i + 1] ))
            matriz_criptografada.append(linha)
    matriz_criptografada = np.array(matriz_criptografada)
    return matriz_criptografada

def principal(chave, chave_inversa):
    try:
        opc = 0
        while (opc != 2):
            opc = int(input('O que deseja fazer? Criptografar(0), descriptografar(1) ou parar o programa(2)? '))

            if (opc == 0):
                os.system('cls')
                mensagem_para_cifrar = input('Digite uma mensagem para ser cifrada: ')

                matriz_cifrada = cifrar(mensagem_para_cifrar, chave)
                print(f'Essa é sua matriz cifrada: \n{matriz_cifrada}')

                mensagem = retornar_mensagem_cifrada(matriz_cifrada)
                print(f'E essa é sua mensagem cifrada: {mensagem}')
            elif (opc == 1):
                os.system('cls')
                numeros = input('Digite a mensagem cifrada: ')
                matriz_criptografada = formatar_entrada(numeros)

                matriz_decifrada = decifrar(matriz_criptografada, chave_inversa)
                print(f'Essa é sua matriz decifrada: \n{matriz_decifrada}')

                mensagem = retornar_mensagem_decifrada(matriz_decifrada)
                print(f'E essa é sua mensagem decifrada: {mensagem}')
            elif (opc != 2):
                os.system('cls')
                print('Digite uma entrada válida.')
    except:
        os.system('cls')
        print('Algo deu errado,tente novamente.')
        principal(chave, chave_inversa)

chave = np.array([[2,1],[-1,4]])
chave_inversa = np.linalg.inv(chave)

principal(chave, chave_inversa)