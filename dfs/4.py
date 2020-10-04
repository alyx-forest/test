n, m = map(int, input().split())

b = [[m*n] * m for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
b[0][0] = 1

def bfs(x, y, before):
    if x < n-1:
        if array[x + 1][y] == 1:
            bfs(x+1, y, b[x][y] + 1)
    if y < m-1:
        if array[x][y + 1] == 1:
            bfs(x, y+1, b[x][y] + 1)
    if b[x][y] > before:
        b[x][y] = before   

for i in range(n):
    for f in range(m):
        if array[i][f] == 1:
            bfs(i,f,b[i][f])

print(b[n-1][m-1])