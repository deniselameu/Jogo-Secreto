import os
print('Bem-Vindo ao jogo Secreto! ')

def gerar_numero_aleatorio():
 import random
 return random.randrange(1, 10)

numero_secreto = gerar_numero_aleatorio()
#print(f'O número secreto é {numero_secreto}')

def limpar():
 #comando para limpar o terminal 
    os.system('cls')
    print('Você Ganhou !!!!! \n')

def verificar_numero_escolhido():
 tentativas = 0
 
 while True:
  numero_escolhido = int(input('Escolha um número de 1 a 10: '))
  tentativas += 1
  if(numero_escolhido == numero_secreto):
   break
  else:
    if(numero_escolhido > numero_secreto):
     print(f'O número é menor que {numero_escolhido} ')
    else: 
     print(f'O número é maior que {numero_escolhido} ')


verificar_numero_escolhido()
limpar()
