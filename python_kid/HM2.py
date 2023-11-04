s=[]
N=int(input())
for i in range(N):
    a=int(input())
    s.append(a)
print(s)
b = []
for a in s:
    if s[i]%2!=0:
        b.append(a)
        b.reverse()
    if s[i]%2==0:
        b.append(a)
        b.remove(a)
print(b)
