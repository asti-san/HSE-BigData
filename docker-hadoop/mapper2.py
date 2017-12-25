"""
	For every antiNucleus pick entries with prodTime bigger than mean value

	key: antiNucleus
	value: eventFile, prodTime
"""

import sys

means = {}
with open('means.txt', 'r') as f:
	for line in f:
		antiNucleus, mean = line.split('\t')
		means[antiNucleus] = float(mean)

for line in sys.stdin:
	tokens = line.split(', ')
	antiNucleus, eventFile, prodTime, Pt = tokens[0], tokens[1], tokens[10], tokens[11]

	if prodTime > means[antiNucleus]:
		print('{0},{1},{2}' .format(antiNucleus, eventFile, Pt))
