#sets is collection of non reppetitive elements.
#we cannot add list and dictionary in a set
#we can add tupple to it
a={1,2,3,4,1}
print(a)
print(type(a)) #it will return {1,2,3,4} it ignores another 1 as it is reppeted
b=set()  # syntax of empty set\


#methos 
b.add(1)
b.add(2)
b.add(3)
b.add(3)
b.add((8,4,6,9,0))
print(b)
c={6,7,0,9,4,3}
print(len(c))
print(len(b))
c.remove(0)
print(c)
print(c.pop())
print(c.clear())

