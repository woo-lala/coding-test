T = int(input())
for _ in range(T):
    arr = input()
    K = int(input())
    memo = dict()
    possible = set()
    
    n = len(arr)
    
    for i in range(n):
        if arr[i] not in memo:
            memo[arr[i]] = [i]
        else:
            memo[arr[i]].append(i)
    
    for k in memo:
        m = len(memo[k])
        value = memo[k]
        if m < K:
            continue
        for i in range(m):
            if (i + K - 1) >= m:
                break
            a = value[i+K-1] - value[i] + 1
            if a not in possible:
                possible.add(a)
                
    if len(possible) == 0:
        print(-1)
    else:
        print(str(min(possible)) + " " + str(max(possible)))