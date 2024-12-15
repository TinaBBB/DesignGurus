class Solution:
  def countChange(self, denominations, total):
    # Bottom-up 
    # dom  idx |  0  1  2  3  4  |5
    # ------------------------------
    #  1    0  |  5  4  3  2  1  |1    
    #  2    1  |  1  1  1  1  0  |1 
    #  3    2  |  0  0  1  0  0  |1
    # ------------------------------ 
    #  -    3  |  0  0  0  0  0   0 

    last_row = [0 for col in range(total+1)]

    # Runs from bottom right to top left
    for idx in range(len(denominations)-1, -1, -1):
      new_row = [0 for col in range(total)] + [1]
      for total_sum in range(total-1, -1, -1):
        # If not choosing the current Option
        num_ways_not_select = last_row[total_sum]

        # If choosing the current Option
        num_ways_select = 0
        if denominations[idx] + total_sum <= total:
          num_ways_select = new_row[total_sum + denominations[idx]]
        
        new_row[total_sum] = num_ways_not_select + num_ways_select

      last_row = new_row
    
    return last_row[0]

        




    # # Top-down 
    # dp = {}  # stores nuumber of ways to reach total for the current index and total sum state

    # def dfs(curr_idx, curr_sum):
    #   # Base Case if matching with total
    #   if curr_sum == total:
    #     return 1
      
    #   # Base case if oob or over sum
    #   if curr_idx >= len(denominations) or curr_sum > total:
    #     return 0
      
    #   # If sub-path has already been explored
    #   if (curr_idx, curr_sum) in dp:
    #     return dp[(curr_idx, curr_sum)]
      

    #   # Checks the results from different actions
    #   #Option 1: don't choose and go to the next index
    #   #Option 2: choose the current one and still chesk the same index
    #   num_ways = dfs(curr_idx, curr_sum+denominations[curr_idx]) + dfs(curr_idx+1, curr_sum)
    #   dp[(curr_idx, curr_sum)] = num_ways
    #   return num_ways
    

    # return dfs(0, 0)




    
