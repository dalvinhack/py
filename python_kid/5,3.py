N=int(input())
n=30000
for i in range(N):
    a=int(input())
    if N%10==4 and a<n:
        a=n
print(a)
