size=int(input())
for row in range(size,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
    