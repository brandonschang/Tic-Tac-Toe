def display_board(board):
	board = list(board)
	print('\n'*10)
	print(f'\n')
	print(f' {board[1]} | {board[2]} | {board[3]} ')
	print('___________')
	print(f'\n {board[4]} | {board[5]} | {board[6]} ')
	print('___________')
	print(f'\n {board[7]} | {board[8]} | {board[9]} ')

def player_input():
	player1 = input('\nPlayer 1, would you like to be X or O? ').upper()
	while (player1 != 'X' and player1 != 'O'):
		player1 = input('Invalid selection. Player 1, would you like to be X or O? ').upper()
	print(f'\nPlayer 1, you will be {player1}.')
	if player1 == 'X':
		print(f'\nPlayer 2, you will be O.\n')
		return ('X','O')
	else:
		print(f'\nPlayer 2, you will be X.\n')
		return ('O','X')

def place_marker(board, marker, position):
	board[position] = marker	

def win_check(board, mark):
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or			#across the top
		(board[4] == mark and board[5] == mark and board[6] == mark) or 			#across the middle
		(board[7] == mark and board[8] == mark and board[9] == mark) or 			#across the bottom
		(board[1] == mark and board[4] == mark and board[7] == mark) or				#down the left
		(board[2] == mark and board[5] == mark and board[8] == mark) or				#down the middle
		(board[3] == mark and board[6] == mark and board[9] == mark) or 			#down the right
		(board[1] == mark and board[5] == mark and board[9] == mark) or				#diagonal left to right
		(board[3] == mark and board[5] == mark and board[7] == mark))				#diagonal right to left			

import random
def choose_first():
	first = random.randint(1,2)
	print(f'\nPlayer {first}, you will go first! \n')
	return first

def space_check(board,position):
	return board[int(position)] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	while True:
		try:
			position = int(input('What space do you want to place your marker in (1-9)? '))
		except:
			print('Invalid response. ')
		else:
			if int(position) in range(1,10):
				if space_check(board,position):
					return int(position)
					break
				else:
					print(f'Space {position} is already taken.\n')
			else:
				print('Invalid response. ')

def replay():
	response = input('Do you want to play again? ').lower()
	return 'y' in response

print('Welcome to Tic-Tac-Toe!\n')
print('The format of the board will be a 3x3 grid, where the positions correllate to the numbers on a phone.\n')
print('Here is the grid with the positions numbered for reference: \n')
print(' 1 | 2 | 3 ')
print('___________')
print('\n 4 | 5 | 6 ')
print('___________')
print('\n 7 | 8 | 9 ')

while True:
	
	#set up game
	board = [' ']*10
	player1, player2 = player_input()

	turn = choose_first()
	game_on = True

	while game_on:

		if turn == 1:
			display_board(board)
			position = player_choice(board)
			place_marker(board, player1, position)

			if win_check(board, player1):
				display_board(board)
				print('3 in a row! Congratulations Player 1! \n')
				game_on = False

			else:
				if full_board_check(board):
					display_board(board)
					print('Tie game, board is full. Better luck next time! \n')
					break
				else:
					turn = 2

		else:
			display_board(board)
			position = player_choice(board)
			place_marker(board, player2, position)

			if win_check(board, player2):
				display_board(board)
				print('3 in a row! Congratulations Player 2! \n')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('Tie game, board is full. Better luck next time! \n')
					break
				else: 
					turn = 1

	if not replay():
		break