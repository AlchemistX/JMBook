#!/usr/bin/env python
gnWidth = 7
gnHeight = 7
lstCoord = [ -gnWidth-1, -gnWidth-0, -gnWidth+1, -1, +1, gnWidth-1, gnWidth+0, gnWidth+1]

def step(strBoard, nStart, strWord, nCur):
    if nCur == len(strWord):
        return True

    for delta in lstCoord:
        idx = nStart + delta
        if strBoard[idx] == strWord[nCur]:
            if step(strBoard, idx, strWord, nCur+1) == True:
                return True

    return False

def doBoggleGame(strBoard, lstWords):
    for strWord in lstWords:
        fGO = True
        for C in strWord:
            if strBoard.find(C) < 0:
                print "%s NO" % (strWord)
                fGO = False
                break

        if fGO :
            idx = strBoard.find(strWord[0])
            while (idx > 0):
                if step(strBoard, idx, strWord, 1) == True:
                    print "%s YES" % (strWord)
                    break
                idx = strBoard.find(strWord[0], idx+1)

            if idx < 0 :
                print "%s NO" % (strWord)

def main():
    strBoard = ""
    nStageCount = raw_input()
    for i in xrange(0, int(nStageCount)) :
        strBoard =""
        strBoard += '0' * gnWidth
        for n in xrange(0, 5) :
            strBoard += '0'
            strBoard += raw_input()
            strBoard += '0'
        strBoard += '0' * gnWidth

        lstWords = []
        nWordCount = raw_input()
        for n in xrange(0, int(nWordCount)) :
            lstWords.append(raw_input())

        doBoggleGame(strBoard, lstWords)

if __name__ == "__main__" :
    main()
    
