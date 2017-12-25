"""
	outputs (antiNucleus, mean_prodTime) pairs into 'means.txt' file
	values separeted by tabs
"""

import sys

current_key = ''
values = [0.0, 0.0]

for line in sys.stdin:
	tokens = line.split('\t')
	prodTime = float(tokens[1])

	if current_key == '':
		current_key = tokens[0]

	if current_key != tokens[0]:
		print('{0}\t{1}' .format(current_key, values[0] / values[1]))

		current_key = tokens[0]
		values = [0.0, 0.0]

	values[0] += prodTime
	values[1] += 1.0

# and the last one
print('{0}\t{1}' .format(current_key, values[0] / values[1]))




