

grades_list = [ 77, 80, 90, 95, 100]
#mutable/appendable

grades_list.append(110)

print(sum(grades_list) / len(grades_list))

print(grades_list[0])

grades_list[0] = 60

print(grades_list)



## tuple operations ##

grades_tuple = (77, 80, 90, 95, 100)
#immutable

grades_tuple = grades_tuple + (100,)

print(grades_tuple)



## set operations ##

grades_set = {77, 80, 90, 100, 100}
grades_set.add(60)
print(grades_set)
# unordered, unique items only duplicates are kicked out
# because they are unordered you can't assign grades_set[0] = 60

my_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(my_numbers.intersection(winning_numbers))
# produces a new set of the matching numbers between 2 sets

print(my_numbers.union(winning_numbers))
# produces new set of merged unique numbers, removing dupes

print({1, 2, 3, 4}.difference({1, 2}))
# produces a set of the numbers that are not in both sets, in this case 3 and 4