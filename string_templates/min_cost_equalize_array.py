modulo = int(1e9 + 7)


def minCostToEqualizeArray(nums, cost1, cost2):
    n = len(nums)
    max_nums = max(nums)
    min_nums = min(nums)
    sum_nums = sum(nums)
    best_cost = float("inf")
    for elem_comp in range(max_nums, 2 * max_nums + 1):
        # total number of increments which make the elem_comp which ranges from the max to 2*max equal to
        # all the other remaining array elems
        increments = elem_comp * n - sum_nums
        # initialize cost to 0 for each iteration
        cost = 0
        min_comp_diff = elem_comp - min_nums
        # Number of increments to make the elements other than the minimum element equal to the current element
        # under context
        num_ops_increment_other_than_min = elem_comp * (n - 1) - (sum_nums - min_nums)
        # number of increments to make current element equal to max
        num_ops_to_increment_min = (elem_comp - min_nums)
        # If we require more operations to make the current element equal to the minimum we cannot pair the
        # minimum with the remaining elements hence we use cost1 aka increment the minimum element individually
        if num_ops_increment_other_than_min <= num_ops_to_increment_min:
            extra = num_ops_to_increment_min - (num_ops_increment_other_than_min)
            cost += extra * cost1
            increments -= extra
        # If we have odd number of increments remaining we cannot use cost2 since it requires a pair increment
        if increments % 2 != 0:
            increments -= 1
            cost += cost1
        # compare the cost of cost1*increments and cost2*increments/2 since it is pairwise
        cost += min(increments * cost1, (increments / 2) * cost2)
        best_cost = min(best_cost, cost)
    return best_cost % modulo


print(minCostToEqualizeArray([2, 3, 3, 3, 5], 2, 1))
