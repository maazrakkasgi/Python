'''#1 write a program to create a dictionary of hindi words with value as their english translation .provide user with an option to look it up!
mydict={
    'fanka':'fan',
    'dabba':'box',
    'vastu':'items'
}

print("options to choose",mydict.keys())
a=input("enter the hindi word above mention \n")
#print('your word meaning is',mydict[a])
print("the meaning of your word is " ,mydict.get(a)) #it will nt throw error if item is not present in dictionary'''

'''#2  Write a program to input eight numbers from the user and display all the unique numbers once
n1=int(input("Enter the no\n"))
n2=int(input("Enter the no\n"))
n3=int(input("Enter the no\n"))
n4=int(input("Enter the no\n"))
n5=int(input("Enter the no\n"))
n6=int(input("Enter the no\n"))
n7=int(input("Enter the no\n"))
n8=int(input("Enter the no\n"))
s={n1,n2,n3,n4,n5,n6,n7,n8}
print(s)'''

'''#3
s={18,"18"}
print(s)'''

'''#4 what will be the value length of following set=2
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))'''

'''#5
s={} #what is the type of s 
print(type(s)) #its type is dictionary'''

'''#6 create an mpty dict allow 4 fiends to enter their favourite language as values and use keys as their names assume that the names are unique
favlang={}
a=input("enter fav lang sajeed\n")
b=input("enter fav lang adil\n")
c=input("enter fav lang vinit\n")
d=input("enter fav lang avi\n")
favlang['sajeed']=a
favlang['adil']=b
favlang['vinit']=c
favlang['avi']=d
print(favlang)'''

'''#7 names same
favlang={}
a=input("enter fav lang sajeed\n")
b=input("enter fav lang adil\n")
c=input("enter fav lang vinit\n")
d=input("enter fav lang adil\n")
favlang['sajeed']=a
favlang['adil']=b
favlang['vinit']=c
favlang['adil']=d
print(favlang)'''

'''#8 languages same
favlang={}
a=input("enter fav lang sajeed\n")
b=input("enter fav lang adil\n")
c=input("enter fav lang vinit\n")
d=input("enter fav lang avi\n")
favlang['sajeed']=a
favlang['adil']=b
favlang['vinit']=c
favlang['avi']=d
print(favlang)'''

#9 can you chnage values inside a list which is considered in set s s={8,7,12,"harry",[1,2]}
#ans Is no becoz a list cant be added in a set

