def insertSort(l):
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            j = i
            while l[j-1] > l[j] and j > 0:
                l[j-1], l[j] = l[j], l[j-1]
                j = j -1 
    return(l)
insertSort([1,5,9,4,5,3,6])

