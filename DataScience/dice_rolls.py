from common import utilities
from itertools import product
from collections import defaultdict

# Suppose we’re shown a fair six-sided die whose faces are 
# numbered from 1 to 6. The die is rolled 6 times. 
# What is the probability that these 6 dice-rolls add up to 21?
possible_rolls = list(range(1,7))
sample_space = set(product(possible_rolls, repeat=6))
print(f"Size of sample space(dice rolled 6 times) is : {len(sample_space)}")

def adds_up_to_21(outcome):
    return sum(outcome) == 21

prob1 = utilities.compute_probability(adds_up_to_21, sample_space)
print(f"Probability of dice summing upto 21 is {prob1}")

weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    weighted_sample_space[sum(outcome)] += 1

prob2 = utilities.compute_probability(lambda x : x == 21, weighted_sample_space)
print(f"Probability of dice summing upto 21 is {prob2}")
assert prob1 == prob2


prob3 = utilities.compute_probability(lambda x : utilities.is_in_interval(x,10,21), weighted_sample_space)
print(f"Probability of interval (10,21) is {prob3}")