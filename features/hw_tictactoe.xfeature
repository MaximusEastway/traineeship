@tictactoe
Feature: Tic-Tac-Toe

  The Tic-Tac-Toe game does the best 
  move depending on the previous human
  move. Test these moves.

  Scenario: First move
  Given we have an empty tic-tac-toe board
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O
   Then the board has a O in column 1 and row 1 on the board

  Scenario: Computer wins
  Given we have an empty tic-tac-toe board
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 2 and row 3 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 1 and row 3 on the board
    And I ask the computer to do its best move for O 
   Then the winner of the game is O

  Scenario: It's a tie
  Given we have an empty tic-tac-toe board
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 1 and row 2 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 2 and row 3 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 3 and row 1 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 3 and row 3 on the board
   Then the winner of the game is undecided