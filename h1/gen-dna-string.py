# Generate all possible DNA strings of length k
#
# CISC471
# Sean Nesdoly
# 2017-09-19

import itertools

k = 3 # length of DNA string to generate 

alphabet = ['A','C','G','T']
allKmers = [i for i in itertools.product(alphabet, repeat=k)]
