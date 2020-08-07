import re
import random
def jogdsf():
    desafioctrl1=re.sub('@',jog1,desafio)
    desafioctrl2=re.sub('#',jog2,desafioctrl1)
    print('\n',desafioctrl2)
print('---- Joguin ----\n')
jogadores=int(input('Quantos jogadores? '))
jogname=[]
dsfstore=[]
for c in range(1,jogadores+1):
    c=input(f'{c}º jogador: ')
    jogname.append([c])
print('\nUse "@" ou "#" no lugar dos nomes\n'
       'e.g. @ deve dar um abraço em #\n'
       'Ou use "&" para repetir desafios')
while c!='n':
    random.shuffle(jogname)
    jog1=str(random.choice(jogname))
    jog2=str(random.choice(jogname))
    while jog1==jog2:
        jog2=str(random.choice(jogname))
    desafio=input('\nDigite um desafio: ')
    if desafio=='&':
        desafio=str(random.choice(dsfstore))
        jogdsf()
    else:
        dsfstore.append([desafio])
        jogdsf()
    c=input('\nContinuar? [s/n] ')