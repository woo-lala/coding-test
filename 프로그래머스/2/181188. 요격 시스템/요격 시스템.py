def solution(targets):
    targets.sort(key=lambda x: x[1])
    cnt = 0
    before = 0 # 초기화
    for s, e in targets:
        if s >= before: # 새로운 요격 필요 else에서 이 요격으로 격추할 수 있는 것들 포함한다
            cnt += 1
            before = e
    return cnt