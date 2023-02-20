import sys
 
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
        
        ## if out of bounds return 0 
        if x_coord < 0 or y_coord < 0:
            return 0
        
        ## If out of bounds return 0
        if x_coord > cols - 1 or y_coord > rows - 1:
            return 0
        
        ## If obstacle return 0 
        if self.grid[y_coord][x_coord] == -1:
            return 0
        
        ## If piece return 1 piece is represented by -2
        if self.grid[y_coord][x_coord] == -2:
            return 1
        
        ## If empty cell return -1 and continue empty cell is 0
        else:
            return -1
        
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
        pieces_attack = 0
        
        if super().check_valid(super().move_up(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_up(self.x_coord, self.y_coord), self.rows, self.cols)
        
        if super().check_valid(super().move_down(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_down(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_left(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_left(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_right(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_right(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols)
        
        if super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols)
            
        
        return pieces_attack
    
# x = King(1, 1, 8, 8, ((-2,-2, -2),(-1, -2, -1),(-2, -2, -2)))
# print(x.all_moves())        
 
class Rook(Piece): ## model up down left and right when hit obstacle stop. 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        
        counter = 0
        while super().check_valid(super().move_up(self.x_coord, self.y_coord - counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_up(self.x_coord, self.y_coord - counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_up(self.x_coord, self.y_coord - counter), self.rows, self.cols)
                break
            counter += 1
        
        counter = 0
        while super().check_valid(super().move_left(self.x_coord - counter, self.y_coord), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_left(self.x_coord - counter, self.y_coord), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_left(self.x_coord - counter, self.y_coord), self.rows, self.cols)
                break
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_down(self.x_coord, self.y_coord + counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_down(self.x_coord, self.y_coord + counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_down(self.x_coord, self.y_coord + counter), self.rows, self.cols)
                break
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_right(self.x_coord + counter, self.y_coord), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_right(self.x_coord + counter, self.y_coord), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_right(self.x_coord + counter, self.y_coord), self.rows, self.cols)
                break
            counter += 1
            
        return pieces_attack
    
# x = Rook(0, 0, 3, 3, ((-2,-1, -2),(0, -2, -1),(-2, -1, -2)))
# print(x.all_moves())
 
class Bishop(Piece): ## model diagonal up down left and right stop when hit obstacle
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        
        counter = 0
        while super().check_valid(super().move_top_right(self.x_coord + counter, self.y_coord - counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_top_right(self.x_coord + counter, self.y_coord - counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_top_right(self.x_coord + counter, self.y_coord - counter), self.rows, self.cols)
                break
            counter += 1
        
        counter = 0
        while super().check_valid(super().move_top_left(self.x_coord - counter, self.y_coord - counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_top_left(self.x_coord - counter, self.y_coord - counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_top_left(self.x_coord - counter, self.y_coord - counter), self.rows, self.cols)
                break
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_bottom_right(self.x_coord + counter, self.y_coord + counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_bottom_right(self.x_coord + counter, self.y_coord + counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_bottom_right(self.x_coord + counter, self.y_coord + counter), self.rows, self.cols)
                break
            counter += 1
            
        counter = 0
        while super().check_valid(super().move_bottom_left(self.x_coord - counter, self.y_coord + counter), self.rows, self.cols) != 0:
            if (super().check_valid(super().move_bottom_left(self.x_coord - counter, self.y_coord + counter), self.rows, self.cols)) == 1:
                pieces_attack += super().check_valid(super().move_bottom_left(self.x_coord - counter, self.y_coord + counter), self.rows, self.cols)
                break
            counter += 1
            
        return pieces_attack
    
# x = Bishop(1, 1, 3, 3, ((-1,0, -2),(-2, 0, -1),(-2, -1, -2)))
# print(x.all_moves())
 
class Queen(Piece): ## A queen is a rook and bishop 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        rook = Rook(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        bishop = Bishop(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        pieces_attack += rook.all_moves()
        pieces_attack += bishop.all_moves()
        
        return pieces_attack
    
# x = Queen(0, 0, 3, 3, ((-1,-2, -2),(-2, 0, -2),(-2, -1, -2)))
# print(x.all_moves())
 
class Knight(Piece): ## Knight hard code all 8 moves 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        
        if super().check_valid(super().move_right(self.x_coord, self.y_coord - 2), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_right(self.x_coord, self.y_coord - 2), self.rows, self.cols)
        
        if super().check_valid(super().move_up(self.x_coord + 2, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack == super().check_valid(super().move_up(self.x_coord + 2, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_down(self.x_coord + 2, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_down(self.x_coord + 2, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_right(self.x_coord, self.y_coord + 2), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_right(self.x_coord, self.y_coord + 2), self.rows, self.cols)
            
        if super().check_valid(super().move_left(self.x_coord, self.y_coord + 2), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_left(self.x_coord, self.y_coord + 2), self.rows, self.cols)
            
        if super().check_valid(super().move_down(self.x_coord - 2, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_down(self.x_coord - 2, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_up(self.x_coord - 2, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_up(self.x_coord - 2, self.y_coord), self.rows, self.cols)
        
        if super().check_valid(super().move_left(self.x_coord, self.y_coord - 2), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_left(self.x_coord, self.y_coord - 2), self.rows, self.cols)
            
        return pieces_attack
        
# x = Knight(0, 0, 3, 3, ((0,0, 0), (-1,-1, -1), (0, -2, 0)))
# print(x.all_moves())
 
class Ferz(Piece): ## Ferz hardcode all 4 moves 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        
        if super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_top_right(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_top_left(self.x_coord, self.y_coord), self.rows, self.cols)
            
        if super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_bottom_right(self.x_coord, self.y_coord), self.rows, self.cols)
        
        if super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols) != -1:
            pieces_attack += super().check_valid(super().move_bottom_left(self.x_coord, self.y_coord), self.rows, self.cols)
            
        return pieces_attack
        
# x = Ferz(1, 1, 3, 3, ((-1,0, -2), (-1,-1, -1), (-1, -2, -2)))
# print(x.all_moves())
 
class Princess(Piece): ## princess is a knight and a bishop 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0
        knight = Knight(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        bishop = Bishop(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        pieces_attack += bishop.all_moves()
        pieces_attack += knight.all_moves()
        
        return pieces_attack 
    
class Empress(Piece): ## Empress is a knight and a rook 
    def __init__(self, x_coord, y_coord, rows, cols, grid):
        super().__init__(grid)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rows = rows
        self.cols = cols
        
    def all_moves(self):
        pieces_attack = 0 
        knight = Knight(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        rook = Rook(self.x_coord, self.y_coord, self.rows, self.cols, self.grid)
        pieces_attack += rook.all_moves()
        pieces_attack += knight.all_moves()
        
        return pieces_attack 
 
 
import random
#############################################################################
######## Board
#############################################################################
class Board:
    ## For each of the pieces count the number of pieces each piece attack
    def __init__(self, rows, cols, grid, enemy_pieces, curr_pieces): 
        self.rows = rows ## int representing num rows
        self.cols = cols ## int representing num cols
        self.grid = grid ## 2D array grid, obstacles = -1 and empty = 0
        self.enemy_pieces = enemy_pieces ## dic key = pos, val = type of piece
        self.curr_pieces = curr_pieces ## dic containing curr pieces     
 
    def value(self):
        worst_piece = None
        worst_piece_val = 0
        worst_piece_type = None
        board_val = 0
        
        for i, v in self.curr_pieces.items():
            if v == "King":
                king = King(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += king
                if (king > worst_piece_val):
                    worst_piece_val = king
                    worst_piece = i
                    worst_piece_type = v
                                    
            if v == "Queen":
                queen = Queen(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += queen
                if (queen > worst_piece_val):
                    worst_piece_val = queen
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Bishop":
                bishop = Bishop(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += bishop
                if (bishop > worst_piece_val):
                    worst_piece_val = bishop
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Knight":
                knight = Knight(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += knight
                if (knight > worst_piece_val):
                    worst_piece_val = knight
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Rook":
                rook = Rook(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += rook
                if (rook > worst_piece_val):
                    worst_piece_val = rook
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Ferz":
                ferz = Ferz(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += ferz
                if (ferz > worst_piece_val):
                    worst_piece_val = ferz
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Princess":
                princess = Princess(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += princess
                if (princess > worst_piece_val):
                    worst_piece_val = princess
                    worst_piece = i
                    worst_piece_type = v
                
            if v == "Empress":
                empress = Empress(i[1], i[0], self.rows, self.cols, self.grid).all_moves()
                board_val += empress
                if (empress > worst_piece_val):
                    worst_piece_val = empress
                    worst_piece = i 
                    worst_piece_type = v
                    
        return worst_piece, worst_piece_type, board_val
                
    def highest_successor(self, remove_piece, remove_piece_type):
        self.curr_pieces.pop(remove_piece)
        piece, curr_val = (-1,-1), 10000000000000
        for key, val in self.enemy_pieces.items():
            # print(piece)
            self.curr_pieces[key] = val
            self.grid[key[0]][key[1]] = -2
            replace_piece, replace_piece_type, replace_val = self.value()
            if replace_val < curr_val:
                curr_val = replace_val
                piece = key
            self.curr_pieces.pop(key)
            self.grid[key[0]][key[1]] = 0
        self.curr_pieces[remove_piece] = remove_piece_type
        # print(piece)
        return piece, curr_val
                
    
 
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
######## Implement Search Algorithm
#############################################################################
from copy import copy, deepcopy
def search(rows, cols, grid, pieces, k):
    ls = []
    for key, val in pieces.items():
        ls.append(key)
    dic_ans = dict()
    k = int(k)
    original_grid = deepcopy(grid)
    original_pieces = pieces.copy()
    curr_pieces = dict()
    for i in random.sample(range(0, len(ls)), k):
        rand_piece = ls[i]
        curr_pieces[rand_piece] = pieces[rand_piece]
        original_pieces.pop(rand_piece)
        original_grid[rand_piece[0]][rand_piece[1]] = -2
    
    current = Board(rows, cols, original_grid, original_pieces, curr_pieces)
 
    while goal_test(current, k) == False:
        # print("break")
        final_pieces, current = algo(rows, cols, original_grid, original_pieces, curr_pieces, k)
        original_grid = deepcopy(grid)
        original_pieces = pieces.copy()
        curr_pieces = dict()
        for i in random.sample(range(0, len(ls)), k):
            rand_piece = ls[i]
            curr_pieces[rand_piece] = pieces[rand_piece]
            original_pieces.pop(rand_piece)
            original_grid[rand_piece[0]][rand_piece[1]] = -2
            
    for key, val in current.enemy_pieces.items():
        final_pieces[key] = val
        grid = current.grid
        grid[key[0]][key[1]] = -2
        if goal_test(Board(rows, cols, grid, current.enemy_pieces, final_pieces), k):
            continue
        else:
            final_pieces.pop(key)
            grid[key[0]][key[1]] = 0
        
    for key, val in final_pieces.items():
        dic_ans[(chr(key[1] + 97), key[0])] = val
        
    return dic_ans
        
def algo(rows, cols, grid, pieces, curr_pieces, k):
    current = Board(rows, cols, grid, pieces, curr_pieces)
    # print(curr_pieces)
    # print(pieces)
    while (goal_test(current, k) == False):
        worst_piece, worst_piece_type, board_val = current.value()
        new_piece, new_val = current.highest_successor(worst_piece, worst_piece_type)
        # print(curr_pieces)
        # print(pieces)
        # print(new_piece)
        # print(worst_piece)
        if (new_val > board_val):
            return curr_pieces, current
        curr_pieces[new_piece] = pieces[new_piece]
        pieces[worst_piece] = curr_pieces[worst_piece]
        pieces.pop(new_piece)
        curr_pieces.pop(worst_piece)
        grid[new_piece[0]][new_piece[1]] = -2
        grid[worst_piece[0]][worst_piece[1]] = 0
        current = Board(rows, cols, grid, pieces, curr_pieces)
        # print(pieces)
    # print(curr_pieces)
    # print(pieces)
    # print(current)
    return curr_pieces, current
 
def goal_test(board, k):
    worst_piece, worst_piece_val, board_val = board.value()
    if board_val == 0 and len(board.curr_pieces) >= k:
        return True
    else:
        return False
 
#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")
 
    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]
    k = 0
    pieces = {}
 
    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    k = handle.readline().split(":")[1].strip() # Read in value of k
 
    piece_nums = get_par(handle.readline()).split()
    num_pieces = 0
    for num in piece_nums:
        num_pieces += int(num)
 
    handle.readline()  # Ignore header
    for i in range(num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = piece    
 
    return rows, cols, grid, pieces, k
 
def add_piece( comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]
 
#Returns row and col index in integers respectively
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)
 
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)
 
# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_local():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, pieces, k = parse(testcase)
    goalstate = search(rows, cols, grid, pieces, k)
    return goalstate #Format to be returned
 
print(run_local())