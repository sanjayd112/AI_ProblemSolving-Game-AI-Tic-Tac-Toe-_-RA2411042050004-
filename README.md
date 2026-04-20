# 🎮 Tic-Tac-Toe AI (Minimax vs Alpha-Beta Pruning)

This is a web-based Tic-Tac-Toe game built using Flask (Python), HTML, CSS, and JavaScript. The player competes against an unbeatable AI that uses Minimax and Alpha-Beta Pruning algorithms.

---

## 📊 Features

- Interactive web-based UI 🎨  
- AI opponent that never loses 🤖  
- Real-time gameplay  
- Displays:
  - ⏱ Execution Time comparison  
  - 🔢 Nodes explored comparison  
- Shows result: You Win / AI Win / Draw  
- Restart game option 🔄  

---

## 🧠 Algorithms Used

### Minimax Algorithm
- Explores all possible moves
- Guarantees optimal decision
- Slower due to full search

### Alpha-Beta Pruning
- Optimized Minimax
- Cuts unnecessary branches
- Faster and more efficient

---

## ⚖️ Performance Metrics

Example output:

Minimax Time: 0.00002  
Alpha-Beta Time: 0.00001  
Minimax Nodes: 4  
Alpha-Beta Nodes: 7  

Meaning:
- ⏱ Time → speed of decision making  
- 🔢 Nodes → number of game states explored  

Lower values = better performance

---

## 📂 Project Structure

tic-tac-toe-ai/
│
├── app.py  
├── requirements.txt  
│
├── templates/  
│   └── index.html  
│
├── static/  
│   ├── style.css  
│   └── script.js  

---

## 🚀 Live Demo

The project is deployed and accessible online:

👉 https://ai-problemsolving-game-ai-tic-tac-toe.onrender.com


---
## ▶️ How to Run Locally

pip install -r requirements.txt

python app.py

Open in browser:
http://localhost:5000

---

## 🌐 Deployment

Deployed using Render (cloud platform).

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

---





