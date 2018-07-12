def methodception(another):
    return another()

def add_numbers():
    return 35 + 77

#print(methodception(add_numbers))

#print(methodception(lambda: 35 + 77))
# lambda functions are anonymous standalone functions, using only 1 line

##


my_list = [13, 56, 77, 484]

print(list(filter(lambda x: x != 13, my_list)))
# filter takes a function, then an iterable(my_list). 
# Needs to be preceeded by list if you want it to return a list

def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))
# this function is equivalent to the lambda function above

print([x for x in my_list if x != 13])
# this list comprehension is another way, unique to python
# but this is python specific, filter is more general across code langs


##
(lambda x: x * 3)(5)
#above and below are equivalent functions
def f(x):
    return x * 3

f(5)