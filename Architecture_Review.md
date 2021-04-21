# PyTetrominoes
Daniel Park and CJ Hilty

## Topic

Tetrominoes are a set of simple shapes that are made out of basic squares attached side by side. They are the basic units in tetromino stacking games, such as Tetris.

This project will

## Visualization

We are building an interactive tetromino game. We will need to visualize a board for the player to stack their tetrominoes that is 10 squares wide and 25 squares tall. We will also need to visualize the tetrominoes as they accumulate on the board, and make animations for as they fall and animations for when a player clears a line. Finally, we will display the score, speed level, and high score next to the game board.

We are using PyGame to visualize our tetromino game.

## Interactivity

The user will use the left and right arrow keys to move the tetrominoes. The up and down arrow keys will be used to rotate the piece clockwise and allow the player to push the piece down when they have it in position. We are using PyGame to make the GUI for our control architecture.

## Model

The model will consist of classes for the board, the tetrominoes, and the game score. The model will handle placing the tetrominoes, choosing the next piece, detecting and removing completed lines, scoring the game, and detecting when the player loses.

## View

During the game, the player will be able to see their score, the next piece, the actual view of the game board,

The score will be calculated by the game model, and it will add ten points every time a piece is placed, as well as additional points when a line is cleared. If there is a full "TETRIS" (four lines of blocks are cleared), then 100 points will be added.

## Controller