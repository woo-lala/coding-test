import collections
N = int(input())
queue = collections.deque([i for i in range(1,N+1)])
while len(queue)>1 :
  queue.popleft()
  queue.rotate(-1)
print(queue[0])