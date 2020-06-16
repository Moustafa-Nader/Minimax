from copy import deepcopy
from random import randint

class State:
    def __init__(self, board, pos, score):
        self.board = board  # 3x3 list
        self.pos = pos      # [I, J]
        self.score = score
        self.empty_pos = []

    def print(self):
        board_copy = deepcopy(self.board)
        board_copy[self.pos[0]][self.pos[1]] = '(' + str(self.score) + ')'
        print('\t'.join(str(x) for x in board_copy[0]))
        print('\t'.join(str(x) for x in board_copy[1]))
        print('\t'.join(str(x) for x in board_copy[2]))

'''
[
    [1, 0, 0]
    [0, 0, 1]
    [1, 0, 1]
]
'''

def valid_pos(pos):
    return pos[0] >= 0 and pos[0] < 3 and pos[1] >= 0 and pos[1] < 3

def copy(state):
    board = [
        state.board[0].copy(),
        state.board[1].copy(),
        state.board[2].copy()
    ]
    empty_pos = state.empty_pos.copy()
    ret = State(board, state.pos.copy(), state.score)
    ret.empty_pos = empty_pos
    return ret


def move_left(state):
    s = copy(state)
    s.pos[1] -= 1
    if not valid_pos(s.pos):
        return None
    s.empty_pos = state.pos
    s.score += s.board[s.pos[0]][s.pos[1]]
    return s

def move_right(state):
    s = copy(state)
    s.pos[1] += 1
    if not valid_pos(s.pos):
        return None
    s.empty_pos = state.pos
    s.score += s.board[s.pos[0]][s.pos[1]]
    return s

def move_up(state):
    s = copy(state)
    s.pos[0] -= 1
    if not valid_pos(s.pos):
        return None
    s.empty_pos = state.pos
    s.score += s.board[s.pos[0]][s.pos[1]]
    return s


def move_down(state):
    s = copy(state)
    s.pos[0] += 1
    if not valid_pos(s.pos):
        return None
    s.empty_pos = state.pos
    s.score += s.board[s.pos[0]][s.pos[1]]
    return s

def max_children(state):
    return [
        move_left(state),
        move_right(state),
        move_up(state),
        move_down(state)
    ]

def min_children(state):
    c1 = copy(state)
    c1.board[c1.empty_pos[0]][c1.empty_pos[1]] = 1

    c2 = copy(state)
    c2.board[c2.empty_pos[0]][c2.empty_pos[1]] = 0

    c3 = copy(state)
    c3.board[c3.empty_pos[0]][c3.empty_pos[1]] = -1

    return [c1, c2, c3]

def generate_state():
    board = [
        [randint(-1 , 1), randint(-1 , 1), randint(-1 , 1)],
        [randint(-1 , 1), randint(-1 , 1), randint(-1 , 1)],
        [randint(-1 , 1), randint(-1 , 1), randint(-1 , 1)]
    ]
    return State(board, [2, 0], 0)

def input_state():
    board = [
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())]
    ]
    return State(board, [2, 0], 0)