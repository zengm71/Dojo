def selectionSort(l):
    for j in range(len(l) - 1):
        min = l[j]
        min_index = j
        for i in range(j, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[j], l[min_index] = l[min_index], l[j]      
    return(l)
selectionSort([1,5,9,4,5,3,6])