# Global Sequence Alignment (with a twist)
# Problem 6.21
#
# Here we compile a matrix M whose entries are derived from the S matrix
# computed when solving the Global Sequence Alignment problem. The (i,j)th
# entry in the M matrix is the score from S[i,j], with the extra condition that
# the source of the score must come from matching v[i] with w[j], even if this
# is a suboptimal global alignment for v[0..i] and w[0..j].
#
# input:  strings v and w
#
# output: the dynamic programming table M whose (i,j)th entry is the score of
#         the optimal global alignment which aligns the character v[i] with the
#         character w[j]
#
# CISC471
# Sean Nesdoly
# 2017-11-13

import numpy as np

# input strings
v = "tacgggtat"
w = "ggacgtacg"

# scoring parameters "from" delta matrix
indel     = -1
mismatch  = -1
match     = +1

# initialize scoring matrix S
S = np.zeros( (len(v)+1, len(w)+1) )
S[:,0] = range(0, -1*len(v)-1, indel)
S[0,:] = range(0, -1*len(w)-1, indel)

# fill the scoring matrix S 
for i in range(1, len(v)+1):
    for j in range(1, len(w)+1):

        # recurrence relation for global sequence alignment
        S[i,j] = max(
                S[i-1,j-1] + match if v[i-1]==w[j-1] else S[i-1,j-1] + mismatch,
                S[i,j-1] + indel,
                S[i-1,j] + indel)



# create matrix M using the S matrix as a "guide"
M = np.zeros( S.shape )
for i in range(1, len(v)+1):
    for j in range(1, len(w)+1):
     
        # for the optimal global alignment score of v[0..i] with w[0..j] with
        # v[i] and w[j] aligned, apply a match or mismatch score to S[i-1,j-1],
        # thus prohibiting indels at these positions
        if v[i-1] == w[j-1]:
            M[i,j] = S[i-1,j-1] + match
        else:
            M[i,j] = S[i-1,j-1] + mismatch

print M
