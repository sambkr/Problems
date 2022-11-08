import numpy as np

#%% Functions
def Check(n,board,row,col):
    # Check row

    if np.count_nonzero(board[row,:]) > 1:
        return False
    
    # Check diagonals
    for i in range(1,n):
        if row+i < n and col+i < n:
            if board[row+i,col+i] > 0:
                # print('Queen found at',str(row-i),str(col+i))
                return False
        if row-i > -1 and col-i > -1:
            if board[row-i,col-i] > 0:
                # print('Queen found at',str(row-i),str(col+i))
                return False
        if row+i < n and col-i > -1:
            if board[row+i,col-i] > 0:
                # print('Queen found at',str(row-i),str(col+i))
                return False
        if row-i > -1 and col+i < n:
            if board[row-i,col+i] > 0:
                # print('Queen found at',str(row-i),str(col+i))
                return False
    print('Successful placement at',str(row),str(col))
    return True
            
def Solve(n,board,col):
    if col == n:
        print('You are finished!')
        print(board)
        input('More solutions? Hit enter:')
        return
    else:
        for row in range(n):
            # Place the queen
            board[row,col] = 1
            print('Trying row',str(row))

            # If this is a valid square, keep the placement and try the next column
            if Check(n,board,row,col):
                col +=1
                print('Next col is',str(col))
                Solve(n,board,col)
                # If we are at a dead-end, backtrack and remove the queen
                print('Trying different row')
                col -=1
                board[row,col] = 0
            # else, remove that queen
            else:
                board[row,col] = 0
        print('Col',str(col))
        # board[:,col] = 0
        print('returning')
        return 

#%% 
n = 8
board = np.zeros(shape=(n,n))
col = 0

Solve(n,board,col)
