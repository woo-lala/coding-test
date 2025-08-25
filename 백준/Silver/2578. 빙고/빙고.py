bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))
    
arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))

x = [0] * 5 # 가로
y = [0] * 5 # 세로
xy = [0] * 2 #대각선
cnt = 0
ccnt = 0
answer = 0

for i in range(5):
    for j in range(5):
        
        for ii in range(5):
            for jj in range(5):
                if arr[i][j] == bingo[ii][jj]:
                    x[ii] += 1
                    y[jj] += 1
                    if ii + jj == 4:
                        xy[0] += 1
                    if ii == jj:
                        xy[1] += 1
        
        cnt = 0
        for c in x:
            if c == 5:
                cnt += 1
        for c in y:
            if c == 5:
                cnt += 1
        if xy[0] == 5:
            cnt += 1
        if xy[1] == 5:
            cnt += 1
            
        if cnt >= 3:
            answer = i * 5 + j + 1
            print(answer)
            exit(0)