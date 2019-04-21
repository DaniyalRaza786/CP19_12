s1=input("Enter First Sentence = ")
s2=input("Enter Second Sentence = ")
s1=s1.split(" ")
s2=s2.split(" ")
count=1
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            
            print("Common Word in Sentences ",count," = ",s1[i])
            count+=1