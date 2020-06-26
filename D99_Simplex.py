'''
Linear programming is an area of mathematics that deals with the simplest form of constrained optimization problem — linear program. And simplex should definitely be in your toolbox if you are serious about algorithms.
Here is an example of a linear program [in standard form].
maximize: -x + 3y + 2z

subject to:
x + y + z ≤ 6
x     + z ≤ 4
    y + z ≤ 3
x + y     ≤ 2

x, y, z ≥ 0
The goal is to maximize a linear function given a set of linear constraints.
The simplex algorithm is rather straightforward. We convert the system of inequalities into system of equalities and then use Gaussian elimination with clever pivot selections.
If you get lost during my explanation, get back to pen and paper and rewrite the table into system of equations. All we are doing is merely solving linear equations.
Notice that each inequality in linear program above is in form of f(x) ≤ b. We can add some non-negative number to the left side to get f(x) + s = b. Variable s is called a slack variable and it will compensate the difference between f(x) and b so that we can get rid of inequality.
 x +  y + z + r             = 6
 x      + z     + s         = 4
      y + z         + t     = 3
 x +  y                 + u = 2
-x + 3y + 2z                = 0
subject to: x, y, z, r, s, t, u ≥ 0
I have rewritten the original problem by introducing slack variable into each inequality. And I have also appended the function to be maximized and set it equal to 0. Why?
Notice that the equation system has a trivial solution. We can set x=y=z=0 and let slack variables compensate the system. It’s not the best solution, but it’s a good starter.
From now on, we rewrite the system into Excel and use the table, instead.

The table you are looking at is called a simplex tableau.
And I want you to remember this rule. If a column contains all zeros but a single one, the variable is takes on non-zero value. Otherwise is the variable set to zero.
Hence the initial solution is x=y=z=0, r=6, s=4, t=3, u=2. And no, it is not a coincidence. Remember we chose a trivial solution for starter to obey the rule above. And it shows that it is pretty much all that we need to solve the problem.

The last row contains the function to be maximized. We can’t increase x since the function would decrease. But we can increase y since its coefficient is positive.
How much can y be increased? Divide the last column [right sides of equalities] by y-column: 6/1, 4/0, 3/1, 2/1 and take the row where y contains a positive value and result of division is the smallest.
We need to take the smallest value so that we do not violate conditions in other rows — we are still solving an equation system, think about it!
Then do Gaussian elimination.

Notice how the system changed. Still remember the rule? New values of variables are now x=z=u=0, y=2, r=4, s=4, t=1 and function value is 6.
There is still another variable that can be increased. It’s z due to its positive coefficient in the last row. Find the correct row and eliminate.

At this moment, the last row contains no positive value, which means we are done. What is the final solution?

Set x=0, y=2, z=1 and the function value is -x + 3y + 2z = 8.
I would definitely recommend you to solve this problem on the paper. Here are some points you can think about in terms of equation system that will help you to understand the simplex algorithm.
when we did elimination using column y, the last row [containing the function] ended up with zero coefficient — what’s the consequence?
we started the table with 4 pivotal columns [those that contain all zeroes but a single one], we ended up with another 4 pivotal columns — why?
setting non-pivotal variables to zero is compensated by pivotal variables; as a consequence the function value increases — why?
the red cell in the tableau always contains a current value of -f(x) — why?
That’s all about simplex. Is it really so simple?
In general, solving a linear program is pretty difficult and theoretical bounds put simplex into exponential algorithms.
There are also further problems: Solution can be unbounded, system may degenerate, simplex may cycle forever, etc. My implementation doesn’t care as long as it is able to return at least one solution.
In practice, however, it is easy. Simplex can be [and usually is] implemented specifically for a given problem and real problems tend to be solved quickly and efficiently.
And if you got interested by linear programming, go ahead and read more about the topic. Keep in mind that you are just working with equations and you won’t get surprised by in-depth explanations of feasible regions, dual problems and all the theory behind.

https://medium.com/100-days-of-algorithms/day-99-simplex-1588dd2ebb05
'''
import numpy as np

# Algorithm
def simplex(c, A, b):
    table = initialize(c,A,b)
    while not search_optimum(table):
        pass

    return solution(c, table)

def initialize(c, A,b):
    (m,n), k = A.shape, len(c)

    # simplex table
    # |A|E|b|
    # |c|0|0|

    table = np.zeros((m+1, m+n+1))
    table[:m,:n] = A
    table[range(m), range(n,n+m)] = 1
    table[:-1,-1] = b
    table[-1, :k] =c

    return table

def search_optimum(table):
    index = np.argwhere(table[-1,:-1] >0).ravel()

    # optimum found
    if not len(index):
        return True

    # pivotal column
    j = index[0]
    column = table[:-1,j].copy()
    column[column <= 0] = -1

    if np.all(column <=0 ):
        raise ArithmeticError('the system is unbounded')

    # pivotal row
    pivots = table[:-1, -1]/ column
    pivots[column <= 0] = np.inf
    i = np.argmin(pivots).ravel()[0]

    # eliminate by pivot at (i,j)
    row = table[i]/ table[i][j]
    table[:] -= np.outer(table[:,j],row)
    table[i,:] = row
    table[:,j] = table[:,j].round()

def solution(c, table):
    (m,n), k = table.shape, len(c)

    # pivotal column
    s = np.sum(table == 0, axis =0) ==m-1
    t = np.sum(table ==1, axis = 0) == 1

    # solution
    x = np.zeros(n-1)

    for j in range(n-1):
        if s[j] and t[j]:
            x[j] = table[:,j] @ table[:,-1]

    return dict(
        x = x[:k],
        slack = x[k:],
        max = table[-1,-1],
        table = table )


# Linear program 1
'''
maximize: -x + 3y + 2z

subject to:
x + y + z <= 6
x     + z <= 4
    y + z <= 3
x + y     <= 2

x, y, z >= 0

'''
c = np.array([-1, 3, 2])
A = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0],
])
b = np.array([6, 4, 3, 2])

lp = simplex(c, A, b)

for k in ['x', 'slack', 'table', 'max']:
    print(k, '\n', lp[k], '\n')

# Linear program 2
'''
maximize: 2r + 4s + 3t + u

subject to:
3r +  s +  t + 4u <= 12
 r - 3s + 2t + 3u <= 7
2r +  s + 3t -  u <= 10

r, s, t, u >= 0

'''
c = np.array([2, 4, 3, 1])
A = np.array([
    [3, 1, 1, 4],
    [1, -3, 2, 3],
    [2, 1, 3, -1]
])
b = np.array([12, 7, 10])

lp = simplex(c, A, b)

for k in ['x', 'slack', 'table', 'max']:
    print(k, '\n', lp[k], '\n')
