# Nim Game with Q-Learning AI Agent

## About the Project

This project implements the classic game of **Nim**, where players take turns removing stones from heaps. The player who removes the last stone wins.

A reinforcement learning agent based on **Q-Learning** is trained to play Nim optimally. The project is structured to allow human interaction against the trained AI agent.

The implementation uses Python and is designed to be simple, educational, and extendable for those interested in reinforcement learning and game AI.

---

## About the Game: Nim

- Nim is a mathematical strategy game.
- There are several heaps (or piles) of stones.
- Two players alternate turns.
- On each turn, a player selects one heap and removes **one or more stones** from it.
- The player who removes the **last stone** wins the game.

---

```yaml

---

## How the Code Works

### Nim Environment (`nim_env.py`)

- Maintains the current state of heaps.
- Implements game rules, valid moves, and game termination logic.
- Provides methods like `reset()`, `step(action)`, and `get_valid_actions()`.

### Q-Learning Agent (`q_learning_agent.py`)

- Learns an optimal policy for Nim through trial and error.
- Maintains a Q-table mapping `(state, action)` pairs to expected rewards.
- Updates the Q-values based on the reward received and future expected rewards.

### Policy (`policy.py`)

- Implements an epsilon-greedy policy:
  - With probability `epsilon`, selects a random valid action (exploration).
  - Otherwise, selects the best known action based on current Q-values (exploitation).

### Main (`main.py`)

- Trains the agent by running multiple episodes of Nim.
- After training, allows a human player to play against the trained agent.
- The human player inputs heap index and number of stones to remove.
- The AI responds with its moves.
- The game ends when all stones are removed, declaring the winner.

---

## How to Run

1. Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/macOS
   .venv\Scripts\activate      # On Windows

2.Install dependencies
pip install -r requirements.txt
```


