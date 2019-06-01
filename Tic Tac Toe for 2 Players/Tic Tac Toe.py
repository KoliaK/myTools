'''
a) Precisamos imprimir um tabuleiro. >DONE<
b) Pegue a entrada do jogador. >DONE<
c) Coloque sua entrada no tabuleiro. >DONE<
d) Verifique se o jogo é ganho, empatado, perdido ou em curso. >DONE<
e) Repita c e d até o jogo ter sido ganho ou empatado. >DONE<
f) Pergunte se os jogadores querem jogar de novo. >DONE<

Extras(Adicionados por KoliaK):
- Função que esvazia o tabuleiro
- Função que atualiza a tela
- Função que pega o input de cada jogador
- Função que pergunta se os jogadores gostariam de jogar de novo
'''
import os
import sys
import time
import random 
board = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_title():
  print('''
  _____ ___ ____   _____  _    ____   _____ ___  _____
 |_   _|_ _/ ___| |_   _|/ \  / ___| |_   _/ _ \| ____|         1 | 2 | 3
   | |  | | |       | | / _ \| |       | || | | |  _|           4 | 5 | 6
   | |  | | |___    | |/ ___ \ |___    | || |_| | |___          7 | 8 | 9
   |_| |___\____|   |_/_/   \_\____|   |_| \___/|_____| 
                                                    by MrKoliaK \n         
Para ganhar o jogo, você deve conseguir marcar 3 espaços em uma linha,
coluna ou diagonal. Suas escolhas são definidas,
devem ser de 1 até 9. Boa Sorte!\n''')

#Prints Board
def draw_board():
  print('   |   |   ')
  print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
  print('   |   |   ')
  print('---|---|---')
  print('   |   |   ')
  print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
  print('   |   |   ')
  print('---|---|---')
  print('   |   |   ')
  print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
  print('   |   |   \n')

#Refreshes Screen
def update_screen():
  os.system('cls') #updates the board
  print_title() #prints the header
  draw_board() #prints the board

#Makes the board empty again
def clear_board():
  for item in range(len(board)):
    if board[item] == 'X' or board[item] == 'O':
        board[item] = ' '

#Gets the player input
def player_input(player, mark):
  while True:
    choice = input(player + ', escolha um espaço do tabuleiro para o ' + mark + ': ')
    
    try:
      int(choice)
    except ValueError:
      print('Utilize apenas números de 1 a 9!')
      time.sleep(1)
      update_screen()
      continue

    choice = int(choice) #gets the player input and changes into an integer

    if choice < 1 or choice > 9:
      print('Utilize apenas números de 1 a 9!')
      time.sleep(1)
      update_screen()
      continue

    if board[choice] == ' ':
      board[choice] = mark #gets the integer input, and adds to the list as X
      break
    else:
      print('Escolha outro espaço, esse já foi usado!')
      time.sleep(1) #stops time for 1 second (adds delay to the printed message)
      update_screen()
      continue

#Checks for a win
def is_win(board, player, mark):
  #("or \" adds the next line in front the line above, that will make it all a single line statement)
  if ((board[1] == mark and board[2] == mark and board[3] == mark) or \
    (board[4] == mark and board[5] == mark and board[6] == mark) or \
    (board[7] == mark and board[8] == mark and board[9] == mark) or \
    (board[1] == mark and board[4] == mark and board[7] == mark) or \
    (board[2] == mark and board[5] == mark and board[8] == mark) or \
    (board[3] == mark and board[6] == mark and board[9] == mark) or \
    (board[1] == mark and board[5] == mark and board[9] == mark) or \
    (board[3] == mark and board[5] == mark and board[7] == mark)):  
    
    update_screen()
    print(player + " ganhou! Parabéns!")
    play_again()

#Checks for a Tie
def is_tie():
  isFull = True
  if ' ' in board:
    isFull = False
  
  if isFull == True:
    update_screen()
    print('Parece que temos um empate!')
    time.sleep(1)
    play_again()

#Asks if the players want to play again in any condition (win, lose or draw)
def play_again():
  while True:
    playAgain = (input("Jogar de novo? [S/N]? "))
    if playAgain == 'S' or playAgain == 's':
      print('Divirtam-se!')
      time.sleep(1)
      clear_board()
      break
    elif playAgain == 'N' or playAgain == 'n':
      print("Obrigado por Jogar! Até a próxima!")
      time.sleep(1)
      sys.exit()
    else:
      print('Responda com S ou N')
      time.sleep(1)
      update_screen()

#Main Loop
def game():
  while True:
    update_screen()
    #player1 turn
    player_input("Player1", "X")
    is_win(board, "Player1", "X")
    is_tie() 
    update_screen()

    #player2 turn
    player_input("Player2", "O")
    is_win(board, "Player2", "O")
    is_tie()
game()
  
  