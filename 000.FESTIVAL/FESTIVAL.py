#!/usr/bin/env python
import sys

def calcMinimalAvg(N, L, D):
    local_sum = 0
    minimal_avg = 100.0
    for width in range(L, N+1):
        minimal_sum = 100*width
        for i in range(0, N-width+1):
            if i == 0 : local_sum = sum(D[i:width])
            else :      local_sum = local_sum - D[i-1] + D[i+width-1]
            if local_sum < minimal_sum : minimal_sum = local_sum
        local_avg = minimal_sum/float(width)
        if local_avg < minimal_avg : minimal_avg = local_avg
    return minimal_avg

def main():
    count = sys.stdin.readline()
    for i in range(0, int(count)):
        N, L = sys.stdin.readline().split()
        D = [int(i) for i in sys.stdin.readline().split()]
        print "%.11f" % calcMinimalAvg(int(N), int(L), D)

if __name__ == "__main__" :
    main()
