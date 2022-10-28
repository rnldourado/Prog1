a,b,k = int(input()),int(input()),int(input())
for s in range(1, k+1):
    if(s % a == 0) and (s % b == 0):
        print(s)
