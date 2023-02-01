# 창고 털기
# n = 창고 개수, arr = 창구 음식량
# 인접한 창고는 털지 못한다. 최댓값은?

n = int(input())
arr = list(map(int, input().split()))
d = [0] * 100

d[0] = arr[0]
d[1] = max(d[0], arr[1])

for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])
