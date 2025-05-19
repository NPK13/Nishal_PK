# generate a series of odd number 


def series(n):
    if n%2 ==0:
        n=n-1
    
    for i in range(n):
        res=2 * i + 1
        print(res,end="  ")




n=int(input("enter the number: "))

series(n)