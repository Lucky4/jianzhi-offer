class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    if j == 0:
                        dp[j] = grid[i][j]
                    else:
                        dp[j] = grid[i][j] + dp[j-1]
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + max(dp[j-1], dp[j])
        
        return dp[cols-1]