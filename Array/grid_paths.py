# Grid Paths:


# Brute force appraoch (Using  Recursion)
class Solution:
    def uniquePaths(self, m, n):
        return self.dfs(0, 0, m, n)
    
    def uniquePaths2(self, m, n):
        #Intialize a 2D dp array with -1
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dfs2(0, 0, m, n, dp)
        
    def dfs(self, i, j, m, n):

        # Base case: 
        # Already at the last cell
        if i == m - 1 and j == n - 1:
            return 1
        # Out of the grid
        if i >= m or j >= n:
            return 0
        
        return self.dfs(i + 1, j, m, n) + self.dfs(i, j + 1, m, n)
    
    def dfs2(self, i, j, m, n, dp):
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        dp[i][j] = self.dfs2(i + 1, j, m, n, dp) + self.dfs2(i, j + 1, m, n, dp)
        return dp[i][j]
    


sol = Solution()
print(sol.uniquePaths(2, 3))   
print(sol.uniquePaths2(4, 5))