#Dictionary: Key_value pairs, unordered, mutable

mydict = {"name": "Daniel", "age": 23, "city": "Tokyo" }
print(mydict)

mydict2 =  dict(name="Aadhya", age=21, city="SI")

value = mydict["age"]
print(value)

mydict["email"] = "dan@test.com"
print(mydict)

#values can be overwritten in my dictionary

#delete

del mydict["age"]
print(mydict)


if "name" in mydict:
    print("name exisit")

try:
    print(mydict2["name"])
except:
    print("oops")

#get keys

for key in mydict.keys():
    print(key)

#get values

for value in mydict.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

#copy a dictionary
dict_copy = dict(mydict)
print(dict_copy)
#assigment leads to variable to point to the same memory location
dict_copy.update(f="hone")
print(dict_copy)