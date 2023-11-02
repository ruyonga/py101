#Tuple: ordered, immutable, allows duplicate elements

mytupple = ("max", 29, "Tokyo")
print(mytupple)

#print tupe
print(type(mytupple))

#one item tupple require a last comma

#create a tupple using the key word
x = tuple(["Roxan", 28, "India"])
print(x)

item = mytupple[2]
print(item)

for x  in mytupple:
    print(x)


if "max" in mytupple:
    print("yes")
else:
    print("no")

print(len(mytupple))
#print(mytupple.index('max'))

#slice work as in the list

name, age, city = mytupple

print(name)


xx = (0,1,2,3,4,5)

i1, *i2, i3 = xx

print(i2)  #combines mulitple items


#tupples consume less memory compared to lists
#tupples are more efficient