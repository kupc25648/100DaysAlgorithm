'''
I was a fresh undergraduate, it was our very first lecture of programming [in Pascal] and stable marriage problem was the first thing we were taught.
The teacher had his own special style of teaching, changing problem terminology to m**chos and b**ches and we were shocked. Yet, it probably worked, I still remember the lesson even today.
There is a group of men and group of women seeking for a partner. Each man and each woman has own preferences and the goal is to find a stable matching. The matching is called stable if neither one of pair can change partner such that both partners in a new pair would gain in their preferences.
Adam prefers Alice
Bob prefers Alice
Alice prefers Bob
Betty prefers Adam
unstable: Adam-Alice, Bob-Betty
stable: Adam-Betty, Bob-Alice
The algorithm is actually pretty easy.
Pair each man with a woman according to man’s preferences. If a woman has already been in pair, but could gain by another man’s proposal, release the original pair and make a new one.
The difficult part is to prove the correctness. If this problem seems like searching for Nash equilibrium, you’re right. That’s the kind of thing people receive a Nobel prize for.
'''
from collections import deque, defaultdict

# Algorithm
def stable_match(men, women):
    free_men = deque(men)
    engage = defaultdict(lambda: None)

    while free_men:
        i = free_men.popleft()

        # man proposes women according to his preference
        for j in men[i]:
            preference = women[j].index
            fiance = engage[j]

            # women accepts the better offer
            if not fiance or preference(i) < preference(fiance):
                engage[j] = i
                fiance and free_men.append(fiance)
                break

    return [(m,w) for w,m in engage.items()]

# Run
men = {
    'adam': ['diana', 'alice', 'betty', 'claire'],
    'bob': ['betty', 'claire', 'alice', 'diana'],
    'charlie': ['betty', 'diana', 'claire', 'alice'],
    'david': ['claire', 'alice', 'diana', 'betty'],
}
women = {
    'alice': ['david', 'adam', 'charlie', 'bob'],
    'betty': ['adam', 'charlie', 'bob', 'david'],
    'claire': ['adam', 'bob', 'charlie', 'david'],
    'diana': ['david', 'adam', 'charlie', 'bob'],
}

print(stable_match(men, women))
