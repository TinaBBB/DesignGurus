import math

class Solution:
  def countChange(self, denominations, total):
    # Bottom-up Solution

    # Denomi idx | 0 1 2 3 4 5
    #   1     0  | 2 2 1 1 1 0
    #   2     1  | 2 2 1 1 x 0
    #   3     2  | x x 1 x x 0
    #   -     3  | x x x x x x 
    # Base cases are oob row and at total, which takes 0 coins to get to
    last_row = [float("inf") for _ in range(total+1)]

    for idx in range(len(denominations)-1, -1, -1):
      new_row = [float("inf") for _ in range(total)] + [0]
      for curr_sum in range(total-1, -1, -1):
        # option 1: not choose the current one and go to the next one
        num_ways_not_choose = last_row[curr_sum]

        # option 2: choose current one and stay
        num_ways_choose = float("inf")
        if denominations[idx] + curr_sum <= total:
          num_ways_choose = 1 + new_row[curr_sum + denominations[idx]]
        
        # optimal ways to get
        num_ways_optimal = min(num_ways_not_choose, num_ways_choose)
        new_row[curr_sum] = num_ways_optimal
      
      last_row = new_row
    
    result = new_row[0] 
    return result if result != float("inf") else -1


 
    # Top-down Solution, with recursive functions
    dp = {}

    def dfs(curr_idx, curr_sum, curr_num_coins):
      # Base Case, getting results:
      if curr_sum == total:
        dp[(curr_idx, curr_sum)] = min(dp.get((curr_idx, curr_sum), float("inf")), curr_num_coins)
        return dp[(curr_idx, curr_sum)]

      # Base Case, oob or over value:
      if curr_idx >= len(denominations) or curr_sum > total:
        return float("inf")
      
      # Base Case, existed path:
      # Note that an existed path can be explored later with a better solution.
      if (curr_idx, curr_sum) in dp and curr_num_coins >= dp[(curr_idx, curr_sum)]:
        return dp[(curr_idx, curr_sum)]

      # Loop through actions
      # Option 1: choose current coin and stay
      num_ways_choose = dfs(curr_idx, curr_sum+denominations[curr_idx], curr_num_coins+1)

      # Option 2: not choose current coin and pass
      num_ways_not_choose = dfs(curr_idx+1, curr_sum, curr_num_coins)

      min_num_ways = min(num_ways_choose, num_ways_not_choose)
      dp[(curr_idx, curr_sum)] = min_num_ways
      return min_num_ways
    
    result = dfs(0, 0, 0)
    return result if result != float("inf") else -1
