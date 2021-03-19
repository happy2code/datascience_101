from common import utilities
from itertools import product

# Problem 1: Analyzing a Family with 4 Children. 
# Suppose a family has 4 children. What is the probability 
# that exactly 2 of the children are boys? 
# We’ll assume that each child is equally likely to be either a boy or a girl.

possible_children = {'Boy','Girl'}
all_combinations = set(product(possible_children, repeat=4))
print(all_combinations)