
ls = ['1','2','3','4','5','6','7','8','9']

def display_grid(ls):
	"""
    function to print the tic tac toe grid output.

    Args:
       list: The parameter list.

    Example:
    ls = ['1', '2', 'X', '4', '5', '6', '7', '8', '9']

	 1  | 2  | X
	----|----|----
	 4  | 5  | 6
	----|----|----
	 7  | 8  | 9
       
    """ 
	value = ls
	for i,v in enumerate(value):
	 	if v =="X" or v =="O":
	 		value[i] = v

	value = tuple(value)

	table = """
	player1--> X player2--> O

	 %c  | %c  | %c
	----|----|----
	 %c  | %c  | %c
	----|----|----
	 %c  | %c  | %c
	"""
	print table % value

def checkwin(ls):
	"""
    function to check winning conditions of players and return result.

    Args:
       ls: list peg elements.

    Returns:
       1 - for three adjacent pegs are matching so player 1 or 2 won.
       2 - Match Draw.
       0 - Continue match.
    """ 
	if ls[0] == ls[1] and ls[1] == ls[2]:
		return 1
	elif ls[0] == ls[3] and ls[3] == ls[6]:
		return 1
	elif ls[0] == ls[4] and ls[4] == ls[8]:
		return 1
	elif ls[1] == ls[4] and ls[4] == ls[7]:
		return 1
	elif ls[2] == ls[5] and ls[5] == ls[8]:
		return 1
	elif ls[3] == ls[4] and ls[4] == ls[5]:
		return 1
	elif ls[6] == ls[7] and ls[7] == ls[8]:
		return 1
	elif ls[2] == ls[4] and ls[4] == ls[6]:
		return 1
	elif (ls[0] != '1' and ls[1] != '2' and ls[2] != '3' and ls[3] != '4' and ls[4] != '5' and ls[5] != '6' and ls[6] != '7' and ls[7] != '8' and ls[8] != '9'):
		return 2
	else:
		return 0

def play():
	"""
    function to play the game with player 1 and 2.

    Returns:
       1 - for three adjacent pegs are matching so player 1 or 2 won.
       2 - Match Draw.
       0 - Continue match.
    """ 
	i = 0
	global player
	player = 1
	while i == 0:
		if (player % 2):
			player = 1
		else:
			player = 2

		if player == 1:
			sign = "X"
		else:
			sign = "O"

		print "Player", (player)
		pos=input('select the position 1 to 9 to place peg :')
		if ls[pos-1] == "X" or ls[pos-1] == "O":
			print "already peg presents in the place."
		else:
			ls[pos-1] = sign
		i = checkwin(ls)
		display_grid(ls)
		player = player+1
		if i==2:
			print "Match Draw"
		elif i == 1:
			print "Player", (player)-1,"won"


if __name__ == '__main__':
	"""
    main function to call play function to print result.
    
    """
	play()

