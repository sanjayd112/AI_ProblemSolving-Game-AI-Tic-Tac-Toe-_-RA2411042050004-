from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

board = [" " for _ in range(9)]

def check_winner(b, p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in win)

def minimax(b, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

def best_move():
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            val = minimax(board, False)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i

    return move

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global board
    idx = request.json["index"]

    if board[idx] != " ":
        return jsonify(board=board)

    board[idx] = "X"

    if check_winner(board, "X"):
        return jsonify(board=board)

    ai = best_move()
    if ai != -1:
        board[ai] = "O"

    return jsonify(board=board)

@app.route("/reset")
def reset():
    global board
    board = [" " for _ in range(9)]
    return jsonify(board=board)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)