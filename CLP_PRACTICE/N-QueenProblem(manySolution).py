def isSafe(board,row,col,n):
    for i in range(col):
        if board[row][i]==1:
            return False


    for i,j in zip(range(row,-1,-1) , range(col,-1,-1)):
        if board[i][j] == 1:
            return False


    for i,j in zip(range (row,n,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return  False

    return True


def SolveNQueenUtil (board,col,n):
    if col >= n:
        return True

    for i in range(n):
        if isSafe(board,i,col, n):
            board[i][col] = 1

            if SolveNQueenUtil(board,col+1,n):
                return True

            board[i][col] = 0

    return False

def printSolution(n):
    board = [[0]*n for _ in range(n)]

    if not SolveNQueenUtil(board,0,n):
        print("Solution Not found for",n,"queen")
        return False

    print("Solution found for",n,"queen")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    return True


n= int(input("Enter no. of grid: \n"))
printSolution(n)