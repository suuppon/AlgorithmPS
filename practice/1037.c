#include <stdio.h>

int main()
{
    int n;
    long long max = 0, min = 1000001;

    int n_divisors;

    scanf("%d", &n_divisors);

    for(int i = 0; i < n_divisors; i++){
        scanf("%d", &n);

        if(n > max)
            max = n;
        if(n < min)
            min = n;
    }

    printf("%lld", min * max);

    return 0;
}