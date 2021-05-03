# CJ Hilty & Daniel Park's Code Review

*Written as of 10:22 am on 5/2/21*

## What parts of the implementation still need to be done, and what barriers still exist to completing the implementation?

As of right now, we have the base functions ready to be coded and the concept behind all our functions and variables nailed down, however, we still need to implement those functions to make and manipulate the blocks in the tetris board. The output of the game right now is only a blank white screen.

## What bugs or technical problems have been particularly tricky to tackle, and is there an insight or approach that would help address this?

We've been struggling a little bit on how we wanted to rotate the block and check if there will be conflicts when turning it, but we figured the easiest way of rotating the block is to set hard coded turns for each type of block and switch between the listed rotations as necessary. As for conflicts, we would check if there would be any color conflicts (or wall conflicts) within the rotated block and the surrounding blocks to see if it is possible to rotate the blocks. If there is a conflict, we would dissallow the rotation.

## Is the code working as intended? How do we know?

As of right now, there is no way for us to check if the code is working as intended (in `tetris_piece.py` and `tetris_board.py` because the output is all in `tetris_game.py`). However, we can soon overcome this by adding the board and pieces objects on the main `tetris_game.py` to see if they will work. We are also struggling to figure out ways to run test cases on our current functions since the output would be on a board. If possible, we would like to go over possible ways to write test cases for our project.

## How is the code’s performance? Is this acceptable for the ways in which it is intended to be used, and if not, what are possible workarounds?

As said before, all our output (as of right now) is a blank white screen and we can't see if this is the way it is intended to be used. However, we would like to report back on this question tomorrow during the check-in.
