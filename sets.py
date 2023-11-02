#sets unordered, mutable, no duplicates

myset = {1,2,3,5,6,7}
print(myset)

#create set from string
s = set("Hello")
print(s)
#find how many unique characters/elements are in a word, conver it to a set

#empty set is created using set func
my_set = set()


print(type(my_set)) #<class 'set'>

myset.add("op")
myset.remove(2)

#union and intersections

odds = {1,3,5,7,9, 11}
evens = {0, 2, 4, 6, 8, 10}
primes = {2, 3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

diff = odds.difference(primes)
print(diff)

c = frozenset([2,4,67,7,5])
#cannot be changed