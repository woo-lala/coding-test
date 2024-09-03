H, W = map(int, input().split())
block = list(map(int, input().split()))

l = 0
result = 0

while l < W-1: 
    biggest = max(block[l+1:])
    h = block[l]
    
    if biggest >= h:
        for i in range(l+1,W):
            if block[i] >= h:
            # if block[i] == biggest:
                l = i
                break
            result += (h-block[i])
    else:
        h = biggest
        for i in range(l+1,W):
            if block[i] == biggest:
                l = i
                break
            result += (h-block[i])
        
print(result)


# 7 8
# 7 1 1 5 0 5 2 7

# 3 6
# 5 4 1 3 1 2

# 5 5
# 1 0 3 2 4