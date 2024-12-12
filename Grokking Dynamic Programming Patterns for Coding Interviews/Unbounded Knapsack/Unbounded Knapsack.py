class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    # Bottom-up Memoization Solution
    
    # Initiate the base case solution
    last_row = [0 for summed_cap in range(capacity+1)]

    # Loop through the index rows and remaining capacity columns
    for curr_idx in range(len(profits)):
      curr_row = [0 for summed_cap in range(capacity+1)]
      for remaining_sum in range(1, capacity+1):
        # Profit if not selecting the current index
        profit_not_select = last_row[remaining_sum]

        # Profit if select the current index, buts to be valid through
        profit_select = 0 
        if weights[curr_idx] <= remaining_sum:
          # Get to the next stage, where remaining weight is deducted, 
          # Get immediate profit + future profit
          profit_select = profits[curr_idx] + curr_row[remaining_sum - weights[curr_idx]]

        curr_row[remaining_sum] = max(profit_not_select, profit_select)
      
      print(curr_row)
      last_row = curr_row
    
    # This is where we start from the back index, and remaining sum equals to full capacity.
    return last_row[-1]


    # # Top-down Tabulation Solution
    # dp = {}

    # def dfs(curr_idx, curr_weight_sum, curr_profit_sum):
    #   # Base Case 1: OOB or reaches capacity limit 
    #   if curr_idx >= len(weights) or curr_weight_sum == capacity:
    #     return curr_profit_sum

    #   # Base Case 2: Over value, invalid path, return 0
    #   if curr_weight_sum > capacity:
    #     return 0 
      
    #   # Base Case 3: Existence of status
    #   if (curr_idx, curr_weight_sum) in dp:
    #     return dp[(curr_idx, curr_weight_sum)]

    #   # Loop through actions, select the current one stay; not select the current one
    #   # Option 1: not selecting the current one and go to the next 
    #   profit1 = dfs(curr_idx+1, curr_weight_sum, curr_profit_sum)

    #   # Option 2: selecting the current one
    #   profit2 = dfs(curr_idx, curr_weight_sum+weights[curr_idx], curr_profit_sum+profits[curr_idx])

    #   max_profit = max(dp.get((curr_idx, curr_weight_sum), 0), profit1, profit2)
    #   dp[(curr_idx, curr_weight_sum)] = max_profit
    #   return max_profit
    
    # return dfs(0, 0, 0)


