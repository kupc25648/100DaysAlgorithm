'''
My today’s algorithm is binary search on sorted array. This one is fascinating, since it is probably one of the easiest algorithms to understand, yet one of the most difficult to implement correctly.
According to Sedgewick, it was invented in mid-50s, but it was not until mid-60s for the first correct implementation to appear. In 2006 binary search routine in Java libraries had to be fixed due to bug in its implementation.
Why is that? You have to be very careful when playing with indices. The key to success is to keep (left, right) boundaries within the searched range rather than outside.


'''
def binaerySearch(listofitems, itemtosearch):
    left, right = 0 , len(listofitems) - 1

    while left <= right:
        middle = (left+right) // 2

        if itemtosearch < listofitems[middle]:
            right = middle - 1
        elif itemtosearch > listofitems[middle]:
            left = middle + 1
        else:
            return middle

    # if itemtosearch is not int the listofitems
    return -1

print(binaerySearch([2,3,4,8,10],8))





