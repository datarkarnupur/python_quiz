board= ["1","2","3",
        "4","5","6",
        "7","8","9"]
def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
player = "x"
for turn in range(9):

    display_board()

    print("player",player)
    position = int(input("enter position(1-9): "))

    board[position - 1] = player

    #check winner
    if (board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]or
        board[0]==board[1]==board[2]):

        display_board()
        print("player",player,"wins!")
        break
    #change player
    if player == "x":
        player= "0"
    else:
        player = "x" 


else:
    display_board()
    print("game draw!")
           

