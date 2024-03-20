from random import randint
from time import sleep
comp = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == comp:
    print('PARABÉNS! Você conseguiu me venncer!')
else: 
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, jogador))
