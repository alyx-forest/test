n, m = map(int, input().split())

result = 0
for i in range(n):
    l = list(map(int,input().split()))
    if result < min(l):
        result = min(l)

print(result)
