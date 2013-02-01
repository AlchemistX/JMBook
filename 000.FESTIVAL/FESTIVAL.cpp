#include <iostream>
#include <iomanip>

int calcSum(int cnt, int* D)
{
    int sum = 0;
    for (int idx = 0; idx < cnt; idx++)
        sum += D[idx];

    return sum;
}

double calcMinimalAvg(int N, int L, int* D)
{
    int nLocalSum = 0;
    int nMinimalSum = 0;
    double nLocalAvg = 0.0;
    double nMinimalAvg = 100.0;

    for (int W = L; W <= N; W++)
    {
        nMinimalSum = W * 100;
        for (int idx = 0; idx <= (N-W); idx++)
        {
            if (idx == 0)   nLocalSum = calcSum(W, &D[idx]);
            else            nLocalSum = nLocalSum - D[idx-1] + D[idx+W-1];

            if (nLocalSum < nMinimalSum)
                nMinimalSum = nLocalSum;
        }
        nLocalAvg = nMinimalSum/double(W);
        if (nLocalAvg < nMinimalAvg)
            nMinimalAvg = nLocalAvg;
    }

    return nMinimalAvg;
}

int main (int argc, char** argv)
{
    int C, N, L, D[1000];

    std::cout << std::fixed << std::setprecision(10);
    std::cin.sync_with_stdio(false);
    std::cin >> C;
    while (C--)
    {
        std::cin >> N >> L;
        for (int idx=0; idx < N; idx++)
            std::cin >> D[idx];
        std::cout << calcMinimalAvg(N, L, D) << std::endl;
    }
}

