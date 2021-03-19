
from common import utilities

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