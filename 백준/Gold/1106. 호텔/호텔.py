C, N = map(int, input().split())
cost = []
plus = []

for _ in range(N):
    cost_city, plus_people = map(int, input().split())
    cost.append(cost_city)
    plus.append(plus_people)
    
MAX = C + max(plus)
MIN = min(plus)

INF = 10**9
dp = [INF] * (MAX + 1)

dp[0] = 0

#초기화
for i in range(len(cost)):
    city_cost = cost[i]
    city_plus = plus[i]
    dp[city_plus] = city_cost


for i in range(len(cost)): #도시 개수
    city_cost = cost[i]
    city_plus = plus[i]
    
    for j in range(city_plus, MAX+1):
        dp[j] = min(dp[j], dp[j-city_plus] + city_cost)
        

print(min(dp[C:]))