'''
String searching is a feature built-in to every text editor. Today’s editors use regular expressions due to all the advantages. They are easy to construct, powerful enough and [mostly] have linear time to search.

There are other very interesting methods that are capable of search in sublinear time! Most profound would probably be Boyer-Moore and Knuth-Morris-Pratt.

https://en.wikipedia.org/wiki/Boyer–Moore_string-search_algorithm
https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm

My implementation applies just a simplified idea. Given the first character behind current search window, shift the window to skip all the following mismatches based on occurrence of the character in pattern.
While simple, it will work well in practice. To get the idea, here’s the best case of what could happen.
'''

def search(text,pattern):
    i,k = 0, len(pattern)
    table = {c: k-i for i, c in enumerate(pattern)}

    while True:
        print(f'search @ {i}')
        if text[i:i+k] == pattern:
            print(f'FOUND @ {i}')
        if i+k < len(text):
            i += table.get(text[i+k], k+1)
        else:
            break

text = 'A parabolic (or paraboloid or paraboloidal) reflector (or dish or mirror)'
search(text, 'parabolic')
