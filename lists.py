#Lists ordered, mutable, allow duplicate elements
mylist = ["banana", "cherry", "apple"]

print(mylist)

#create a new list with the list key word
mylist2 = list()
print(mylist2)

#list can contain any items
print(mylist[-2]) #start teh list from behine

#check if item in list

if "banana" in mylist:
    print("yes")


#Append to the list

mylist.append("lemon")
print(mylist)

#insert item at specific point
mylist.insert(1, "Juice")

print(mylist)

#remove item from list using pop

item  = mylist.pop()
print(item)
print(mylist)

#remove specific item

item = mylist.remove("banana")
print(mylist)

#revese list

reversedList = mylist.reverse()
print(mylist)

#sort list, changes the original ist
sortedl = mylist.sort()
print(sortedl)

newlist1 = [4,3,7,-5,-6,-3]
print(newlist1)
new_sorted = sorted(newlist1)

print(new_sorted)

#create a new list with mulitple items

x_list = [0]* 5

print(x_list)

#contact list with plus sign
u_list = x_list + mylist
print(u_list)

#can you substract?
#print(u_list - mylist)

#slicing

xlist = [1,2,3,4,5,6,7,8,9,10]
#reverse
print(xlist[:: -1])
print(xlist[:1])
print(xlist[1:5])
print(xlist[0:5])
print(xlist[::2]) #take every 2 items


#copying list

list_org = [0,9,93,35,45,46]

list_cpy = list_org.copy()
print(list_cpy)
list_org.append("new1")
print(list_org)
list_cpy = list(list_org)
print(list_cpy)
list_org.append("new2")
print(list_org)
list_cpy = list_org[:]
print(list_cpy)
list_org.append("new3")
print(list_org)
print(list_cpy)


#list compheresion

b = [1,3,4,5,6,7,7]
c = [i*i for i in b]
print(c)