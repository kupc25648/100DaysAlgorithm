'''
Matrix multiplication is an associative operation. (AB)C is equal to A(BC) for matrices A, B, C, and it doesn’t matter which order of pair multiplication you choose.
Unfortunately, that’s not true from computational perspective. If dimensions of matrices are A=[10, 20], B=[20, 30], C=[30, 40], numbers of scalar multiplications differ significantly:
(AB)C = 10*20*30 + 10*30*40 = 18000
A(BC) = 20*30*40 + 10*20*40 = 32000
The best ordering can be found using recursive relationship. Let MCM denotes a function that returns a minimum number of scalar multiplications. Then MCM can be defined as the best split among all possible choices.

MCM(A1,...,Ai) = min MCM(A1,..,Ai) x MCM(A1+1,..,Ai)

Using dynamic programming and memoization, the problem can be solved in O(n³) time.
'''


def MCM(chain):
    n = len(chain)

    #   single matrix chain has zero cost
    aux = {(i,i):(0,)+chain[i] for i in range(n)}

    #   i: length of subchain
    for i in range(1,n):
        #   j: starting in dex of subchain
        for j in range(0, n-i):
            best = float('inf')

            #   k: splitting point of subchain
            for k in range(j, j+i):
                #   multiply subchains at splitting point
                lcost, lname, lrow ,lcol = aux[j,k]
                rcost, rname, rrow ,rcol = aux[k+1,j+i]
                cost = lcost+rcost+lrow * lcol*rcol
                var = '(%s%s)' % (lname, rname)

                #   pick the best one
                if cost < best:
                    best = cost
                    aux[j,j+i] = cost, var, lrow,rcol

    return dict(zip(['cost','order','rows','cols'],aux[0,n-1]))

print(MCM([('A', 10, 20), ('B', 20, 30), ('C', 30, 40)]))
