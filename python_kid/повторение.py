b=0
c=0
for i in range(100):
    a=int(input())
    if a<301:
        b=b+a
        c=c+1
    else:
        print("NO")
    if a==0:
        print(b/c)

    
