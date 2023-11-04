s = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a%5==0 or a%9==0:
        s=s+1
        continue
print(s)
