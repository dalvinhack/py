import random
maximum = 1
N = int(input())
for i in range(N):
    k=random.randint(1,100)
    print(k)
    if k > maximum:
        maximum = k         
print(maximum)
