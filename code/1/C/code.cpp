#include <iostream>
#include <vector>

using namespace std;

int main() {
    int q;
    cin >> q;

    vector<int> snakes(q); // 蛇の長さを保持する配列

    for (int i = 0; i < q; i++) {
        int k, l;
        cin >> k >> l;

        if (k == 1) {
            snakes[i] = l;
        } else if (k == 2) {
            snakes.erase(snakes.begin());
        } else if (k == 3) {
            int sum = 0;
            for (int j = 0; j < l - 1; j++) {
                sum += snakes[j];
            }
            cout << sum << endl;
        }
    }

    return 0;
}