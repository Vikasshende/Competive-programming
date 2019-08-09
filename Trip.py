n=int(input("enter no of student"))
while(n!=0 and n<1000):
    s=0
    total=0
    list=[]
    for i in range(n):
        x=int(input("enter amount"))
        if(x<10000):
             list.append(x)

        else:
            print("excess amount")


    s=sum(list)
    avg=s/n
    for j in list:
        rem=avg-j
        if(rem>=0):
         total=total+rem
    print("$%.2f"%(total))
    n=int(input("enter no of student"))