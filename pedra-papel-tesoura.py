import random

                                                              #aviso o Python que vou importar informação aleatóriamente pro meu jogo
                                                                # porque a escolha do computador vai ser aleatória
winner = ''
                                                                #o winner fica vazio, porquê a cada rodada, dependendo da escolha do jogador
                                                                #o ganhador será diferente
random_choice = random.randint(0,2)

                                                                #acima declarei que os núeros aleatórios estão entre 0,1 e 2
                                                                #abaixo especifico a cada número seu papel no jogo
if random_choice == 0:
    computer_choice = 'pedra'
elif random_choice == 1:
    computer_choice = 'papel'
else: 
    computer_choice = 'tesoura'

                                                                #crio pra user_choice uma string vazia, para criar um looping se o usuário não der uma resposta válida
user_choice = ''
while (user_choice != 'pedra' and
       user_choice != 'papel' and
       user_choice != 'tesoura'):
    user_choice = input ('pedra, papel ou tesoura?')            #enquanto estiver errada a resposta, ele vai perguntar até a resposta ser válida
                                                                #sendo válida, o jogo continua

                                                                #explico pro Python, quais resultador terão o jogo, com base na resposta aleatória do computador
if computer_choice == user_choice:
    winner = 'Empate'
elif computer_choice == 'papel' and user_choice == 'pedra':
    winner = 'Computador'
elif computer_choice == 'pedra'and user_choice == 'tesoura':
    winner = 'Computador'
elif computer_choice == 'tesoura' and user_choice == 'papel':
    winner = 'Computador'
else:
    winner = 'Você'

if winner == 'Empate':
    print ( 'Ahh, nós dois escolhemos', computer_choice + ', vamos jogar de novo!') #exibo a mensagem no caso de empate
else:
    print ( winner, 'ganhou! O Computador escolheu', computer_choice + '.')       #se não mostro quem ganhou e também a resposta do computador

input()


