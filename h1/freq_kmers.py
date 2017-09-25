# Frequent Words Problem
#
# Compute the most frequent kmers within a string. A kmer is defined as a
# substring of length k. The implemented algorithm has a worst-case time
# complexity of O(n^2); this will vary depending on the collision resolution
# technique used when filling the hashtable with kmers. The space complexity is
# determined by how large the hashtable is; thus, it is in O(n).
#
# input:	a string and an integer k
# output:	all most frequent kmers in the given string
#
# CISC471
# Sean Nesdoly
# 2017-09-14

# Find the most frequent kmers in a string
def get_most_frequent_kmers(text, k):
	kmers = parse_kmers(text, k)
	print(kmers)
	max_kmer = max(kmers.values())

	for token in kmers:
		if (kmers[token] == max_kmer):
			print(token)

# Create a dictionary of unique kmers where each value denotes the count of
# how often that kmer appears within the given string
def parse_kmers(text, k):
	n = len(text)-k+1 # number of kmers
	kmers = {text[0:k]: 1}

	for i in range(1, n):
		token = text[i:i+k]
		if (token in kmers):
			kmers[token] +=1
		else:
			kmers[token] = 1

	return kmers

# sample run
get_most_frequent_kmers("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
