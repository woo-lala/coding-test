#92341
def solution(fees, records):
    answer = []
    memo = dict()
    
    for record in records:
        time, num, status = record.split(" ")
        hh, mm = map(int, time.split(":"))
        
        if num not in memo:
            memo[num] = (hh, mm, 0, status)
        else:
            if status == 'OUT':
                start = memo[num][0] * 60 + memo[num][1]
                end = hh * 60 + mm
                temp = memo[num][2] + (end - start)
                memo[num] = (hh, mm, temp, status)
            elif status == 'IN':
                temp = memo[num][2]
                memo[num] = (hh, mm, temp, status)
    
    answer = []
    for key in memo:
        hh, mm, time, status = memo[key]
        start = hh * 60 + mm
        end = 23*60+59
        if status == 'IN':
            time = time + (end-start)
            
        print(hh, mm, time, status)
        if fees[0] >= time:
            answer.append((key, fees[1]))
        else:
            time = (time - fees[0])/fees[2]
            if int(time) >= time:
                time = int(time)
            else:
                time = int(time) + 1
            fee = fees[1] + time * fees[3]
            answer.append((key, fee))
    
    answer.sort()
    result = []
    for num, fee in answer:
        result.append(fee)
    
    return result