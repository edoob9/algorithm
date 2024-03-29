# Finding a specific part in an array

def solution(map):
    cnt = 0
    x = y =0
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    n = len(map)
    print(len(dx))
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                for d in range(len(dx)):
                    
                    nx = i + dx[d]
                    ny = j + dy[d]
                    
                    if nx >= 0 and nx <n and ny >=0 and ny<n and map[nx][ny]==0:
                        cnt += 1
                        # To avoid revisiting previously visited rows and columns
                        map[nx][ny] = 100
    print(map)          
    return cnt

print(solution([[0,0,0,0,0], [0,1,0,0,0], [0,0,0,1,0], [0,0,0,0,0], [0,0,0,0,0]]))
# [[100, 100, 100, 0, 0], [100, 1, 100, 100, 100], [100, 100, 100, 1, 100], [0, 0, 100, 100, 100], [0, 0, 0, 0, 0]]
# 14
