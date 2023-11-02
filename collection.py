#Collection countr, namedtuple, ordereddict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import  deque

a = "aaaaaaabbbbvvvv"
#Returns the key value pair matchine the number of times the item exist
#used to find how many times each item exist
my_counter = Counter(a)
print(my_counter)

print(my_counter.most_common(1)[0][0])  #returns the most common element in the string
print(list(my_counter.elements())) #convert a string to its respective elements


Point = namedtuple("Point", "x,y")
pt = Point(1, -5)

print(pt)
print(pt.x, pt.y)


d = deque()

d.append(2)
d.append(3)

d.appendleft(5)
d.extend([9])
d.extendleft([0,2,3,4])

print(d)