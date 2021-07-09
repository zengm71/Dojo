def countdown(n):
    return(list(range(n, -1, -1)))
countdown(5)

def print_and_return(l):
    print(l[0])
    return(l[1])
print_and_return([1,2])

def first_plus_length(l):
    return(l[0] + len(l))
first_plus_length([1,2,3,4,5])

def values_greater_than_second(l):
    if (len(l) < 2):
        return (False)
    l_return = [x for x in l if x > l[1]]
    print(len(l_return))
    return(l_return)
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

def length_and_value(a, b):
    return([b] * a)
length_and_value(4,7)
length_and_value(6,2)