#pyramid
def pattern(n):
    k= n 
    for i in range(0,n):
        for j in range(0,k):
            print(end="")
        k = k-1
        for j in range(0, i+1):
            print("*", end="")
        print("\r")
pattern(5)

# RIGHT START PATTEN
def pattern(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("*", end="")
        print("\r")
    for i in range (n,0,-1):
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
pattern(5)
