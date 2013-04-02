#!/usr/bin/env python
nBase = 2
def doNormalize(lstN):
    lstN.append(0)
    for i in xrange(len(lstN)-1):
        if lstN[i] < 0:
            nBorrow = (abs(lstN[i]) + (nBase-1)) / nBase
            lstN[i+1] -= nBorrow
            lstN[i]   += nBorrow * nBase
        else:
            lstN[i+1] += lstN[i] / nBase
            lstN[i] %= nBase
    if lstN[-1] == 0: lstN.pop()

def addTo(lstA, lstB):
    ret = []
    for i in xrange(len(lstB)):
        if ( len(lstA) > i):
            ret.append(lstA[i] + lstB[i])
        else:
            ret.append(lstB[i])
    return ret

def subFrom(lstA, lstB):
    ret = []
    for i in xrange(len(lstB)):
        if ( len(lstA) > i):
            ret.append(lstA[i] - lstB[i])
        else:
            ret.append(-lstB[i])
    return ret

def doMultiply(lstA, lstB):
    ret = [0] * (len(lstA) + len(lstB) + 1)
    for i in xrange(len(lstA)):
        for j in xrange(len(lstB)):
            ret[i+j] += lstA[i] * lstB[j]
    #doNormalize(ret)
    return ret

def doKaratsuba(lstA, lstB):
    nA = len(lstA)
    nB = len(lstB)
    #print "nA(%d), nB(%d)"%(nA, nB)
    if nA < nB: return doKaratsuba(lstB, lstA)
    if nA == 0 or nB == 0: return []
    if nA < 50: return doMultiply(lstA, lstB)

    nHalf = nA / 2

    lstA0 = lstA[0:nHalf]
    lstA1 = lstA[nHalf:]
    lstB0 = lstB[0:min(len(lstB), nHalf)]
    lstB1 = lstB[min(len(lstB), nHalf):]

    lstZ2 = doKaratsuba(lstA1, lstB1)
    lstZ0 = doKaratsuba(lstA0, lstB0)

    lstA0 = addTo(lstA0, lstA1)
    lstB0 = addTo(lstB0, lstB1)

    lstZ1 = doKaratsuba(lstA0, lstB0)

    lstZ1 = subFrom(lstZ1, lstZ0)
    lstZ1 = subFrom(lstZ1, lstZ2)

    lstR = lstZ0 + lstZ1 + lstZ2

    return lstR

def doFanMeeting(lstIdol, lstFan):
    return doKaratsuba(lstIdol, lstFan)[len(lstIdol)-1:len(lstFan)].count(0)

def main():
    nCases = int(raw_input())
    for _ in xrange(0, nCases):
        lstIdol = [0 if i == 'F' else 1 for i in raw_input()]
        lstFan = [0 if i == 'F' else 1 for i in reversed(raw_input())]
        print doFanMeeting(lstIdol, lstFan)
        #print "====="

if __name__ == "__main__":
    main()
