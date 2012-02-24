#include <stdio.h>
#include <assert.h>
#define MAX 100000

typedef int DataType;
int n;
DataType x[MAX];

int bsearch(DataType t) {
    int l, u, m;
    l = 0;
    u = n - 1;
    while (l<=u ) {
        m = (l + u)/2;
        if (x[m]<t)
            l = m + 1;
        else if (x[m] == t) 
            return m;
        else 
            u = m-1;
    }
    return -1;

}

int main(int argc, char const* argv[])
{
    int i = 0;
    int t = 10, 
        n = 2;

    for (i = 0; i < n; i++) 
        x[i] = 10*i;
    printf("%d\n", bsearch(t));
    return 0;
}
