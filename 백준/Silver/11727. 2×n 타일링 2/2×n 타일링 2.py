n = int(input())

dp = [0] * (n+1)

if n == 1:
    print(1)
else:
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    print(dp[n] % 10007)