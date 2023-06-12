from random import randint

modo = int(input('escolha um modo de jogo \nRodada única digite 1 \nMelhor de cinco digite 2 \n:'))

res = []

if modo == 1:
  player = int(input('escolha sua opção \nPedra - digite 1\nPapel - digite 2\nTesoura - digite 3\n:'))
  res.append(player)
  pc = randint(1,3)
  res.append(pc)

  print(res)
  if res == player:
    print('deu empate')

  if res[0] % res[1] > 1: 
    print('o jogador venceu')