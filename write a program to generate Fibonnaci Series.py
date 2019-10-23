#fibonnaci series
term=10
n1=0
n2=1
count=2
if term<=0:
    print("enter positive number:")
elif(term==1):

    print(n1)
else:
    print('fibonnaci series upto',term)
    print(n1,n2,end=', ')
    while count<term:
        n=n1+n2
        print(n,end=',')
        n1=n2
        n2=n
        count+=1


#sort method to find the fibonnaci series
# term=10
# n1=0
# n2=1
# count=2
# print("fibonnaci series upto ",term)
# print(n1,n2,end=',')
# while  term>count:
#     n=n1+n2
#     print(n,end=',')
#     n1=n2
#     n2=n
#     count+=1

