n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

count = 0
cx = 0
cy = 0
d = [[0] * m for _ in range(n)]

def dfs(x, y):
    if array[x][y] == 0:
        d[x][y] = 1
        if x < n-1:
            if array[x+1][y] == 0:
                dfs(x+1,y)
        if y < m-1:
            if array[x][y+1] == 0:
                dfs(x,y+1)    


for i in range(n):
    for f in range(m):
        if d[i][f] == 0 and array[i][f] == 0:
            dfs(i, f)
            count += 1

print(count)


