let boardDiv = document.getElementById("board");
let locked = false;

function draw(board) {
    boardDiv.innerHTML = "";

    board.forEach((val, i) => {
        let cell = document.createElement("div");
        cell.className = "cell";
        cell.innerText = val;

        cell.onclick = () => {
            if (locked) return;
            if (val !== " ") return;

            locked = true;

            fetch("/move", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({index: i})
            })
            .then(res => res.json())
            .then(data => {
                draw(data.board);

                document.getElementById("t1").innerText = data.t1?.toFixed(5);
                document.getElementById("t2").innerText = data.t2?.toFixed(5);
                document.getElementById("n1").innerText = data.n1;
                document.getElementById("n2").innerText = data.n2;

                if (data.result) {
                    document.getElementById("status").innerText = data.result;
                    locked = true;
                } else {
                    locked = false;
                }
            });
        };

        boardDiv.appendChild(cell);
    });
}

function resetGame() {
    locked = false;

    fetch("/reset")
    .then(res => res.json())
    .then(data => {
        draw(data.board);
        document.getElementById("status").innerText = "You = X | AI = O";
    });
}

fetch("/reset")
.then(res => res.json())
.then(data => draw(data.board));