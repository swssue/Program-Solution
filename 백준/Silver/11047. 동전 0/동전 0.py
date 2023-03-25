import sys

N,K = map(int,sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
for coin in reversed(coins):
    if K//coin != 0:
        cnt+=K//coin
        K = K%coin
print(cnt)