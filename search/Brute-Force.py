'''
재료를 통해서 음식을 만드려고 하는 문제 = 재료당 넣을 수 있는 자료의 최대 개수 배열이 주여진다.
단, 재료들은 바로 옆에 근접한 재료는 사용하지못한다.
    test = [2,1,3,4,8,9,2,5]
    print(test[::2])
'''
import itertools

def rem_near(l,n):
    for i in range(len(l)):
        for j in range(n-1):
            if l[i][j]+ 1 == l[i][j+1]:
                l[i] = ()
                break

def solution(data):
    index = [0,1,2,3,4,5,6,7]
    cor_4 = list(itertools.combinations(index, 4))
    cor_3 = list(itertools.combinations(index, 3))
    # print(cor_3)
    # print(len(cor_4)) 
    print(rem_near(cor_3, 3))
    print(rem_near(cor_4, 4))
    # print(list(filter(lambda x: x !=(), cor_3)))
    cor_3 = list(filter(lambda x: x !=(), cor_3))
    cor_4 = list(filter(lambda x: x !=(), cor_4))
    sum_cor = list(map(lambda x:sum([data[i] for i in x]), cor_4+cor_3))
    print(sum_cor)
    #print(max(sum_cor))
    print(sorted(sum_cor, reverse=True)[0])
    return None

solution([2,1,3,4,8,9,2,5])
