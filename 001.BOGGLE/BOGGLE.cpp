#include <iostream>
#include <cstring>

const int gnWidth = 7;
const int gnHeight = 7;
const int gnSize = gnWidth*gnHeight;
const int garrCoord[8] = 
{
    -gnWidth - 1,
    -gnWidth - 0,
    -gnWidth + 1,
             - 1,
             + 1,
    +gnWidth - 1,
    +gnWidth + 0,
    +gnWidth + 1
};

inline char* find(char *pBegin, char *pEnd, char nVal)
{
    while (pBegin != pEnd)
    {
        if (*pBegin == nVal) return pBegin;
        ++pBegin;
    }

    return pEnd;
}

inline bool step(char *pBoard, char *pStart, char *szWord, char nLength, int nCur)
{
    if (nLength == nCur)
        return true;
    
    for (int i = 0; i < 8; i++)
    {
        char *pPos = pStart + garrCoord[i];
        if (*pPos == szWord[nCur])
            if (step(pBoard, pPos, szWord, nLength, nCur+1))
                return true;
    }
    return false;
}

inline void doBoggleGame(char *pBoard, char arrWord[10][11], int nWordCount)
{
    char *pBegin = pBoard;
    char *pEnd = pBoard+gnSize;

    for (int nWC = 0; nWC < nWordCount; nWC++)
    {
        int nLength = strlen(arrWord[nWC]);
        bool fGO = true;
        for (int i = nLength; i >= 0; --i)
        {
            if (find(pBegin, pEnd, arrWord[nWC][i]) == pEnd)
            {
                std::cout << arrWord[nWC] << " NO" << std::endl;
                fGO = false;
            }
        }

        if (fGO)
        {
            char *pStart = find(pBegin, pEnd, arrWord[nWC][0]);
            while (pStart != pEnd)
            {
                if (step(pBoard, pStart, arrWord[nWC], nLength, 1))
                {
                    std::cout << arrWord[nWC] << " YES" << std::endl;
                    break;
                }
                pStart = find(pStart+1, pEnd, arrWord[nWC][0]);
            }

            if (pStart == pEnd)
                std::cout << arrWord[nWC] << " NO" << std::endl;
        }
    }
}

int main (int argc, char** argv)
{
    int nStageCount = 0;
    int nWordCount = 0;
    char arrBoard[gnSize];
    char arrWord[10][11];

    std::cin >> nStageCount;
    while (nStageCount--)
    {
        memset (arrBoard, 0, sizeof(arrBoard));
        memset (arrWord, 0, sizeof(arrWord));

        char *pStage = arrBoard + gnWidth + 1;
        for (int i = 0; i < 5; i++)
            std::cin >> (pStage + i*gnWidth);

        std::cin >> nWordCount;
        for (int i = 0; i < nWordCount; i++)
            std::cin >> arrWord[i];

        doBoggleGame(arrBoard, arrWord, nWordCount);
    };

    return 0;
}
