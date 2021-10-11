n = int(input())
g = n - 1
for i in range(g,-1,-1):
    for k in range(n-g,0,-1):
        print(k,end=" ")
    print(" ")
    g = g-1
       


    

   