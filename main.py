from criptografia import *

mensagem_para_cifrar = input('Digite uma frase para ser cifrada:')

matriz_cifrada = cifrar(mensagem_para_cifrar, chave)
matriz_decifrada = decifrar(matriz_cifrada, chave_inversa)
msg = retornar_mensagem(matriz_decifrada)

print('Matriz cifrada: ')
print(matriz_cifrada)
print('Matriz decifrada:')
print(matriz_decifrada)
print(f'\nA mensagem que você digitou foi: {msg}')
