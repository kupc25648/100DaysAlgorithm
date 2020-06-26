'''
Given a totally ordered set, find the next permutation of the current configuration:

FADE -> FAED -> FDAE -> FDEA -> ...

Even though almost every library offers a similar function, this tool can quickly become very useful in various competitions when you need to speed your algorithm up.

The algorithm itself is simple. Beginning from end, find the longest decreasing sequence 42531 and denote the preceding item as pivot 42531. Swap pivot with the smallest higher item 43521 in the sequence and revert the sequence 43125.

# The reversed() method takes a single parameter: return reverse of the element in the parameter as a reverseobject, can be turned to a list by list(reversed(parameter))
'''


def permute(a_list):
    n = len(a_list)

    #   i: position of pivot
    for i in reversed(range(n-1)):
        if a_list[i] < a_list[i+1]:
            break
    else:
        #   very last permutartion
        a_list[:] = reversed(a_list[:])
        return a_list

    #   j: position of the next candidate
    for j in reversed(range(i,n)):
        if a_list[i] < a_list[j]:
            #   swap pivot and reverse the tail
            a_list[i], a_list[j] = a_list[j], a_list[i]
            a_list[i+1:] = reversed(a_list[i+1:])
            break

    return a_list

my_List = ['A','B','C','D']

for i in range(23):
    print(permute(my_List))





