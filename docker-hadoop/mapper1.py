"""
	key:   antiNucleus
	value: prodTime
"""

import sys

for line in sys.stdin:
	tokens = line.split(', ')
	print("{0}\t{1}" .format(tokens[0], tokens[10]))
