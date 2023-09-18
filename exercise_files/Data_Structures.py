
# Lists
my_list = [1,2,3,4,5]

print(my_list)

my_list = ["list", "of", "strings"]

my_list = ["list", False, []]

my_list = [[1,2,3,4,5], [False, True], []]

len(my_list) # length of list

# Sets
my_set = {1,2,3,4,5,6}

print(my_set)

type(my_set) # type

len(my_set) # length of set

my_set = {55,5,0,6,8,88,8,899}

print(my_set)
len(my_set) # length of set

[1,3] == [1,3]
[1,3] == [1,5]

# sets
{1,3} == {1,3,3,3}


# Tuples
# tuples that you are never going to be able to add to them, so it uses only exactly the amount of memory it needs
my_tuples = (1,2,3)
len(my_tuples)

(2,3) == (2,1)
(2,3) == (2,3)


my_list.append(5)
print(my_list)

# Dictionary

my_Dictionary = {
    'apple' : "a red fruit",
    'bear' : "a scary animal"
}

my_Dictionary["apple"]

my_Dictionary = {
    'apple' : "a red fruit",
    'bear' : "a scary animal",
    'apple' : "Sometimes red fruit",
}

my_Dictionary["apple"]