#Question 2
length=    int(input("Enter Shape Length                          : "))
secondlast=int(input("Enter Second Last Number Of Your Student Id : "))
last=      int(input("Enter Second Last Number Of Your Student Id : "))
def main():
    
    i=1
    while(i<=length-1):
        j=length-1
        while(j>=i):
            print(" ",end=' ')
            j-=1
        k=1
        while(k<i*2):
            if(k==i):
                print(secondlast,end=' ')
            else:
                print(last,end=' ')
            k+=1
    
        i+=1
        print("")
    for z in range(1,(length*2)):
        print(secondlast,end=' ')
    print("")
    a=1
    while(a<=length-1):
        b=2
        while(b<=a+1):
            print(" ",end=' ')
            b+=1
        c=length-1
        while(c>=a):
            if(c==a):
                print(secondlast,end=' ')
            else:
                print(last,end=' ')
            c-=1
        d=length-2
        while(d>=a):
            print(last,end=' ')
            d-=1
        a+=1
        print()
main() 