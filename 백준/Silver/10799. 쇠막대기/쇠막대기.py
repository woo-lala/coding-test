arr = input()

n = len(arr)
stack = list()

stack.append(arr[0])
result = 0

for i in range(1, n):
    if arr[i] == ')':
        if arr[i-1] == '(': #레이저
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
    else:
        stack.append('(')

print(result)