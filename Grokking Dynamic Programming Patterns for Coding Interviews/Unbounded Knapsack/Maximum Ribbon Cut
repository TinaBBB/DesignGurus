import math

class Solution:
  def countRibbonPieces(self, ribbonLengths, total):
    # Bottom-up Solution
    # length  idx | 0 1 2 3 4 | 5
    #   2      0  | 2 2 1 1 x | 0 
    #   3      1  | x x 1 x x | 0
    #   5      2  | 1 x x x x | 0
    # ------------------------------
    #   -      3    x x x x x | x
    last_row = [float("-infinity") for total_sum in range(total+1)]

    for curr_idx in range(len(ribbonLengths)-1, -1, -1):
      new_row = [float("-infinity") for total_sum in range(total)] + [0]
      for curr_sum in range(total-1, -1, -1):
        # num_coins_not_select
        num_coins_not_select = last_row[curr_sum]

        # number of coins if selected
        num_coins_select = float("-infinity")
        if ribbonLengths[curr_idx] + curr_sum <= total:
          num_coins_select = 1 + new_row[curr_sum + ribbonLengths[curr_idx]]

        optimal_num_coins = max(num_coins_not_select, num_coins_select)
        new_row[curr_sum] = optimal_num_coins
      
      last_row = new_row
    
    return last_row[0]


    # # Top-down Solution
    # dp = {}

    # def dfs(curr_idx, curr_sum, curr_coins):
    #   # Base Case if match
    #   if curr_sum == total:
    #     dp[(curr_idx, curr_sum)] = max(dp.get((curr_idx, curr_sum), 0), curr_coins)
    #     return dp[(curr_idx, curr_sum)]
    #   # Base Case if oob or over value
    #   if curr_idx >= len(ribbonLengths) or curr_sum > total:
    #     return 0 
      
    #   # Base Case if exists
    #   if (curr_idx, curr_sum) in dp and dp[(curr_idx, curr_sum)] >= curr_sum:
    #     return dp[(curr_idx, curr_sum)]
      
    #   # Loop through actions
    #   # num coins if not selecting the current coin
    #   num_coins_not_select = dfs(curr_idx+1, curr_sum, curr_coins)

    #   # num coins if selecting the current coin
    #   num_coins_select = dfs(curr_idx, curr_sum+ribbonLengths[curr_idx], curr_coins+1)

    #   optimal_num_coins = max(num_coins_not_select, num_coins_select)
    #   dp[(curr_idx, curr_sum)] = optimal_num_coins
    #   return optimal_num_coins
    
    # return dfs(0, 0, 0)

