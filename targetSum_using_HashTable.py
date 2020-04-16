# x + y = targetSum
# Will use the array as x value
# Will use targetSum - x as y value
def twoNumberSum(array, targetSum):
	# Create a hash table
	nums = {}
	for num in array:
		potential_match = targetSum - num
		if potential_match in nums:
			return [num, potential_match]
		else:
			nums[num] = True
	return []
