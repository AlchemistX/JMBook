#!/usr/bin/env python
def genFS(D):
    P = set()
    for i in xrange(0, len(D), 2):
        if D[i] <  D[i+1]: P.add((int(D[i]), int(D[i+1])))
        else:              P.add((int(D[i+1]), int(D[i])))
    return P

def doPicnic(lstTaken, P):
    if False not in lstTaken :
        return 1
    nFirstFree = lstTaken.index(False)
    nRet = 0
    for i in xrange(nFirstFree+1, len(lstTaken)):
        if lstTaken[i] != True and ((nFirstFree, i) in P) == True:
            lstTaken[nFirstFree] = lstTaken[i] = True
            nRet += doPicnic(lstTaken, P)
            lstTaken[nFirstFree] = lstTaken[i] = False
    return nRet

def main():
    nCases = int(raw_input())
    for _ in xrange(0, nCases):
        nStudents, nFriendPairs = map(int, raw_input().split())
        print doPicnic([False]*nStudents, genFS(raw_input().split()))

if __name__ == "__main__" :
    main()
