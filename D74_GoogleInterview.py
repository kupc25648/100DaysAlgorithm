'''
There are several articles on the web that discuss the following question which supposedly originates at Google interview.
If the probability of seeing a car on the highway in 30 minutes is 0.95, what is the probability of seeing a car on the highway in 10 minutes? (assume a constant default probability)
That’s a question to test my skill in probability — what if math is not my friend, but programming is?
The probability of 10-minute interval must be in range between 0 and 1, I know at least as much. And I can simulate Bernoulli event with probability p¹⁰ using uniform random generator: success = rand() < p¹⁰.
Next, I can track a road during three independent 10-minute intervals with given probability p¹⁰ to check if I see a car. If I track many roads at once, I can estimate probability p³⁰ of 30-minute interval based on 10-minute intervals with fixed value p¹⁰.
So, I can find p³⁰ for a given value of p¹⁰, but how do I find p¹⁰ for desired value of p³⁰=.95? The answer is bisection method. It is a kind of binary search on continuous data.
Start the search at interval [0, 1] and set p¹⁰ = .5
If p³⁰ > .95, search on [0, .5]
If p³⁰ < .95, search on [.5, 1]
In just a moment we can find out the probability for 30-minute interval is about 63%. And who says we need math to solve complex tasks?!
'''
import numpy as np

# Algorithm
def solve_question(trials):
    # range to search in
    probability_range = np.array([0.,1.])

    while True:
        # prob. to see car in 10 miniutes
        probability_10min = probability_range.mean()

        # simulate three 10_minute interval
        events = np.random.rand(trials,3) < probability_10min
        events = np.sum(events, axis=1) > 0

        # prob. to see car in 30 minutes
        probability_30min = np.mean(events)
        if abs(probability_30min - 0.95) < 1e-4:
            return probability_10min

        # bisection
        i = 0if probability_30min < 0.95 else 1
        probability_range[i] = probability_10min

# Run
print(solve_question(10**5))
