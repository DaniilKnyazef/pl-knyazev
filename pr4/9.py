N = int(input())
S = 0
C1 = 0
C2 = 1
for i in range(2,N+1):
   S = C1 + C2
   C1 += 1
print(S)   
