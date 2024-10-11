# Planet Wars Bot using Behavior Trees

This project is a Python implementation of a bot that plays **Planet Wars**, a real-time strategy game where players conquer planets and engage in interplanetary warfare. The bot is designed using **Behavior Trees** to create a reactive, strategic AI capable of competing against various test bots in different game scenarios.

## Table of Contents
- [About the Game](#about-the-game)
- [Behavior Trees](#behavior-trees)
- [Competition](#competition)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## About the Game

In **Planet Wars**, players aim to dominate the galaxy by conquering planets. Each planet produces a certain number of ships per turn, which can be sent to other planets for offensive or defensive purposes. The game consists of:
- Neutral, enemy, and player-controlled planets.
- Planets that produce ships over time, which are used to capture other planets.

The game logic, including ship production, sending ships between planets, and taking over planets, is handled by the game engine (written in Java).

## Behavior Trees

The bot is designed using a **Behavior Tree** framework. A Behavior Tree is a model of a decision-making process used to determine the actions of the bot in real-time. The tree structure allows the bot to evaluate conditions and execute actions based on the current game state. This approach provides a flexible, modular, and scalable method to handle complex game logic.

### Key Features of the Bot:
- **Reactive Decision-Making**: The bot evaluates the current game state and adjusts its actions accordingly.
- **Single Behavior Tree**: A single, modular behavior tree is used to control the bot’s actions.
- **Adaptive Strategies**: The bot dynamically changes its strategy depending on the state of the game, such as planet ownership, ship count, and enemy actions.

## Competition

To test the bot’s capabilities, it will be run against a set of test bots, each presenting unique challenges. The ultimate goal is to design a bot that can win consistently across different game maps. Additionally, a class-wide competition will be held where bots are pitted against each other in a pairwise format. The bot that wins the most matches will earn extra credit.

## Setup Instructions

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ChristyYuen/planet-wars-bot.git

## Usage

To run the bot against the game engine, follow these steps:

1. **Run the Python bot:**
    ```bash
    python bot.py
    ```

You can adjust parameters or change the bot's behavior by modifying the `behavior_tree.py` file.

