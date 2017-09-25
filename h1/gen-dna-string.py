# Generate all possible DNA strings of length k
#
# input:	integer k denoting the length of DNA strings to generate
# output:	a list of tuples of all possible DNA strings of length k 
#	
# CISC471
# Sean Nesdoly
# 2017-09-19

import itertools

def gen_dna_string(k):
	alphabet = ['A','C','G','T']
	allKmers = [i for i in itertools.product(alphabet, repeat=k)]
	return allKmers
