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
                setTimeout(() => locked = false, 200);
            });
        };

        boardDiv.appendChild(cell);
    });
}

function resetGame() {
    locked = false;

    fetch("/reset")
    .then(res => res.json())
    .then(data => draw(data.board));
}

fetch("/reset")
.then(res => res.json())
.then(data => draw(data.board));