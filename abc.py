i=1
while(i<=5):
    j=1
    while(j<6-i):
        print(' ',end="")
        j+=1
    k=1
    while(k<2*i):
        if(k%2==0):
            print('3',end=' ')
        else:
            print('4',end=' ')
        k+=1
    i+=1
print("end")