dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solution(nums):
    answer = 0
    n = len(nums)
    # 완전탐색, Exhaustive Search
    for i in range(n):
        for j in range(n):
            flag = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # if nums[i][j] >= nums[nx][ny] and nx >=0 and nx < n and ny >=0 and ny <n: This code occur error about 'out of range'
                if nx >=0 and nx < n and ny >=0 and ny <n and nums[i][j] >= nums[nx][ny]:
                    flag =False
                    break
            if flag == True:
                answer +=1

    return answer

print(solution([[10,20,50,30,20], [20,30,50,70,90], [10,15,25,80,35], [25,35,40,50,90], [33,22,55,65,55]]))
# answer = 6
