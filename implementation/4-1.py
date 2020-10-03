n = int(input())
list = input().split()

x = 1
y = 1

for c in list:
    if c == 'L' and y != 1:
        y -= 1
    if c == 'R' and y != n:
        y += 1
    if c == 'U' and x != 1:
        x -= 1
    if c == 'D' and x != n:
        x += 1

print(x,y)