public class Solution {
    public int MaxProductPath(int[][] grid) {
        (long min, long max)[,] prod_grid = new (long min, long max)[grid.Length, grid[0].Length];
        prod_grid[0, 0].min = prod_grid[0, 0].max = grid[0][0];
        
        for (int i = 1; i < grid.Length; ++i) {
            prod_grid[i, 0].min = prod_grid[i, 0].max = grid[i][0] * prod_grid[i-1, 0].max;
        }
        for (int i = 1; i < grid[0].Length; ++i) {
            prod_grid[0, i].min = prod_grid[0, i].max = grid[0][i] * prod_grid[0, i-1].max;
        }
        
        for (int i = 1; i < grid.Length; ++i) {
            for (int j = 1; j < grid[0].Length; ++j) {
                long new_val1 = grid[i][j] * Math.Min(prod_grid[i-1, j].min, prod_grid[i, j-1].min);
                long new_val2 = grid[i][j] * Math.Max(prod_grid[i-1, j].max, prod_grid[i, j-1].max);
                prod_grid[i, j] = (Math.Min(new_val1, new_val2), Math.Max(new_val1, new_val2));
            }
        }
        
        long result = prod_grid[grid.Length-1, grid[0].Length-1].max;
        
        return result >= 0? (int)(result % ((int)Math.Pow(10, 9) + 7)): -1;
    }
}