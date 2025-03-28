# Pong-Game

A classic Pong game implementation in Python using the Turtle graphics library. This two-player game features paddles, a bouncing ball, and score tracking.

## Features

- Two-player gameplay
- Score tracking for both players
- Increasing ball speed as the game progresses
- Collision detection
- Smooth paddle movement
- Classic visual style

## Game Controls

- **Right Paddle**:
  - Up Arrow: Move Up
  - Down Arrow: Move Down

- **Left Paddle**:
  - W: Move Up
  - S: Move Down

## Implementation Details

### Components

- [`main.py`](main.py): Core game loop and setup
- [`paddle.py`](paddle.py): Paddle class implementation
- [`ball.py`](ball.py): Ball class with movement and collision logic
- [`scoreboard.py`](scoreboard.py): Score tracking and display

### Technical Features

- Screen dimensions: 800x600 pixels
- Paddle size: 20x100 pixels
- Ball speed increases with each paddle hit
- Score display at the top of the screen
- Automatic ball reset after scoring

## How to Play

1. Run `main.py`
2. Use the controls to move the paddles:
   - Left player uses W/S keys
   - Right player uses Up/Down arrow keys
3. Try to hit the ball with your paddle
4. Score points when your opponent misses the ball
5. The game continues indefinitely - first to reach desired score wins!

## Dependencies

- Python 3.x
- turtle (built-in library)
- time (built-in library)

## Implementation Notes

- The ball speeds up gradually as the game progresses
- Ball resets to center after each point
- Collision detection for:
  - Paddle hits
  - Wall bounces
  - Score zones
- Paddles are constrained to screen boundaries
