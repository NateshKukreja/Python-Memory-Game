import random

def create_board(size):
    '''int->list (of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    board = [None] * size

    letter = 'A'
    for i in range(len(board) // 2):
        board[i] = letter
        board[i + len(board) // 2] = board[i]
        letter = chr(ord(letter) + 1)
    random.shuffle(board)
    return board


def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i + 1)), end=' ')


def wait_for_player():
    '''(None)->None
    Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass


def play_game(board):
    '''(list of str)->None

    plays the game
    '''
    flag2 = False
    discovered = [False] * len(board)

    # create a new list to contain the stars but uses .append() and .join() to make it into string
    starBoard = []
    for i in range(len(board)):
        starBoard.append(' *')
    starBoard = "  ".join(starBoard)
    print(starBoard)
    # this creates a new list that contains the stars, but in a list using .split()
    starCount = starBoard.split()
    # this will count the amount of variables found. Starts at the length of the list/2 because there are
    # counter will subtract 1 after every move
    counter = (len(board)) / 2

    # creates a list (converts to string) the length of the board to print numbers under the list starBoard
    numberSel = []
    for j in range(len(board)):
        numberSel.append(str(j + 1))
    numberSel = "  ".join(numberSel)
    print(numberSel)
    # counts the amount of guesses the user uses
    guessCount = 0

    # while statement to keep looping as long as the user has not found all the combinations
    while (counter > 0):

        
        # subtracts 1 because a list starts at 0
        A = int(input("Enter your first location")) - 1
        B = int(input("Enter your second location")) - 1


        # used to ensure that the inputs should be within the length of the board
        if ((A >= len(board)) or (A < 0) or (B < 0) or (B >= (len(board)))):
            print("You have made an invalid choice, please try again")
        elif ((A == B)):
            print("You have entered the same number, please enter again.")
        elif ((discovered[A] == True) or (discovered[B] == True)):
            print("This location is discovered, please try again.")
        

        # ensures that the input given hasn't been disovered
        else:
            if ((board[A] == board[B]) and ((discovered[A] == False) and (discovered[B] == False))):
                starCount[A] = board[A]
                starCount[B] = board[B]
                discovered[A] = True
                discovered[B] = True
                flag2 = True  # this is used to subtract 1 from the variable counter
                printBoard(board, starCount, discovered, A, B, numberSel)
                guessCount = guessCount + 1

            # used to let the user go again because the list variables do not match
            elif (board[A] != board[B]):
                starCount[A] = board[A]
                starCount[B] = board[B]
                printBoard(board, starCount, discovered,A, B, numberSel)
                guessCount = guessCount + 1

            # subtracts 1 from the counter and then returns the flag as false
            if (flag2 == True):
                counter = counter - 1
                flag2 = False
    print("You won the game!")
    print("It took you " + str(guessCount) + " guesses!")
    print("That is " + str(guessCount - (len(board) / 2)) + " more than the best possible")

#prints the board with the discovered values
def printBoard(board, starCount, discovered, A, B, numberSel):

    '''
    (list, list, bool, int, int, list) --> (list, list) of str

    takes in the list of the board, list of the starCount, the discovered boolean, the user input
    as well as the number list and outputs the board with the displayed values at the user
    inputed values (list index) as well as the number list under it
    '''
    
    numberSel = "".join(numberSel)
    #if the values matches, prints the matches value with stars
    if ((discovered[A] == True) and (discovered[B] == True)):
        for i in range(len(board)):
            print(starCount[i] + " ", end="")
        print()
        print(numberSel)
    else:
        for i in range(len(board)):
            print(starCount[i] + " ", end="")
        print()
        print(numberSel)

    #uses this function to ensure the player has looked at the screen long enough
    wait_for_player()
    #if nothing matches, makes the board all stars
    for i in range(len(board)):
        if (discovered[B] == False):
            starCount[i] = "*"

size = int(input("How many cards do you want to play with? \nEnter an even number between 2 and 52"))
while ((size > 52) or (size < 2) or (size % 2 != 0)):
    print("Invalid input. The size is greater than 52 or is less than 2. Please enter an even integer between 2 and 52")
    size = int(input("What is the size would you like the board to be (2 to 52)"))

board = create_board(size)
play_game(board)
