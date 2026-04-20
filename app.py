from flask import Flask, render_template, request, jsonify
import math
import time

app = Flask(__name__)

board = [" " for _ in range(9)]

# Metrics
minimax_nodes = 0
alphabeta_nodes = 0


def check_winner(b, p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in win)


# ---------- MINIMAX ----------
def minimax(b, is_max):
    global minimax_nodes
    minimax_nodes += 1

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


# ---------- ALPHA-BETA ----------
def alphabeta(b, is_max, alpha, beta):
    global alphabeta_nodes
    alphabeta_nodes += 1

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
                val = alphabeta(b, False, alpha, beta)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = alphabeta(b, True, alpha, beta)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


# ---------- BEST MOVE ----------
def best_move():
    global minimax_nodes, alphabeta_nodes

    # Reset counters
    minimax_nodes = 0
    alphabeta_nodes = 0

    # --- Minimax ---
    start = time.time()
    minimax(board[:], True)
    minimax_time = time.time() - start

    # --- Alpha-Beta ---
    start = time.time()
    alphabeta(board[:], True, -math.inf, math.inf)
    alphabeta_time = time.time() - start

    # Use Alpha-Beta for actual move
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            val = alphabeta(board, False, -math.inf, math.inf)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i

    return move, minimax_time, alphabeta_time, minimax_nodes, alphabeta_nodes


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
        return jsonify(board=board, result="You Win 🎉")

    if " " not in board:
        return jsonify(board=board, result="Draw 🤝")

    ai, t1, t2, n1, n2 = best_move()

    if ai != -1:
        board[ai] = "O"

    if check_winner(board, "O"):
        return jsonify(board=board, result="AI Wins 🤖",
                       t1=t1, t2=t2, n1=n1, n2=n2)

    if " " not in board:
        return jsonify(board=board, result="Draw 🤝",
                       t1=t1, t2=t2, n1=n1, n2=n2)

    return jsonify(board=board, result="",
                   t1=t1, t2=t2, n1=n1, n2=n2)


@app.route("/reset")
def reset():
    global board
    board = [" " for _ in range(9)]
    return jsonify(board=board)




if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)