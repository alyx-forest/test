N, M, K = map(int, input().split())
array = [int(i) for i in input().split()]
count = 0
sum = 0
array.sort()
second = array[-2]

for i in range(M):
    if count < K:
        sum += max(array)
        count += 1
    else:
        sum += second
        count = 0

print(sum)