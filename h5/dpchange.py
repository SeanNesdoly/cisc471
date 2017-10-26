# DPCHANGE
# 
# Convert some amount of money M into given denominations, using the smallest
# possible number of coins. This script solves this problem using a dynamic
# programming approach.
#
# input:    an mount of money, M, and an array of d denominations
#           c=(c1,c2,..,cd), in decreasing order of value (c1>c2>..>cd)
#
# output:   a list of d integers i1,i2,...,id such that c1i1+c2i2+...+cdid = M,
#           and i1+i2+...+id is as small as possible
#
# CISC471
# Sean Nesdoly
# 2017-10-25

import sys

def dpchange(M, c, d):
    best_num_coins = [0]*M

    # solve problem for each target value m to obtain the final solution
    for m in range(M):
        best_num_coins[m] = sys.maxint
        for i in range(d):
            if m+1 >= c[i]:
                if best_num_coins[m-c[i]] + 1 < best_num_coins[m]:
                    best_num_coins[m] = best_num_coins[m-c[i]] + 1


    # retrace steps to determine the coins used in the solution 
    n = best_num_coins[M-1]
    curr_index = M-1
    soln = []

    for i in range(n):
        for j in range(d):

            # offset from current index by coin denomination
            next_index = curr_index - c[j] 

            if next_index >= 0:

                if best_num_coins[next_index] == n - (i+1):
                    soln.append(c[j]) # add denomination to solution
                    curr_index = next_index # update current position
                    break

            elif next_index == -1:
                soln.append(c[j]) # all denominations have been found

    return best_num_coins[M-1], soln



# sample run
M = 40
c = [25,20,10,5,1]
d = len(c)

print dpchange(M,c,d) # (2, [20, 20])
