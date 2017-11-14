# Global Sequence Alignment Problem
#
# input:  string v of length n and string w of length m, and a scoring matrix
#         delta
#
# output: an alignment of v and w whose score (as defined by the delta matrix)
#         is maximal among all possible alignments of v and w
#
# CISC471
# Sean Nesdoly
# 2017-11-13

import numpy as np

# input strings
v = "tacgggtat"
w = "ggacgtacg"

# scoring parameters "from" delta matrix
# TODO: implement a real delta matrix (acgt rows, acgt columns)
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
print S



# backtrack to find solution
v_soln = [ ] 
w_soln = [ ] 

i = len(v)
j = len(w)

while i > 0 or j > 0:

    # grab diagonal, left, and up entries 
    d = S[i-1,j-1]
    l = S[i,j-1]
    u = S[i-1,j]

    if i == 0 and j != 0:

        # termination case 1: exhaust all remaining characters of w
        while j != 0:
            v_soln.insert(0, "-")
            w_soln.insert(0, w[j-1])
            j -= 1

    elif i != 0 and j == 0:

        # termination case 2: exhaust all remaining characters of v
        while i != 0:
            print i,j
            v_soln.insert(0, v[i-1])
            w_soln.insert(0, "-")
            i -= 1

    elif S[i,j] == d+1 and v[i-1]==w[j-1]:
        
        # match
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, w[j-1])
        i -= 1
        j -= 1
    
    elif S[i,j] == d-1 and v[i-1]!=w[j-1]:
        
        # mismatch
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, w[j-1])
        i -= 1
        j -= 1

    elif S[i,j] == l-1:
        
        # indel for v, use character from w
        v_soln.insert(0, "-")
        w_soln.insert(0, w[j-1])
        j -= 1

    elif S[i,j] == u-1:

        # use character from v, indel for w
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, "-")
        i -= 1 

# print one solution to the global sequence alignment of strings v and w
print ''.join(str(i) for i in v_soln)
print ''.join(str(j) for j in w_soln)
