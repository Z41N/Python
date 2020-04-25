# Take advantage of sort property
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	# Len - 1 because of the last index on right 
	right = len(array) - 1
	while left < right:
		combinedSum = array[left] + array[right]
		if combinedSum == targetSum:
			return [array[left], array[right]]
		elif combinedSum < targetSum:
			left += 1
		elif combinedSum > targetSum:
			right -= 1
	return []
 
