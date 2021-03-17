def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space 
                if event_condition(outcome)])

def compute_probability(event_condition, sample_space):
    events = get_matching_event(event_condition, sample_space)
    return len(events)/len(sample_space)

    
