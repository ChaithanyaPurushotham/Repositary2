Num=int(input("Enter the number"))

if(Num==1):
    print(Num,"is a prime numner")
if(Num>1):
    for i in range(2,Num+1):
        if(Num%i == 0):
            if(i==Num):
                print(Num,"is a prime number")
            else:
                print(Num,"is not a prime number")
                break
        else:
            if(i==Num):
                print(Num,"is a prime number")
                break
            
