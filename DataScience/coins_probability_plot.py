from common import utilities
from matplotlib import pyplot as plt


head_count_sample_space_10_flips = utilities.generate_head_count_sample_space(10)
x_10_flips = list(head_count_sample_space_10_flips.keys())
x_10_freqencies = [head_count/10 for head_count in x_10_flips]
sample_space_size_10_flips = sum(head_count_sample_space_10_flips.values())
probabilities_10_flips = [value/sample_space_size_10_flips for value in head_count_sample_space_10_flips.values()]
relative_likelihood_10 = [10*prob for prob in probabilities_10_flips]
assert sum(probabilities_10_flips) == 1
where_10 = [not utilities.is_in_interval(value,3,7) for value in x_10_flips]
plt.plot(x_10_freqencies, relative_likelihood_10, linestyle='dotted', label='10 coin flips')
plt.fill_between(x_10_freqencies,relative_likelihood_10,where=where_10)

head_count_sample_space_20_flips = utilities.generate_head_count_sample_space(20)
x_20_flips = list(head_count_sample_space_20_flips.keys())
x_20_freqencies = [head_count/20 for head_count in x_20_flips]
sample_space_size_20_flips = sum(head_count_sample_space_20_flips.values())
probabilities_20_flips = [value/sample_space_size_20_flips for value in head_count_sample_space_20_flips.values()]
relative_likelihood_20 = [20*prob for prob in probabilities_20_flips]
assert sum(probabilities_20_flips) == 1
where_20 = [not utilities.is_in_interval(value,5,15) for value in x_20_flips]
plt.plot(x_20_freqencies, relative_likelihood_20, linestyle='dashed', label='20 coin flips')
plt.fill_between(x_20_freqencies,relative_likelihood_20,where=where_20)


plt.xlabel("Frequency of heads")
plt.ylabel("Relative likelihood")
plt.legend()

plt.show()