from state import *
from random import randint
from gui import *
import time
def minmax(state, depth, alpha, beta, is_max, first):
    if depth == 0:
        return state.score

    if is_max:
        mx = -1e9
        mx_child = None
        children = max_children(state)
        for child in children:
            if child is None:
                continue
            val = minmax(child, depth - 1, alpha, beta, False, False)
            if val > mx:
                mx = val
                mx_child = child
            alpha = max(alpha, mx)
            if beta <= alpha:
                break
        if first:
            return mx_child
        return mx
    else:
        mn = 1e9
        children = min_children(state)
        for child in children:
            val = minmax(child, depth, alpha, beta, True, False)
            mn = min(mn, val)
            beta = min(beta, mn)
            if beta <= alpha:
                break
        return mn

def solve(state, max_moves, max_depth):
    return minmax(state, min(max_moves, max_depth), -1e9, 1e9, True, True)

if __name__ == "__main__":

    print('1- Randomly generate level')
    print('2- Input level')
    if int(input()) is 2:
        print('Write 9 numbers representing 3x3 grid')
        state = input_state()
    else:
         state = generate_state()

    min_score = int(input('Minimum level goal\t: '))
    max_moves = int(input('Maximum number of moves\t: '))
    max_depth = int(input('Maximum depth\t\t: '))

    mx = -1
    state.print()
    print('---------------------------------------------')
    window.deiconify()
    min_score_widget.set(str(min_score))
    max_moves_widget.set(str(max_moves))
    max_depth_widget.set(str(max_depth))

    while max_moves:
        b[state.pos[0]][state.pos[1]]["disabledbackground"] = "white"
        state.print()
        state = solve(state, max_moves, max_depth)
        max_moves -= 1
        mx = max(mx, state.score)
        pos = state.empty_pos
        state.board[pos[0]][pos[1]] = randint(-1 , 1)
        state.print()
        
        display_state(state)
        t[state.pos[0]][state.pos[1]].set(str(state.score))
        time.sleep(0.3)
        b[state.pos[0]][state.pos[1]]["disabledbackground"] = "blue"
        window.update()
  


        print('---------------------------------------------')
    
    print()
    print('=============================================')
    max_score_widget.set(str(mx))
    final_score_widget.set(str(state.score))
    if min_score <= mx:
        print('WINNER!!')
        win_display()
    else:
        print('FAIL')
        fail_display()
    print()
    print('MAX Score\t: ' , mx)
    print('FINAL Score\t: ' , state.score)
    print('=============================================')
    window.mainloop()