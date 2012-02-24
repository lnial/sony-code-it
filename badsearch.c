#include <stdio.h>
#define MAX 100000

typedef int DataType;
int n;
DataType x[MAX];



int bsearch(DataType t) {
    int l, u, m;
    l = 0;
    u = n - 1;
    printf("THIS_LINE\n");
    while (l <= u ) {
        m = (l + u)/2;
        printf("%d %d %d\n", l, u, m);
        if (x[m] < t)
            l = m + 1;
        else if (x[m] > t) 
            u = m;
        else 
            return m;
    }
    return -1;

}

int main(int argc, char const* argv[])
{
    int i = 0;
    int t = 5, 
        n = 20;
    for (i = 0; i < n; i++) 
        x[i] = 10*i;
    printf("%d\n", bsearch(t));
    return 0;
}
