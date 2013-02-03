#include <cstdio>
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
char garrBoard[gnSize] = {0,};
char garrWord[10][11] = {0,};

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
                printf("%s NO\n", arrWord[nWC]);
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
                    printf("%s YES\n", arrWord[nWC]);
                    break;
                }
                pStart = find(pStart+1, pEnd, arrWord[nWC][0]);
            }

            if (pStart == pEnd)
                printf("%s NO\n", arrWord[nWC]);
        }
    }
}


int main (int argc, char** argv)
{
    int nStageCount = 0;
    int nWordCount = 0;

    scanf("%d", &nStageCount);
    while (nStageCount--)
    {
        char *pStage = garrBoard + gnWidth + 1;
        for (int i = 0; i < 5; i++)
            scanf("%s", (pStage + i*gnWidth));

        scanf("%d", &nWordCount);
        for (int i = 0; i < nWordCount; i++)
            scanf("%s", garrWord[i]);

        doBoggleGame(garrBoard, garrWord, nWordCount);
    };

    return 0;
}
