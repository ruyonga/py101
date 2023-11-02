#string: ordered, immutable, text representation

my_string = "am a programmer"
print(my_string)

char = my_string[0]
print(char)

substring  = my_string[1:5]
print(substring)


my_string = "Hello word"
#mystring.strip

print(my_string.upper())
print(my_string.lower())
print(my_string.endswith("word"))
print(my_string.count("l"))
print(my_string.replace("word", "world"))

x_string = "am a programmer"
split_s = x_string.split(" ")
print(split_s)

#join
joined = " ".join(split_s)
print(joined)

a6 = ["a"]* 10
print(a6)

myupated_a6 = ",".join(a6)
print(myupated_a6)


var = "Daniel"

myname = "the variable is %s" % var
print(myname)



var = "Daniel"

myname = "the variable is {}".format(var)
print(myname)



var = "Daniel"

myname =f"the variable is {var}"
print(myname)



