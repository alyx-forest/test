loc = input()

alpha = ['0','a','b','c','d','e','f','g','h']
x = int(loc[1])
y = alpha.index(loc[0])
count = 0

if x + 2 <= 8 and y + 1 <= 8:
    count+=1
if x + 2 <= 8 and y - 1 >= 1:
    count+=1
if x + 1 <= 8 and y + 2 <= 8:
    count+=1
if x + 1 <= 8 and y - 2 >= 1:
    count+=1
if x - 1 >= 1 and y + 2 <= 8:
    count+=1
if x - 1 >= 1 and y - 2 >= 1:
    count+=1
if x - 2 >= 1 and y + 1 <= 8:
    count+=1
if x - 2 >= 1 and y - 1 >= 1:
    count+=1

print(count)