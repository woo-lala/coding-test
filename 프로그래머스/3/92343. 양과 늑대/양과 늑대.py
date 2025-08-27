def solution(info, edges):
    visited = [False] * len(info)
    
    cnt_wolf = 0
    cnt_sheep = 0
    
    possible = list()
    
    def backtrack(cnt_sheep, cnt_wolf):
        if cnt_sheep > cnt_wolf:
            possible.append(cnt_sheep)
        else:
            return
        
        for s, e in edges:
            if visited[s] and not visited[e]:
                visited[e] = True
                if not info[e]:
                    backtrack(cnt_sheep + 1, cnt_wolf)
                else:
                    backtrack(cnt_sheep, cnt_wolf + 1)
                visited[e] = False
                    
    if not info[0]:
        cnt_sheep += 1
    else:
        cnt_wolf += 1
    
    visited[0] = True
    backtrack(cnt_sheep, cnt_wolf)
    
    return max(possible)