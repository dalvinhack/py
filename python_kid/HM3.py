s=[]
N=int(input())
for i in range(N):
    a=int(input())
    s.append(a)
print(s)
x = max(s)
b = s.index(x)
s.insert(b,0)
print(s)
