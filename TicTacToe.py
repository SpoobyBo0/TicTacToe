# Printar put spelplanen i terminalen
def print_board(board):
    for row in board:
        print(*row)


# Hur varje plats kommer se ut
y = ["-"]
# Gör bara en lista med nmr så man kan ha vilken sotrlek på spelplanen som man vill
list = []
for i in range(3, 10000):
    list.append(i)

# Lägger till spelplanan i listan board
board = []

t = 2

while t > len(board):

    x = int(input("Vilken spelplan vill du köra? "))

    if x < 3:
        print("Spelplanen måste minst vara 3x3 ")

    if x in list:

        for _ in range(x):
            board.append(y * x)

# En fuction som kollar om någon har vunnit
def won():
    for row in board:
        if all(x == "w" for x in row):
            return True
        if all(x == "o" for x in row):
            return True
    for i in range(len(board)):
        if all(board[j][i] == "w" for j in range(len(board))):
            return True
        if all(board[j][i] == "o" for j in range(len(board))):
            return True


# Function för att kolla om det blir lika
def tie():
    return False


# Hela spelet
def game(player_turn):

    print_board(board)

    while True:
        print("Player " + player_turn + ", Your Turn")
        row = input("Select row: ")
        vertical = input("Select a vertical row: ")

        if row and vertical != "x" or "o":
            row = int(row) - 1
            vertical = int(vertical) - 1

            board[row][vertical] = player_turn

        print_board(board)

        if won():
            print("Player " + player_turn + " Win!")
            spela_igen = input("Do you want to play r? y/n: ")
            if spela_igen == "n".capitalize():
                break

        elif tie():
            print("The game was a tie")
            spela_igen = input("Do you want to play agian? y/n: ")
            if spela_igen == "n".capitalize():
                break

        if player_turn == "w":
            player_turn = "o"
        else:
            player_turn = "w"


game("w")
