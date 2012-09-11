# Helper function definitions with docstrings for the
# I have omitted the details of the implementation here.

def find_neighbors(Board, x,y):
    """ returns a list of all neighbor squares.
        A neighbor square is represented as a tuple:
        (i,j)
        Example:
        Input: x=1, y=2, Board = see Section 2.2
        Output: [(1,1),(0,2),(2,2)]
    """

def two_next_squares_available(x,y):
    """ Checks whether the square Board(x,y) has two
        consecutive free squares next to it.
        Example:
        Input: x=2, y=2, Board = [[ 0, 'X', 'X'],
                                  [ 0, 'O', 'X'],
                                  [ 0,  0,  'O']]
        Output: True

    """

def get_board():
    """ Returns the board of the current game.
    """

# Target function representation
X = [x1,x2,x3,x4,x5,x6] = 6*[0]
W = [w1,w2,w3,w4,w5,w6] = 6*[0]
V = [x*w for x,y in zip(x,w)]
Board = get_board()
 
# Evaluate the board by examining every square.
for x in range(3):
    for y in range(3):
        neighbors = find_neighbors(x,y)

        for j,k in neighbors:
            # If the square is a naught
            if Board[x][y] == 'O':
                # ... and its neighbor is a naught
                if Board[j][k] == 'O':
                    x1 += 1
                # If the square is empty, check whether
                # there exists two empty squares in line
                elif not Board[j][k]:
                    x5 += 1
                    if is_two_neighbors_available(x,y):
                        x3 += 1
            # Or if the square is a cross
            if Board[x][y] == 'X':
                # ... and its neighbor is a cross
                if Board[j][k] == 'X':
                    x2 += 1
                # If the square is empty, check whether
                # there exists two empty squares in line
                elif not Board[j][k]:
                    x6 += 1
                    if is_two_neighbors_available(x,y):
                        x4 += 1

#Update the weights
V = LMS_weight_update(X,W,V)