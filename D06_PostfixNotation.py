'''
Reverse Polish notation (RPN), also known as Polish postfix notation or simply postfix notation, is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands.

While humans mostly use infix notation of algebraic expressions, Reverse Polish notation or postfix notation is much easier to parse algorithmically.
For example, these expressions are equivalent, the first one is in infix form and the second one is in postfix form.
2 * (1 + 3) = 2 1 3 + *
When you are implementing your very first expression parser, postfix and prefix notations are the best way to go. Onto stack: Push, push, pop, push, push, pop. Pop.

ps
The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.
__add__ (self, other)
__sub__ (self, other)
__mul__ (self, other)
__div__ (self, other)

ps2
The pop() method removes the item at the given index from the list. The method also returns the removed item.

ps3
Split a string into a list where each word is a list item:
You can specify the separator, default separator is any 'whitespace' or an indicated separator .split("indicator").



'''
ops = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '^': float.__pow__,
}

# expression as string of RPN
# return calculated result

def postfix(expression):
    stack =[]
    for x in expression.split():
        if x in ops:
            x = ops[x](stack.pop(-2), stack.pop(-1))
        else:
            x = float(x)
        stack.append(x)

    return stack.pop()

print(postfix('1 2 + 4 3 - + 10 5 / *'))






