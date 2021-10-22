from behave import *
import tictactoe as ttt
from hamcrest import *

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = ttt.EMPTY_BOARD

    assert_that(context.board, all_of(ttt.EMPTY_BOARD))


@when(u'I play X on column {col_num} and row {row_num} on the board')
def step_impl(context, col_num, row_num):
    context.board, context.winner = ttt.play(context.board, "X", int(col_num)-1, int(row_num)-1)


@when(u'I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = ttt.play_best_move(context.board, "O")


@then(u'the board has a {player} in column {col_num} and row {row_num} on the board')
def step_impl(context, player, col_num, row_num):
    board_index = (int(row_num)-1) * 3 + (int(col_num)-1)
    player_at_index = context.board[board_index]

    assert_that(player_at_index, equal_to(player))

@then(u'the winner of the game is {winner}')
def step_impl(context, winner):
    if winner in ("X", "O"):
        assert_that(context.winner, equal_to(winner))
    elif winner == "undecided":
        assert_that(context.winner, equal_to("T"))
    else:
        raise AssertionError("Unexpected outcome to winner")