def solution(moves):
    x =y =0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ['G', 'R', 'L']
    d =1
    now_station = ['up', 'right', 'down','left']
    # attention : now_station index = dx & dy index

    for i in moves:
        if i == 'G':
            nx = x + dx[d]
            ny = y + dy[d]
        if i == 'R':
            d +=1
            if d > 3:
                d = 0
            print(now_station[d])
        if i == 'L':
            d -=1
            if d < 0:
                d = 3      
            print(now_station[d])
          
        x = nx
        y = ny
    return [x,y]
            
print(solution('GGGRGGG'))
