import sys
from collections import deque

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, grid):
        self.grid = grid
        
    def move_up(self, x_coord, y_coord):
        return x_coord, y_coord - 1
    
    def move_down(self, x_coord, y_coord):
        return x_coord, y_coord + 1
    
    def move_right(self, x_coord, y_coord):
        return x_coord + 1, y_coord
    
    def move_left(self, x_coord, y_coord):
        return x_coord - 1, y_coord
    
    def move_top_right(self, x_coord, y_coord):
        return x_coord + 1, y_coord - 1
    
    def move_top_left(self, x_coord, y_coord):
        return x_coord - 1, y_coord - 1
    
    def move_bottom_right(self, x_coord, y_coord):
        return x_coord + 1, y_coord + 1
    
    def move_bottom_left(self, x_coord, y_coord):
        return x_coord - 1, y_coord + 1
    
    def check_valid(self, move, rows, cols): ## check against grid to see if the val is correct
        x_coord, y_coord = move
        
        if x_coord < 0 or y_coord < 0:
            return False
        
        if x_coord > cols - 1 or y_coord > rows - 1:
            return False
            
        if self.grid[y_coord][x_coord] == -1:
            return False
        
        else:
            return True
        
# x = Piece()
# print(x.check_valid(x.move_bottom_left(9, 9), 11, 11))

class King(Piece):
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self): ## model a 8 moves avail by king (hardcode all 8)
        all__possible_moves = []
        
        if super().check_valid(super().move_up(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_up(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
        
        if super().check_valid(super().move_down(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_down(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_left(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_left(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_right(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_right(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_top_right(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_top_left(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_bottom_right(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
        
        if super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_bottom_left(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        
        return all__possible_moves
    
# x = King(0, 0, 8, 8, ((0,0),(-1, -1)))
# print(x.all_moves())        

class Rook(Piece): ## model up down left and right when hit obstacle stop. 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        
        counter = 0
        while super().check_valid(super().move_up(self.x_coord, self.y_coord - counter), self.rows, self.cols):
            x, y = super().move_up(self.x_coord, self.y_coord - counter)
            all__possible_moves.append((x, y))
            counter += 1
        
        counter = 0
        while super().check_valid(super().move_left(self.x_coord - counter, self.y_coord), self.rows, self.cols):
            x, y = super().move_left(self.x_coord - counter, self.y_coord)
            all__possible_moves.append((x, y))
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_down(self.x_coord, self.y_coord + counter), self.rows, self.cols):
            x, y = super().move_down(self.x_coord, self.y_coord + counter)
            all__possible_moves.append((x, y))
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_right(self.x_coord + counter, self.y_coord), self.rows, self.cols):
            x, y = super().move_right(self.x_coord + counter, self.y_coord)
            all__possible_moves.append((x, y))
            counter += 1
            
        return all__possible_moves
    
# x = Rook(0,0, 2, 2, ((0,0), (-1,-1)))
# print(x.all_moves())

class Bishop(Piece): ## model diagonal up down left and right stop when hit obstacle
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        
        counter = 0
        while super().check_valid(super().move_top_right(self.x_coord + counter, self.y_coord - counter), self.rows, self.cols):
            x, y = super().move_top_right(self.x_coord + counter, self.y_coord - counter)
            all__possible_moves.append((x, y))
            counter += 1
        
        counter = 0
        while super().check_valid(super().move_top_left(self.x_coord - counter, self.y_coord - counter), self.rows, self.cols):
            x, y = super().move_top_left(self.x_coord - counter, self.y_coord - counter)
            all__possible_moves.append((x, y))
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_bottom_right(self.x_coord + counter, self.y_coord + counter), self.rows, self.cols):
            x, y = super().move_bottom_right(self.x_coord + counter, self.y_coord + counter)
            all__possible_moves.append((x, y))
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_bottom_left(self.x_coord - counter, self.y_coord + counter), self.rows, self.cols):
            x, y = super().move_bottom_left(self.x_coord - counter, self.y_coord + counter)
            all__possible_moves.append((x, y))
            counter += 1
            
        return all__possible_moves
    
    
# x = Bishop(0, 0, 2, 2, ((0,0), (-1,-1)))
# print(x.all_moves())

class Queen(Piece): ## A queen is a rook and bishop 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        rook = Rook(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        bishop = Bishop(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        all__possible_moves.extend(bishop.all_moves())
        all__possible_moves.extend(rook.all_moves())
        
        return all__possible_moves
    
# x = Queen(0, 0, 2, 2, ((0,0), (-1,-1)))
# print(x.all_moves())

class Knight(Piece): ## Knight hard code all 8 moves 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        
        if super().check_valid(super().move_right(self.x_coord, self.y_coord - 2), self.rows, self.cols):
            x, y = super().move_right(self.x_coord, self.y_coord - 2)
            all__possible_moves.append((x, y))
        
        if super().check_valid(super().move_up(self.x_coord + 2, self.y_coord), self.rows, self.cols):
            x, y = super().move_up(self.x_coord + 2, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_down(self.x_coord + 2, self.y_coord), self.rows, self.cols):
            x, y = super().move_down(self.x_coord + 2, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_right(self.x_coord, self.y_coord + 2), self.rows, self.cols):
            x, y = super().move_right(self.x_coord, self.y_coord + 2)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_left(self.x_coord, self.y_coord + 2), self.rows, self.cols):
            x, y = super().move_left(self.x_coord, self.y_coord + 2)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_down(self.x_coord - 2, self.y_coord), self.rows, self.cols):
            x, y = super().move_down(self.x_coord - 2, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_up(self.x_coord - 2, self.y_coord), self.rows, self.cols):
            x, y = super().move_up(self.x_coord - 2, self.y_coord)
            all__possible_moves.append((x, y))
        
        if super().check_valid(super().move_left(self.x_coord, self.y_coord - 2), self.rows, self.cols):
            x, y = super().move_left(self.x_coord, self.y_coord - 2)
            all__possible_moves.append((x, y))
            
        return all__possible_moves
        
# x = Knight(0, 0, 3, 3, ((0,0, 0), (-1,-1, 0), (0, 0, 0)))
# print(x.all_moves())

class Ferz(Piece): ## Ferz hardcode all 4 moves 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        
        if super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_top_right(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_top_left(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        if super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_bottom_right(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
        
        if super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols):
            x, y = super().move_bottom_left(self.x_coord, self.y_coord)
            all__possible_moves.append((x, y))
            
        return all__possible_moves
        
# x = Ferz(0, 0, 2, 2, ((0,0), (-1,-1)))
# print(x.all_moves())

class Princess(Piece): ## princess is a knight and a bishop 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        knight = Knight(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        bishop = Bishop(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        all__possible_moves.extend(bishop.all_moves())
        all__possible_moves.extend(knight.all_moves())
        
        return all__possible_moves 
    
class Empress(Piece): ## Empress is a knight and a rook 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        all__possible_moves = []
        knight = Knight(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        rook = Rook(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        all__possible_moves.extend(rook.all_moves())
        all__possible_moves.extend(knight.all_moves())
        
        return all__possible_moves 

#############################################################################
######## Board
#############################################################################
class Board:
    ## Find all attacking places by the pieces and then mark them as -1 (ie cannot go)
    def __init__(self, rows, cols, grid, enemy_pieces): 
        self.rows = rows ## int representing num rows
        self.cols = cols ## int representing num cols
        self.grid = grid ## 2D array grid, obstacles = -1 and empty = 1
        self.enemy_pieces = enemy_pieces ## arrays of type of piece and pos
        self.attacked_places = []
        
        for i in self.enemy_pieces:
            self.grid[i[1][0]][i[1][1]] = -1
            
        
        for i in self.enemy_pieces:
            if i[0] == "King":
                king = King(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(king.all_moves())
                
            if i[0] == "Queen":
                queen = Queen(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(queen.all_moves())
                
            if i[0] == "Bishop":
                bishop = Bishop(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(bishop.all_moves())
                
            if i[0] == "Knight":
                knight = Knight(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(knight.all_moves())
                
            if i[0] == "Rook":
                rook = Rook(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(rook.all_moves())
                
            if i[0] == "Ferz":
                ferz = Ferz(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(ferz.all_moves())
                
            if i[0] == "Princess":
                princess = Princess(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(princess.all_moves())
                
            if i[0] == "Empress":
                empress = Empress(i[1][1], i[1][0], self.rows, self.cols, grid)
                self.attacked_places.extend(empress.all_moves())
                
        ## mark all attacked grid as -1        
        for i in self.attacked_places:
            if self.grid[i[1]][i[0]] != -1:
                self.grid[i[1]][i[0]] = -1
                    
    def get_grid(self):
        return self.grid

# x = Board(5,5,[[0,0,0,0,0],[0,0,-1,-1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [["Bishop", (2,1)], ["Rook", (2, 3)]])
# print(x.get_grid())

#############################################################################
######## State
#############################################################################
class State:
    ## A state takes in a board and the position of the attacker
    def __init__(self, board, x_coord, y_coord):
        self.board = board
        self.x_coord = x_coord
        self.y_coord = y_coord
        
#############################################################################
######## Node
#############################################################################
class Node:
    ## A node takes in a state, parent node, actions taken and path cost
    def __init__(self, state):
        self.state = state
        self.parent_node = None
        self.action = []
        self.path_cost = 0
        
        
#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    board = Board(rows, cols, grid, enemy_pieces) ## Populate board 
    frontier = deque() ## deque O(1) for remove front 
    visited =  [[0 for j in range(cols)] for i in range(rows)] ## visited array to prevent duplicate visits 
    
    initial_state = State(board, own_pieces[0][1][1], own_pieces[0][1][0])
    visited[own_pieces[0][1][0]][own_pieces[0][1][1]] = 1
    first_node = Node(initial_state)
    frontier.append(first_node)
    
    while len(frontier) > 0:
        pop_node = frontier.popleft()
        king = King(pop_node.state.x_coord, pop_node.state.y_coord, rows, cols, grid)
        
        for valid_moves in king.all_moves():
            if visited[valid_moves[1]][valid_moves[0]] == 0:
                visited[valid_moves[1]][valid_moves[0]] = 1
                state = State(board, valid_moves[0], valid_moves[1])
                node = Node(state)
                node.parent = pop_node
                node.action.extend(pop_node.action)
                node.action.append([(chr(pop_node.state.x_coord + 97), pop_node.state.y_coord), (chr(valid_moves[0] + 97), valid_moves[1])])
                if goal_test(state, goals):
                    # print(node.action)
                    return node.action
                else:
                    frontier.append(node)
    return []
        

def goal_test(state, goals):
    for i in goals:
        if i[1] == state.x_coord and i[0] == state.y_coord:
            return True
        else:
            False    
#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

#############################################################################
######## Main function to be called
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# To return: List of moves
# Return Format Example: [[('a', 0), ('a', 1)], [('a', 1), ('c', 3)], [('c', 3), ('d', 5)]]
def run_BFS():    
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves

# print(run_BFS())