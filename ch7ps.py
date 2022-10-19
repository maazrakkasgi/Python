#!  multiplication program

'''n=int(input("Enter the no:"))
for i in range(1,11):
    print(str(n)+ "X"+ str(i) + "="+ str(i*n))'''

    #2 
'''l1=["Harry","sohan","sachin","rahul"]
for name in l1:
    if name.startswith("s"):
        print("Hello "+name)'''

 #3 multiplication program using while loop
'''n=int(input("Enter the NUmber"))
i=0
while i<11:
    print(str(n)+"X"+str(i)+"="+str(i*n))
    i=i+1'''

    #4 prime or not prime
'''n=int(input("Enter the no:\n"))
prime=True
for i in range(2,n):
    if(n%i==0):
        prime=False
        break
if(prime):
    print("The number is prime")
else:
    print("The number is not prime")'''

    #5 sum of n antural no

'''num=int(input("Enter the no"))
i=0
n=0
while i<=num:
    n=n+i
    i=i+1
print(n)'''
#6 factorial of no
'''n=int(input("ENter the no:\n"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"The factorial of given no is :{fact}")'''#f string
#7 star patterns 
'''n=int(input("Enter the no that star should print that no of time:\n"))
for i in range(n):
    print("*"*(i+1))'''
#8 star pattern
'''n=3
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))'''
#9 print multiplication table in revese order
'''n=int(input("Enter the NUmber"))
i=10
while i<=10 and i>0:
    print(str(n)+"X"+str(i)+"="+str(i*n))
    i=i-1'''