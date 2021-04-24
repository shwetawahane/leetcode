'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#for point A , traverse until you reach a point (n-1,k) where k ranges from 0 to n-1
#for point B, traverse until you reach a point(0,k) where k ranges from 0 to n-1

'''
For B(X,Y):check nodes: 

above me (x-1,y) 
dig rite (x-1,y+1)
dig left (x-1,y-1)

For A(X,Y):check nodes: 

below me (x+1,y) 
dig rite (x+1,y+1)
dig left (x+1,y-1)

'''

def A_findNext(x,y):
    A_below = board[x+1][y]
    n = len(board)
    
    if y-1 < 0:
        A_dig_left = 0
    else:
        A_dig_left = board[x+1][y-1]
    
    if y+1 > n-1:
        A_dig_rite = 0
    else:
        A_dig_rite = board[x+1][y+1]
    
    if A_below > A_dig_rite:
        if A_below > A_dig_left:
            return A_below, x+1, y
        else:
            return A_dig_left, x+1, y-1
    else:
        if A_dig_rite > A_dig_left:
           return A_dig_rite, x+1, y+1
        else:
            return A_dig_left, x+1, y-1

def B_findNext(x,y):
    n = len(board)
    
    B_above    = board[x-1][y] 
    
    if y+1 > n-1:
        B_dig_rite = 0
    else:
        B_dig_rite = board[x-1][y+1]
    
    if y-1 <0:
        B_dig_left = 0
    else:
        B_dig_left = board[x-1][y-1]
    
    
    if B_above > B_dig_rite:
        if B_above > B_dig_left:
            return B_above, x-1, y
        else:
            return B_dig_left, x-1, y-1
    else:
        if B_dig_rite > B_dig_left:
           return B_dig_rite, x-1, y+1
        else:
            return B_dig_left, x-1, y-1

def maxPathSum(board, p, q):
    n = len(board)
    xA = 0
    yA = p
    
    xB = n-1
    yB = q
    sumA = 0
    sumB = 0
    
    for i in range(n):
        A_point = board[xA][yA]
        sumA += A_point
        
        if xA+1 < n:
            valueA, xA, yA = A_findNext(xA,yA)
        
        B_point = board[xB][yB]
        sumB+=B_point
        
        if xB-1 >=0:    
            B_point = board[xB][yB]
        valueB, xB, yB = B_findNext(xB,yB)

    max_sum = max(sumA, sumB)
    print(sumA, sumB)
    print(max_sum)
    
        


        
board = [[9,4,7],[2,1,3],[1,4,2]]
p=2
q=1
maxPathSum(board,p,q)
    
    
    
