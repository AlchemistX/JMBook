#!/usr/bin/env python

nBoardWidth = 5
nBoardHeight = 5

# ===========
# | | | | | |
# ===========
# | | | | | |
# ===========
# | | | | | |
# ===========
# | | | | | |
# ===========
# | | | | | |
# ===========

def tr1Dto2D(nIdx):
    return (nIdx%nBoardWidth, nIdx/nBoardWidth)

def tr2Dto1D(tupCoord):
    return tupCoord[0] + tupCoord[1] * nBoardWidth

def isConn(strBoard, tupCoord, C):
    CO = ((tupCoord[0] - 1), (tupCoord[1] - 1))
    if ((CO[0] >= 0) and (CO[1] >= 0)) : print "upper left"
    if ((tupCoord[0] - 0) >= 0) and ((tupCoord[1] - 1) >= 0) : print "upper"
    if ((tupCoord[0] + 1) <  5) and ((tupCoord[1] - 1) >= 0) : print "upper right"
    if ((tupCoord[0] - 1) >= 0) and ((tupCoord[1] - 0) >= 0) : print "left"
    if ((tupCoord[0] + 1) <  5) and ((tupCoord[1] - 0) >= 0) : print "right"
    if ((tupCoord[0] - 1) >= 0) and ((tupCoord[1] + 1) <  5) : print "lower left"
    if ((tupCoord[0] - 0) >= 0) and ((tupCoord[1] + 1) <  5) : print "lower"
    if ((tupCoord[0] + 1) <  5) and ((tupCoord[1] + 1) <  5) : print "lower right"

def doBoggleGame(strBoard, lstWords):
    for strWord in lstWords :
        nIdx = strBoard.find(strWord[0])
        if nIdx < 0 : print strWord + " NO"
        else :
            print nIdx
            print tr1Dto2D(nIdx)
            print tr2Dto1D(tr1Dto2D(nIdx))



def main():
    strBoard = ""
    nStageCount = raw_input()
    for i in xrange(0, int(nStageCount)) :
        for n in xrange(0, 5) :
            strBoard += raw_input()

        lstWords = []
        nWordCount = raw_input()
        for n in xrange(0, int(nWordCount)) :
            lstWords.append(raw_input())

        doBoggleGame(strBoard, lstWords)
            

if __name__ == "__main__" :
    main()

