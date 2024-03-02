def solution(keyinput, board):
    x, y = 0, 0
    for k in keyinput:
        if k == 'left' and x > -abs(int(board[0] / 2)):
            x -= 1
        elif k == 'right' and x < abs(int(board[0] / 2)):
            x += 1
        elif k == 'down' and y > -abs(int(board[1] / 2)):
            y -= 1
        elif k == 'up' and y < abs(int(board[1] / 2)):
            y += 1
    return [x, y]

