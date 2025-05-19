# 숫자 카드
from bisect import bisect_left

m = int(input())
m_list = list(map(int, input().split()))

n = int(input())
n_list = list(map(int, input().split()))

m_list.sort()
m_size = len(m_list)

for x in n_list:
    i = bisect_left(m_list, x)
    
    if i < m_size:
        if m_list[i] == x:
            print(1, end=" ")
        else:
            print(0, end = " ")
    else:
        print(0, end = " ")