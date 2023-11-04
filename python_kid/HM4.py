s=[]
N=int(input())
for i in range(N):
    a=int(input())
    s.append(a)
print(s)
k=min(s)
while k in s:
    s.remove(k)
print(s)
    
