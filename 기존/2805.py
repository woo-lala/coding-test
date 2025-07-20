#2805

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = max(arr)

while s <= e:
    mid = (s+e) // 2
    
    temp = 0
    for x in arr:
        if x > mid:
            temp += (x-mid)
    
    if temp >= M:
        result = mid
        s = mid + 1
    else:
        e = mid - 1
        
print(result)