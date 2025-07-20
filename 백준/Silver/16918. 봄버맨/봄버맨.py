R, C, N = map(int, input().split())
graph = [list(input()) for _ in range(R)]

def get_next_state(board):
    result = [['O'] * C for _ in range(R)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                result[i][j] = '.'
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < R and 0 <= nj < C:
                        result[ni][nj] = '.'
    return result

if N == 1:
    for row in graph:
        print(''.join(row))
elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    first = get_next_state(graph)
    second = get_next_state(first)
    if N % 4 == 3:
        for row in first:
            print(''.join(row))
    else:
        for row in second:
            print(''.join(row))
