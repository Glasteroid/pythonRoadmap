def check_winner(board):
    for i in range(len(board)):
        for item in board[i]:
            if board[i].count(item) == len(board) and item > 0:
                print("{} is the winner".format(item))
                return 0

        for j in range(len(board)):
            if i + 2 < len(board) and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j] and board[i + 1][j] ==  board[i + 2][j] and (board[i][j] + board[i + 1][j] + board[i + 2][j] > 0):
                print("{} is the winner".format(board[i][j]))
                return 0
                
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == board[2][2]:
            print("{} is the winner".format(board[0][0]))
            return 0
            
        elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1] == board[2][0]:
            print("{} is the winner".format(board[0][2]))
            return 0
        
        print("There is no winner.")
        return 0
                
check_winner([[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]])