from common import utilities
from matplotlib import pyplot as plt

head_count_sample_space_20_flips = utilities.generate_head_count_sample_space(20)
x = list(head_count_sample_space_20_flips.keys())
y = [head_count_sample_space_20_flips[key] for key in head_count_sample_space_20_flips]
plt.scatter(x,y)
plt.xlabel("Number of heads")
plt.ylabel("Number of times with x heads")
plt.show()