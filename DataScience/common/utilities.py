from itertools import product
from collections import defaultdict

def get_matching_events(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space 
                if event_condition(outcome)])

def compute_probability(event_condition, generic_sample_space):
    matching_events = get_matching_events(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        event_size = len(matching_events)
        sample_space_size = len(generic_sample_space)
        return event_size/sample_space_size
    else:
        event_size = sum(generic_sample_space[outcome] for outcome in matching_events)
        sample_space_size = sum(generic_sample_space.values())
        return event_size/sample_space_size

def is_in_interval(number, min, max):
    return min <= number <= max

def generate_head_count_sample_space(number_of_flips = 10):
    weighted_sample_space = defaultdict(int)
    for outcome in product(['Heads','Tails'], repeat = number_of_flips):
        head_count = len([value for value in outcome if value == 'Heads'])
        weighted_sample_space[head_count] += 1

    return weighted_sample_space

