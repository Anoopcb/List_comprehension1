## List comprehension

## create a list of squares from 1 to 10 with list comprehension

#normal

squares = []
for i in range(1, 11):

    squares.append(i**2)
print(squares)

# now by list comprehension

squares1 = [i**2 for i in range(1, 11)]
print(squares1)

squares2 = [i**3 for i in range(1, 11)]
print(squares2)

# one more example

## normal way
negative = []
for i in range(1, 11):
    negative.append(-i)
print(negative)

## by list comprehension

negative1 = [-i for i in range(1, 11)]
print(negative1)


#one more example
## normal way

names = ["Anoop", "Shalini", "Pi"]

new_list=[]

for name in names:

    new_list.append(name[0])
print(new_list)


## by list comprehension

new_list2 = [name[0] for name in names]
print(new_list2)

l2 = ["abc", "cde", "adf"]

def reverse_string(l):

    return [name[::-1] for name in l]

print(reverse_string(l2))



#### list comprehension with if statements


numbers = list(range(1, 11))
print(numbers)

numbers1 = [i for i in range(1, 11) if i %2==0]
print(numbers1)


def num_to_string(l):

    return [str(i) for i in l if (type(i)==int or type(i)== float)]
print(num_to_string([1, 2, 2, [1, 2, 3], 4.5, "Pi"]))



##

nums = [1, 2, 3, 5, 4, 7, 8, 9, 8, 2, 6]




new_list5 = [i*2 if (i%2==0) else -i for i in nums]
print(new_list5)

## nested for in list comprehension

nested_comp = [[i for i in range(1, 4)] for j in range(3)]
print(nested_comp)










