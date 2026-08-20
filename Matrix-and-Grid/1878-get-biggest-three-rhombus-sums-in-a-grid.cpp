class Solution {
public:

    // perimeter sum of rhombus
    int rhombusArea(const vector<vector<int>>& grid,int x, int y, int r, int rows, int cols) {
        if (r == 0) return grid[x][y];
        int sum = 0;

        // 4 edges
        for (int k = 0; k < r; k++) {
            // top -> right
            sum += grid[x - r + k][y + k];

            // right -> bottom
            sum += grid[x + k][y + r - k];

            // bottom -> left
            sum += grid[x + r - k][y - k];

            // left -> top
            sum += grid[x - k][y - r + k];
        }

        return sum;
    }

    vector<int> getBiggestThree(vector<vector<int>>& grid) {

        int rows = grid.size();
        int cols = grid[0].size();

        set<int, greater<int>> best; // keeps sorted + distinct

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {

                int r = 0;

                while (true) {

                    // check rhombus validity
                    if (i - r < 0 || i + r >= rows ||
                        j - r < 0 || j + r >= cols)
                        break;

                    int area = rhombusArea(grid, i, j, r, rows, cols);

                    best.insert(area);

                    // keep only top 3
                    if (best.size() > 3)
                        best.erase(prev(best.end()));

                    r++;
                }
            }
        }

        return vector<int>(best.begin(), best.end());
    }
};