class Solution {
public:
    int trail_zeroes(vector<int>& row) {
        int z = 0;
        for (int i = 0; i < row.size(); i += 1) {
            if (row[i] == 0)
                z += 1;
            else
                z = 0;
        }
        return z;
    }
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> zeros(n);

        // count trailing zeros
        for (int i = 0; i < n; i++)
            zeros[i] = trail_zeroes(grid[i]);

        int ops = 0;

        for (int i = 0; i < n; i++) {
            int need = n - i - 1;

            int k = i;
            while (k < n && zeros[k] < need)
                k++;

            if (k == n)
                return -1; // impossible

            // bring row up using adjacent swaps
            while (k > i) {
                swap(zeros[k], zeros[k - 1]);
                ops++;
                k--;
            }
        }

        return ops;
    }
};