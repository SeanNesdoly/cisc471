# Given an unsorted list of n-1 distint integers in the range (1,n), find the
# missing integer in linear time. This problem is in theta(n) for both time
# and space complexity. 
#
# Solution 1:
#	fill array with numbers from the set;  
#	iterate through and find the missing integer.
#
# Solution 2:	
#	sum(1...n) - sum(elements of set S) = missing number
#
# CISC471 Homework 1
# Sean Nesdoly
# 2017-09-14

import random

# upper bound on range for integers in set S
n = 20 

# create set S of n-1 distinct integers
S = [i for i in xrange(1, n+1)]
random.shuffle(S)
S.pop(random.randint(0, n-1))
print S

# ==================================================  
# Solution 1
# ==================================================  
# fill each array element with the matching value in S
arr = [0] * n
for i in range(len(S)):
	arr[S[i]-1] = 1

# search for the missing value
missing_val1 = -1
for i in range(n):
	if (arr[i] == 0):
		missing_val1 = i+1

print "Missing value from solution 1:", missing_val1

# ==================================================  
# Solution 2
# ==================================================  
missing_val2 = (n*(n+1)/2) - sum(S)
print "Missing value from solution 2: ", missing_val2
