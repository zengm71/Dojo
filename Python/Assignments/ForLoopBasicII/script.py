def biggie_size(l):
    return([x if x <=0 else 'big' for x in l ])
biggie_size([-1, 3, 5, -5])

def count_positives(l):
    l[-1] = len([x for x in l if x > 0])
    return(l)
count_positives([-1,1,1,1]) 
count_positives([1,6,-4,-2,-7,-2])

def sum_total(l):
    return(sum(l))
sum_total([1,2,3,4])
sum_total([6,3,-2])

def average(l):
    return(sum(l)/len(l))
average([1,2,3,4]) 

def length(l):
    return(len(l))
length([37,2,1,-9])
length([])

def minimum(l):
    if len(l) == 0:
        return False
    else:
        return(min(l))
minimum([37,2,1,-9])

def maximum(l):
    if len(l) == 0:
        return False
    else:
        return(max(l))
maximum([37,2,1,-9])

def ultimate_analysis(l):
    return({
        'sumTotal': sum_total(l), 
        'average': average(l),
        'minimum': minimum(l),
        'maximum': maximum(l),
        'length': length(l)
    })
ultimate_analysis([37,2,1,-9])

def reverse_list(l):
    return([l[x] for x in range(len(l)-1, -1, -1)])
reverse_list([37,2,1,-9])