# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

t= (10,20,30,40,50,"hello",True,23.2)
t1=tuple((10,20,30))

print(t1)
print(len(t))

# Accessing elements using index
print(t[4])
print(t[1:6])
print(t[::-1])
print(t[-1])

# convert tuple to list
l=list(t)
l.append(600)
t=tuple(l)
print(t)
print(l)

# unpack tuple
k=(10,20,30,40,50)
l=(100,200)
(a,*b,c)=k
print(a)
print(b)
print(c)

# join tuple
a=k+l
print(a*2)