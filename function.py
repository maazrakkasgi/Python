# functions: it is group of statemnt which is used to perfirm specific task.

'''def percent(marks):
    p=(sum(marks))/4
    return p
marks1=[44,56,76,67]
percentage1=percent(marks1)
marks2=[56,76,78,90]
percentage2=percent(marks2)
print(percentage1,percentage2)'''
# greeting 

'''def greet(name):
    print("goog mornihg" +name)
greet("maaz")'''

#default argument

'''def greet(name="stranger"):
    print("goog mornihg ," +name)
greet("maaz")
greet()'''

#recurssion factorial;

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)    
    
n1=int(input("Enter the no :"))
f= factorial(n1)
print(f)  

