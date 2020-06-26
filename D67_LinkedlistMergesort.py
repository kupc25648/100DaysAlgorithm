'''
I was pretty sure I wouldn’t implement mergesort in the series. Quicksort was at least interesting since its implementation is tricky. Is there anything interesting about merging? Sure there is — computational models.
Regular mergesort on a fixed array has O(n.log n) time complexity and O(n) space complexity. What is the difference if we use linked-list instead?
I have implemented both, recursive and iterative versions of the algorithm.
Recursive version splits the list into two equally long partitions using fast/slow pointer trick from day 62. Each sublist is sorted and result is merged.
Time complexity is obviously O(n.log n) and space complexity is O(log n). Why not O(1)? Space complexity measured on heap would be O(1), but we have to take into account that recursive call has its cost and space used on stack is still O(log n).
Iterative version takes “sorted” lists of length one and repeatedly merges lists of the same length until a single complete list remains.
Time complexity is again O(n.log n) and this time we can clearly see that space complexity is O(log n).
What is surprising, the linked-list version of algorithm seems to require less memory than fixed array version. Is that true?
Not really. First thing to notice is that linked-list itself requires more space than fixed-array, hence the list has a larger information capacity.
Mergesort is able to use this capacity to avoid further allocations. It’s a similar case to stack vs. heap allocations discussed above. The requirement is still there, just hidden.
To be precise, linked-list mergesort requires extra O(log n) allocated space, but still requires extra O(n) space to keep the order.
'''
from types import SimpleNamespace
from random import randint

# Algorithm
def _merge(p,q):
    r,s = [Node()]*2

    while p or q:
        if not q or p and p.value < q.value:
            r.next = p
            r,p = r.next, p.next
        else:
            r.next = q
            r,q = r.next, q.next

    return s.next

def mergesort_recursive(head):
    # list is sorted
    if not (head and head.next):
        return head

    # make equal split
    p,q,r = head, head.next, None
    while q:
        p,q,r = p.next, q.next and q.next.next, p
    r.next = None

    # sort recursively
    p = mergesort_recursive(p)
    q = mergesort_recursive(head)

    # merge
    return _merge(p,q)

def mergesort_iterative(head):
    splits = []

    while head:
        #sorted list of length 1
        head, p = head.next, head
        p.next = None
        splits.append((1,p))

        while len(splits) > 1:
            (i,p), (j,q) = splits[-2:]
            if i != j and head:
                break

            #merge
            splits[-2:] = [(i+j, _merge(p,q))]

    return splits and splits[0][1] or None

# Utilities
Node = SimpleNamespace

def random_linked_list(size, r):
    head = None
    for i in range(size):
        head = Node(value = randint(0,r), next = head)
    return head

def print_list(head):
    def _iter(head):
        while head:
            yield head.value
            head = head.next

    print(list(_iter(head)))

# Run
head = random_linked_list(size=20, r=10)
print_list(head)
head = mergesort_recursive(head)
print_list(head)

head = random_linked_list(size=20, r=10)
print_list(head)
head = mergesort_iterative(head)
print_list(head)

