N = int(input("Enter number of queens: "))


def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end=" ")
		print('\n')


def isSafe(board, row, col):

	for i in range(col):
		if board[row][i] == 1:
			return False

	for i, j in zip(range(row, -1, -1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	for i, j in zip(range(row, N, 1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True


def solveNQUtil(board, col):

	if col >= N:
		return True

	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQUtil(board, col + 1) == True:
				return True

			board[i][col] = 0
	return False


def solveNQ():

    board = []
    for i in range(N+1):
        temp = []
        for i in range(N+1):
            temp.append(0)
        board.append(temp)


    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

solveNQ()
