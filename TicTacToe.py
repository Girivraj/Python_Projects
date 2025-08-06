def user_input():
  player1_turn = input("Enter the row_number(row1 or row2 or row3): ").lower()
  player1_position = int(input("Enter the position (0 or 1 or 2): "))
  return player1_turn,player1_position

def validate(player1_turn, player1_position):
  start = True
  while start:
    if player1_turn == 'row1' or player1_turn == 'row2' or player1_turn == 'row3':
        start = False
    if player1_position == 0 or player1_position == 1 or player1_position == 2:
      start = False
    else:
      start = True
      return "Infinite loop"

def player_turn(choice,player1_turn, player1_position):
  if board1[player1_turn][player1_position] == ' ':
    board1[player1_turn][player1_position] = choice
  else:
    print("The position is already taken")

def cpu_turn(choice,player1_turn, player1_position):
  if choice == 'O':
    cpu_c = 'X'
  else:
    cpu_c = 'O'
  turn = ['row1','row2','row3']
  cpu_turn = random.choice(turn)
  position = [0,1,2]
  cpu_position = random.choice(position)
  if board1[cpu_turn][cpu_position] == ' ':
    board1[cpu_turn][cpu_position] = cpu_c
  else:
    print("The position is already taken")

def result():
    b = board1  # shorthand
    # Check if any winning combination has the same symbol and is not empty
    if (b['row1'][0] == b['row2'][0] == b['row3'][0] != ' ') or \
       (b['row1'][1] == b['row2'][1] == b['row3'][1] != ' ') or \
       (b['row1'][2] == b['row2'][2] == b['row3'][2] != ' ') or \
       (b['row1'][0] == b['row1'][1] == b['row1'][2] != ' ') or \
       (b['row2'][0] == b['row2'][1] == b['row2'][2] != ' ') or \
       (b['row3'][0] == b['row3'][1] == b['row3'][2] != ' ') or \
       (b['row1'][0] == b['row2'][1] == b['row3'][2] != ' ') or \
       (b['row1'][2] == b['row2'][1] == b['row3'][0] != ' '):
        print(f"{b['row1'][0]} wins")
        return True
    return False

import random
board1 = {
    "row1":[' ', ' ', ' '],
    "row2":[' ', ' ', ' '],
    "row3":[' ', ' ', ' ']
}
def start():
  choice = str(input("Enter your choice X or O: ")).upper()
  a = False
  while not a:
    #user_input()
    player1_turn, player1_position = user_input()
    validate(player1_turn, player1_position)
    player_turn(choice,player1_turn, player1_position)
    cpu_turn(choice,player1_turn, player1_position)
    for row in board1.values():
      print(' '.join(row))
    a = result()

start()
