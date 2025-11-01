N = int(input())
arr = []
MIN = 10 ** 9
MAX = 0
for _ in range(N):
    start_day, end_day = map(int, input().split())
    arr.append((start_day, end_day, end_day - start_day + 1))
    MIN = min(MIN, start_day)
    MAX = max(MAX, end_day)

graph = [0] * (MAX+1)

for start, end, days in arr:
    for d in range(days):
        graph[start+d] += 1

total_sum = 0
height = 0
width = 0
        
for i in range(MAX+1):
    if graph[i] == 0:
        total_sum += (height * width)
        height = 0
        width = 0
    else:
        height = max(height, graph[i])
        width += 1
        
total_sum += (height * width)

print(total_sum)