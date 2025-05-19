#create a dictionary with the multiple of first 10 numbers




def dict(list):
    result={}
    

    for i in range(1,10):
        count=0

        for num in list:
            if num % i==0:
                count+=1
        result[i]=count
    return result

    



n=int(input("enter the number of items in the list:"))
list=[]
for i in range(n):
    list.append(int(input("enter the item")))
print(list)
output=dict(list)

print(output)
    