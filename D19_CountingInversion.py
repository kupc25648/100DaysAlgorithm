'''
Count of inversions in array is a textbook showcase of what is the difference between quadratic and linearithmic algorithm.
While naive method may select each tuple of items to be compared, more efficient approach is to adapt merge-sort to do the counting for you. As a result, function returns number of inversions and the sorted array as bonus.

https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)
In computer science and discrete mathematics, a sequence has an inversion where two of its elements are out of their natural order.

'''
items = []
def inversions(items):
    n = len(items)
    if n <= 1:
        return items, 0

    # number of inversions in partitions
    left, linv = inversions(items[:n//2])
    right, rinv = inversions(items[n//2:])

    inv = linv + rinv
    llen, rlen = len(left), len(right)
    i,j,aux = 0,0,[]

    #merge and count inversions
    for k in range(n):
        if i < llen and j < rlen and left[i] > right[j]:
            inv += llen-i
            aux.append(right[j])
            j+=1
        elif i < llen:
            aux.append(left[i])
            i+=1
        else:
            aux.append(right[j])
            j+=1

    return aux, inv

print(inversions([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))







