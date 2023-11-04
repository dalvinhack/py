a = int(input())
s=0
while a != 0:
    a = int(input())
    if a%2==0:
        s = s+1
        continue
    if a == 0:
        break
print(s)
