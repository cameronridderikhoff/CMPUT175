# CMPUT 175 Winter 2013 Lab 3 Exercise 2
# This program is used solve a maze
#With help from Cameron Ridderikhoff

# A Stack implementation

class Stack:
    def __init__(self):
        self.__items = []
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        return self.__items.pop()
    def peek(self):
        return self.__items[len(self.__items)-1]
    def isEmpty(self):
        return len(self.__items) == 0
    def size(self):
        return len(self.__items)
    
# This function takes a string as input, and returns a list of the ints in the
# string.  This is used by the Maze constructor.
def parse_line(line):
    line_contents = line.split()
    i = 0
    while i < len(line_contents):
        line_contents[i] = int(line_contents[i])
        i = i + 1
    return line_contents


# Classes for working with mazes

# Represents a Maze, with any number of squares.
class Maze:
    # Creates a new maze:
    def __init__(self, file_name):
        file = open(file_name, "r")
        maze_size = parse_line(file.readline())
        self.__squares = []
        
        for x in range(0, maze_size[0]):
            self.__squares.append([0] * maze_size[1])
        
        x = 0
        while x < maze_size[0]:
            y = 0
            while y < maze_size[1]:
                square = MazeSquare(x, y)
                self.__squares[x][y] = square
                y = y + 1
            x = x + 1
                
        start_location = parse_line(file.readline())
        self.__start = self.__squares[start_location[0]][start_location[1]]
        
        finish_location = parse_line(file.readline())
        self.__finish = self.__squares[finish_location[0]][finish_location[1]]
        
        for line in file:
            legal_move = parse_line(line)
            self.__squares[legal_move[0]][legal_move[1]].add_move(
                self.__squares[legal_move[2]][legal_move[3]])
        
    # Returns the start square of this maze:
    def get_start_square(self):
        return self.__start
    
    # Returns True if the square is the finish square, and False otherwise:
    def is_finish_square(self, square):
        if square == self.__finish:
            return True
        else:
            return False

# Represents a single square in a maze.
class MazeSquare:
    
    def __init__(self, x, y):
        self.__moves = []
        self.__x = x
        self.__y = y
        
    def add_move(self, neighbor):
        self.__moves.append(neighbor)
        
    def get_legal_moves(self):
        return self.__moves
    
    def get_location(self):
        return (self.__x, self.__y)
    
def main():
    maze=Maze("unsolvable_maze.txt")
    stack=Stack()
    stack.push(maze.get_start_square())
    while not stack.isEmpty():
        current=stack.pop()
        if maze.is_finish_square(current):
            print("The solution has been found!")
            return
        else:
            move_list=current.get_legal_moves()
            for move in move_list:
                stack.push(move)
    print("No solution was found.")
main()