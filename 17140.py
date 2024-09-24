#17140

r,c,k = map(int, input().split())
A = []

for _ in range(3):
    A.append(list(map(int, input().split())))


row_dict = dict()
col_dict = dict()
r_len = 3
c_len = 3

def remake(arr):
    s = []
    dictionary = dict()
    for x in arr:
        if x == 0:
            continue
        else:
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] += 1
    
    sorted_data = sorted(dictionary.items(), key = lambda x : (x[1], x[0]))
    
    for num, cnt in sorted_data:
        s.append(num)
        s.append(cnt)
        
    return s
    
def function(arr, row, column):
    global r_len
    global c_len
    
    for i in range(row):
        arr[i] = remake(arr[i])
        row_dict[i] = len(arr[i])

    column = max(row_dict.values())

    for i in range(row):
        if len(arr[i]) < column:
            for _ in range(column - len(arr[i])):
                arr[i].append(0)
    
    r_len, c_len = row, column
    return arr


def exchange(arr):
    
    row = len(arr)
    col = len(arr[0])
    
    B = [[0] * row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            B[i][j] = arr[j][i]
    return B


time = 0

while True:
    
    if r_len >= r and c_len >= c:
        if A[r-1][c-1] == k:
            print(time)
            break
    
    if time > 100:
        print(-1)
        break
    
    if r_len >= c_len:
        A = function(A, r_len, c_len)
    else:
        A = exchange(A)
        
        A = function(A, c_len, r_len)
        r_len, c_len = c_len, r_len
        A = exchange(A)
    
    time += 1