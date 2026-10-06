def solution(keyinput, board):
    
    # 1. 일단 가운데(0,0)에서 시작
    x = 0
    y = 0
    
    # 2. 벽이 x, y 각각 적용되어야
    # (아마 나누기 2해서 몫만 두기)
    x_wall = board[0] // 2
    y_wall = board[1] // 2
    
    for key in keyinput : 
        # y가 up 움직일 때,
        if key == 'up' :
            if y < y_wall :
                y = y + 1
        # y가 down 움직일 때,
        if key == 'down' :
            if y > -1 * y_wall : 
                y = y - 1
                
        # x 가 left로 움직일 때,
        if key == 'left' :
            if x > -1 * x_wall :
                x = x - 1
                
        # x 가 right로 움직일 때,
        if key == 'right' :
            if x < x_wall :
                x = x + 1
    
    
    answer = [x , y]
    return answer