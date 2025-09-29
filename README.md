# Snake Game 🐍

A classic Snake Game implementation using Python's Turtle graphics library. Control the snake to eat food and grow longer while avoiding collisions with walls and your own body!

![Snake Game](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Game Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

## Features ✨

- **Intuitive Controls**: Use arrow keys for movement and space bar to pause
- **Score System**: Track current score and highest score
- **Progressive Difficulty**: Game speed increases as your snake grows longer
- **Collision Detection**: Walls and self-collision end the game
- **Visual Feedback**: Colorful snake segments and food with clean UI
- **Game Reset**: Automatic reset when collisions occur

## Game Elements 🎮

- **Snake Head**: Brown circle that turns red when moving
- **Body Segments**: Red squares that follow the head
- **Food**: Green squares that randomly appear
- **Score Display**: White text showing current and highest scores
- **Playing Area**: 600x600 black background game board

## How to Play 🎯

1. **Movement**:
   - `↑ Up Arrow` - Move upward
   - `↓ Down Arrow` - Move downward  
   - `← Left Arrow` - Move left
   - `→ Right Arrow` - Move right
   - `Space Bar` - Pause movement

2. **Objective**:
   - Eat green food squares to grow longer
   - Each food gives 10 points
   - Avoid hitting walls or your own body
   - Achieve the highest score possible

3. **Game Over**:
   - When snake hits the wall
   - When snake collides with its own body
   - Game automatically resets with score set to zero

## Installation & Requirements 🛠️

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes built-in with Python)

### Running the Game
```bash
# Download the snake.py file and navigate to its directory
python snake.py
