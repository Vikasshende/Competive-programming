def Problem(x):
 count=1
 while( x != 1):
    if( x%2 == 0):
        x= x / 2
        count = count+1

    else:
        x = 3 * x + 1
        count = count +1
 return count

x,y=input().split(' ')
x=int(x)
y=int(y)
max =Problem(x)

while(x<=y):
    max1=Problem(x)
    x=x+1
    if(max>=max1):
      max=max

    else:
      max=max1
print(max)