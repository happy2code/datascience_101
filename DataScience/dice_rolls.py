from common import utilities
from itertools import product

# Suppose we’re shown a fair six-sided die whose faces are 
# numbered from 1 to 6. The die is rolled 6 times. 
# What is the probability that these 6 dice-rolls add up to 21?
possible_rolls = list(range(1,7))
sample_space = set(product(possible_rolls, repeat=6))

def adds_up_to_21(outcome):
    return sum(outcome) == 21

prob = utilities.compute_probability(adds_up_to_21, sample_space)
print(f"Probability of dice summing upto 21 is {prob}")