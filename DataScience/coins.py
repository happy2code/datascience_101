
from common import utilities
from itertools import product
from collections import defaultdict

def is_heads_or_tails(outcome) :
    return outcome in {'Heads', 'Tails'}

def is_neither(outcome):
    return not is_heads_or_tails(outcome)

def is_heads(outcome):
    return outcome == 'Heads'

def is_tails(outcome):
    return outcome == 'Tails'

sample_space = {'Heads', 'Tails'}
event_conditions = [is_heads_or_tails, is_neither, is_heads, is_tails]

for event_condition in event_conditions:
    prob = utilities.compute_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name}' is '{prob}'")

weighted_sample_space = {'Heads': 4, 'Tails': 1}
for event_condition in event_conditions:
    prob = utilities.compute_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"Weighted Probability of event arising from '{name}' is '{prob}'")

def generate_sample_space(num_flips = 10):
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(['Heads','Tails'], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips
                        if outcome == 'Heads'])
        weighted_sample_space[heads_count] += 1

    return weighted_sample_space

weighted_sample_space = generate_sample_space()
assert weighted_sample_space[10] == 1
assert weighted_sample_space[9] == 10

prob = utilities.compute_probability(lambda x: utilities.is_in_interval(x,8,10), weighted_sample_space)
print(f"Probability of observing more than 7 heads is {prob}")