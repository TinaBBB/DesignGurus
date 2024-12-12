class Solution:
  def solveRodCutting(self, lengths, prices, n):
    # Bottom-up Memoization 

    # Initiate memoization last out-of-index row
    last_row = [0 for remaining_length in range(n+1)]

    # Loop through available row (cur length) and column (summed length values)
    for curr_idx in range(len(lengths)-1, -1, -1):
      curr_length_option = lengths[curr_idx]
      curr_row = [0 for remaining_length in range(n+1)]
      for curr_sum_length in range(n-1, -1, -1):
        #profit if not selecting
        profit_not_select = last_row[curr_sum_length]

        # profit if selecting
        profit_select = 0
        if curr_length_option <= n - curr_sum_length:
          profit_select = prices[curr_idx] + curr_row[curr_sum_length + curr_length_option]
        
        optimal_profit = max(profit_not_select, profit_select)
        curr_row[curr_sum_length] = optimal_profit

      last_row = curr_row
    
    return curr_row[0]

    # Top-down Tabulation 
    dp = {}

    def dfs(curr_idx, curr_length_sum, curr_price_sum):
      # Base Case idx OOB or rod value exceeds
      if curr_idx >= len(lengths) or curr_length_sum > n:
        return 0

      # Base Case used up allocations, 
      if curr_length_sum == n:
        return curr_price_sum

      # Base Case, existence in dp dict
      if (curr_idx, curr_length_sum) in dp:
        return dp[(curr_idx, curr_length_sum)]
      
      # Loop through possible actions
      cutable_length = n - curr_length_sum

      for cut_length in range(1, cutable_length + 1):
        #profit if not select the current option
        profit_not_select = dfs(curr_idx+1, curr_length_sum, curr_price_sum)

        # profit if selecting the current option
        profit_selct = dfs(curr_idx, curr_length_sum + lengths[curr_idx], curr_price_sum+prices[curr_idx])

        optimal_profit = max(profit_not_select, profit_selct)
        dp[(curr_idx, curr_length_sum)] = optimal_profit
        return optimal_profit
      
    # call dfs function
    return dfs(0, 0, 0)
      
