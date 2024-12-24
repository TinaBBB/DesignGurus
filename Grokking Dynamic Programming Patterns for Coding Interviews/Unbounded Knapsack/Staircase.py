class Solution:
  def countWays(self, n):
    # states: current_idx
    # actions: step 1, 2, 3

    # button-up tabulation
    # idx |  actions  optimual
    #     |  1  2  3
    # -------------------------
    #  0  |  2  1  1     4 
    #  1  |  1  1  x     2
    #  2  |  1  x  x     1
    # -------------------------
    #  3  |  1  1  1     1
    dp = {n:1}

    for curr_idx in range(n-1, -1, -1):
      # loop through actions
      total_ways = 0
      for step in range(1, 4):
        next_idx = curr_idx + step
        if next_idx <= n:
          curr_ways = dp.get(next_idx, 0)
          total_ways += curr_ways
      dp[curr_idx] = total_ways
    
    return dp[0]



    # # top-down memoization 
    # dp = {}

    # def dfs(current_idx):
    #   # base case, getting to the last step 
    #   if current_idx == n:
    #     return 1
      
    #   # base case, out of bound
    #   if current_idx >= n+1:
    #     return -1

    #   # if already explored
    #   if current_idx in dp:
    #     return dp[current_idx]
      

    #   # explore different actions
    #   total_ways = 0
    #   for step in range(1,4):
    #     num_ways = dfs(current_idx+step)
    #     if num_ways >= 0:
    #       total_ways += num_ways
      
    #   dp[current_idx] = total_ways

    #   return dp[current_idx]
    
    # return dfs(0)
