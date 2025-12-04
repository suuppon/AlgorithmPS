#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int zero[41];
    int one[41];

    zero[0] = 1; one[0] = 0;
    zero[1] = 0; one[1] = 1;

    for (int i = 2; i <= 40; ++i) {
        zero[i] = zero[i - 1] + zero[i - 2];
        one[i]  = one[i - 1]  + one[i - 2];
    }

    int T;
    std::cin >> T;

    while (T--) {
        int N;
        std::cin >> N;
        std::cout << zero[N] << " " << one[N] << '\n';
    }

    return 0;
}