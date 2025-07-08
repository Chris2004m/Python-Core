# Simple Tic Tac Toe game

def print_board(board):
    print("\n".join([" ".join(row) for row in board]))
    print()


def check_winner(board):
    lines = []
    # rows
    lines.extend(board)
    # cols
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] != "-" and all(cell == line[0] for cell in line):
            return line[0]
    return None


def is_draw(board):
    return all(cell != "-" for row in board for cell in row)


def main():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current = "X"
    while True:
        print_board(board)
        move = input(f"Player {current}, enter row and column (1-3 1-3): ")
        try:
            r, c = map(int, move.split())
            r -= 1
            c -= 1
            if r not in range(3) or c not in range(3) or board[r][c] != "-":
                print("Invalid move. Try again.")
                continue
            board[r][c] = current
        except Exception:
            print("Invalid input. Enter two numbers between 1 and 3.")
            continue
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    main()
