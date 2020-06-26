'''
Factorial number system is an interesting showcase of a mixed radix. Instead of powers of homogeneous base as we are usually used to, factoradic uses factorials.

For example,
6281 = 6*10³ + 2*10² + 8*10¹ + 10⁰
11412210 = 7! + 6! + 4*5! + 4! + 2*3! + 2*2! + 1! + 0*0!

What’s interesting about representations of a number in different [homogeneous or mixed] radices? If a numeral representation in radix R shows a high entropy, it will keep high entropy in all the representations. This is very powerful idea that brings notion of what information is. The information contained in the number can be transferred [to radix system] or hidden, but cannot vanish.
For joy, I decided to use a one-liner today. Or two one-liners to be exact. Have fun!
https://github.com/coells/100days


'''

# Algorithm
fac = lambda i, *j: i and fac(*divmod(i, len(j)+1), *j) or j or (i,)
dec = lambda i, k=0, *j: j and dec(i*len(j)+i+k,*j) or i
# Run
for i in range(0, 11):
    f = fac(i ** 3)
    d = dec(*f)
    print(d, '<->', ' '.join(map(str, f)))
