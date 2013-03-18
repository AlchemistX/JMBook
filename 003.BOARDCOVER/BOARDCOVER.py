#!/usr/bin/env python

def genBlock(nStride):
    ret = []
    ret.append((0, 1          , nStride    ))
    ret.append((0, 1          , nStride + 1))
    ret.append((0, nStride    , nStride + 1))
    ret.append((0, nStride - 1, nStride    ))
    return ret

def setBlock(strBoard, tupBlock, nPos):
    if  chr(strBoard[nPos+tupBlock[0]]) == '.' and chr(strBoard[nPos+tupBlock[1]]) == '.' and chr(strBoard[nPos+tupBlock[2]]) == '.':
        strBoard[nPos+tupBlock[0]] = 'B'
        strBoard[nPos+tupBlock[1]] = 'B'
        strBoard[nPos+tupBlock[2]] = 'B'
        return True
    return False

def rstBlock(strBoard, tupBlock, nPos):
    strBoard[nPos+tupBlock[0]] = '.'
    strBoard[nPos+tupBlock[1]] = '.'
    strBoard[nPos+tupBlock[2]] = '.'
    return True

def doBoardCover(strBoard, lstBlock, nWidth, nHeight, nStride):
    if strBoard.count('.') % 3: return 0
    P = strBoard.find('.')
    if P == -1 : return 1
    ret = 0
    for T in xrange(0, 4):
        if setBlock(strBoard, lstBlock[T], P):
            ret += doBoardCover(strBoard, lstBlock, nWidth, nHeight, nStride)
            rstBlock(strBoard, lstBlock[T], P)
    return ret

def main():
    nCases = int(raw_input())
    for _ in xrange(0, nCases):
        nHeight, nWidth = map(int, raw_input().split())
        nStride = nWidth + 2
        strPadding = 'M' * nStride
        strBoard = bytearray()
        for _ in xrange(0, nHeight):
            strBoard += 'M'
            strBoard += raw_input()
            strBoard += 'M'
        strBoard += strPadding
        print doBoardCover(strBoard, genBlock(nStride), nWidth, nHeight, nStride)

if __name__ == "__main__":
    main()

