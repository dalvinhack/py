a=int(input())
s=0;
if (a%2==0):
    s=s+1;
    a=a//10;
if (a%2==0):
    s=s+1;
    a=a// 10;
if (a%2==0):
    s=s+1;
print(s)
