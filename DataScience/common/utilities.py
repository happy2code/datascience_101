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
