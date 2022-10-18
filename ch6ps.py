#1 write a program to find greatest of four numbrs entered by user

'''n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())

if (n1 > n2) and (n1>n3) and (n1>n4):
    print(n1,"is greatest")
elif (n2 > n1) and (n2>n3) and (n2>n4):
    print(n2,"is greatest")
elif (n3 > n2) and (n3>n1) and (n3>n4):
    print(n3,"is greatest")
else:
    print(n4,"is greatest")'''

    # student pass or fail for 4 subjects

'''s1=int(input("Enter the marks of subject 1\n"))
s2=int(input("Enter the marks of subject 2\n"))
s3=int(input("Enter the marks of subject 3\n"))
s4=int(input("Enter the marks of subject 4\n"))

total=(s1 + s2+ s3+ s4)
print(total)
avg=(total)/4
print(avg,"%")

if(s1<35) or (s2<35) or (s3<35) or(s4<35):
    print("fail")
elif(avg<35):
    print("fail")
else:
    print("pass")'''

    #3


'''
text=input("Enter the comment\n")

if("make a lot of money " in text):
    spam= True
elif("buy now" in text):
    spam=True
elif("subscribe this " in text):
    spam= True
elif("click this"in text):
    spam=TRUE
else:
    spam=False

if(spam):
    print("the statement is spam")
else:
    print("the statement is not spam")    '''

#4 program to find whther a given username contains less than 10 charecters or not
'''a=input("Enter user name\n")
if(len(a)>=10):
    print(" it has more than 10 charecters")
else:
    print("it has less than 10 charecters")    '''

#5 

'''names=["Maaz","Adil","Sajeed","Vinit","Avi"]
n=input("Enter the name to check\n")

if(n in names):
    print("Name is present")
else:
    print("Name is not present")'''
    
    #6

'''marks=int(input("enter the percentage\n"))

if(marks>90 and marks<=100):
    print("EX")
elif(marks>80 and marks<=90):
    print("A")
elif(marks>70 and marks<=80):
    print("B") 
elif(marks>60 and marks<=70):
    print("C")
elif(marks>50 and marks<=60):    
    print("D")
else:
    print("Fail")'''    

#7
'''a=input("enter the post")

if("Harry"in a or "harry"in a or "HARRY"in a):
    print("they are talking about Harry")'''