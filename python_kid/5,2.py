N=int(input())
x=0
for i in range(N):
    a=int(input())
    if a%3==0 and a%9!=0:
        x=x+1
print(x)
