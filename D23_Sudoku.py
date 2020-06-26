'''
Back on the day, I was fresh undergraduate at my first lecture of Linear algebra. The lecturer came in the class and told us, “This puzzle was a gift from my former student. It’s similar to Rubik’s cube but way more complex and I’m not able to solve it. Whoever of you solves it has granted A in the class.”
My classmate found a sequence of moves that led to permutation of three positions and wrote a program that first found solution in 6000 moves and then in 3000 moves. 3 weeks later he got A for granted.
Do you have a story about puzzle, too? Feel free to share with me.

ps
1.)
numpy.matrix.A1 Return self as a flattened ndarray.
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.matrix.A1.html
2.)
set in python
https://realpython.com/python-sets/
3.) modulus %
Divides and returns the value of the remainder.
4.) Floor Division //
Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
5.) Bitwise OR |
https://www.programiz.com/python-programming/operators

'''
import numpy as np

def sudoku(matrix, n=0):
    if n >=81:
        return matrix
    if matrix.A1[n]:
        return sudoku(matrix, n+1)

    i,j,k,l = n//9, n%9, n//27*3, (n%9)//3*3

    # get variable value
    x = set(range(1,10)) - (
        set(matrix[i].A1) |
        set(matrix.T[j].A1) |
        set(matrix[k:k+3,l:l+3].A1)
        )

    # backtracking
    for value in x:
        matrix[i,j] = value
        if sudoku(matrix, n+1) is not None:
            return matrix
    else:
        matrix[i,j] = 0

print(sudoku(np.matrix("""
    0 0 0 1 0 9 0 7 0;
    0 9 0 0 0 0 8 0 0;
    5 0 3 0 4 0 0 0 0;
    0 0 0 0 0 0 7 9 0;
    0 0 7 2 6 5 3 0 0;
    0 3 8 0 0 0 0 0 0;
    0 0 0 0 9 0 4 0 1;
    0 0 6 0 0 0 0 2 0;
    0 5 0 4 0 2 0 0 3
""")))

