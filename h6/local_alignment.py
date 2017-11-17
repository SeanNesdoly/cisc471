# Local Sequence Alignment Problem
#
# input:  strings v and w and a scoring matrix "delta"
#
# output: substrings of v and w whose global alignment, as defined by the
#         "delta" matrix, is maximal among all global alignments of all
#         substrings of v and w
#
# CISC471
# Sean Nesdoly
# 2017-11-16

import numpy as np

# input strings
v = "tacgggtat"
w = "ggacgtacg"
# local alignment: v_soln=tacg, w_soln=tacg; score=4

# scoring parameters as defined by the "delta" matrix
# TODO: implement a real delta matrix (acgt- rows, acgt- columns)
indel     = -1
mismatch  = -1
match     = +1

# initialize scoring matrix S
S = np.zeros( (len(v)+1, len(w)+1) )

# fill scoring matrix S
for i in range(1, len(v)+1):
    for j in range(1, len(w)+1):

        # recurrence relation for global sequence alignment
        S[i,j] = max(
                S[i-1,j-1] + match if v[i-1]==w[j-1] else S[i-1,j-1] + mismatch,
                S[i,j-1] + indel,
                S[i-1,j] + indel,
                0) # allows for an early "escape" from the matrix


# ==============================================================================


# backtrack through S matrix to find solution
v_soln = [ ] 
w_soln = [ ] 

# begin traceback at index of largest value in S;
# if there is more than 1 occurrence, use the first
i,j = np.unravel_index(np.argmax(S), S.shape)
score = S[i,j]

while i > 0 or j > 0:

    # grab diagonal, left, and up entries 
    d = S[i-1,j-1]
    l = S[i,j-1]
    u = S[i-1,j]
    
    if S[i,j] == 0:

        break # escape from matrix

    elif i == 0 and j != 0:

        # termination case 1: exhaust all remaining characters of w
        while j != 0:
            v_soln.insert(0, "-")
            w_soln.insert(0, w[j-1])
            j -= 1

    elif i != 0 and j == 0:

        # termination case 2: exhaust all remaining characters of v
        while i != 0:
            v_soln.insert(0, v[i-1])
            w_soln.insert(0, "-")
            i -= 1

    elif S[i,j] == (d + match) and v[i-1]==w[j-1]:
        
        # match
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, w[j-1])
        i -= 1
        j -= 1
    
    elif S[i,j] == (d + mismatch) and v[i-1]!=w[j-1]:

        # mismatch
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, w[j-1])
        i -= 1
        j -= 1

    elif S[i,j] == l + indel:
        
        # indel for v, use character from w
        v_soln.insert(0, "-")
        w_soln.insert(0, w[j-1])
        j -= 1

    elif S[i,j] == u + indel:

        # use character from v, indel for w
        v_soln.insert(0, v[i-1])
        w_soln.insert(0, "-")
        i -= 1 


# print a solution to the local sequence alignment of strings v and w
print 'v alignment: ', ''.join(str(i) for i in v_soln)
print 'w alignment: ', ''.join(str(j) for j in w_soln)
print 'local alignment score: ', score
print '\nscoring matrix S:\n', S
