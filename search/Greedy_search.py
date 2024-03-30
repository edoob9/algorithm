'''
    ver.1
'''

N=1260
cnt=0
charge = [5,50, 500, 10, 100]
charge.sort(reverse=True)

print(charge)
# [500, 100, 50, 10, 5]

for i in charge:
    num_ = N//i
    N -= num_*i
    cnt+=num_
    
print(cnt)

'''
    ver.2
'''
'''
첫째 줄에 색을 칠해야 하는 문제의 수 N (1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에 N개의 문자가 공백 없이 순서대로 주어진다. 
각 문자는 i번째 문제를 어떤 색으로 칠해야 하는지를 의미하며, R은 빨간색, B는 파란색을 나타낸다. 그 외에 다른 문자는 주어지지 않는다.

모든 문제를 원하는 색으로 칠할 때까지 필요한 작업 횟수의 최솟값을 출력
'''

# 단, 그리디 알고리즘은 모두 최적의 해를 확실하게 찾을 수 없다.
import sys
N = int(sys.stdin.readline())
colors = input()
count = 0
dict = {'B':0, 'R':0}
precolor = ''
for color in colors:
    if color != precolor:
        dict[color]+=1
    precolor=color

count = dict['R']+1 if dict['B']>dict['R'] else dict['B']+1
# if dict['B']>dict['R']:
#     count = dict['R']+1 
# else:
#     dict['B']+1

print(count)
