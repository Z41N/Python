# Recursive solution (however, iterative would be faster @ O(N)
# Avg. T = O(log(N))
# Avg. S = O(log(N))
# Worst T = O(N)
# Worst S = O(N)
def findClosestValueInBst(tree, target):
	return z_helper(tree, target, float("inf"))

# First thing, let's create a helper method
# Similar to whiteboard concept to keep track of closest value
def z_helper(tree, target, closest):
	# If no more branches, return None
	if tree is None:
		return closest
	# If our current closest > node, update closest to be the node
	if abs(target-closest) > abs(target-tree.value):
		closest = tree.value
	# If target < node, go down the left branch
	if target < tree.value:
		return z_helper(tree.left, target, closest)
	# Else if target > node, go down the right branch
	elif target > tree.value:
		return z_helper(tree.right, target, closest)
	# We've accounted for everything except target = closest 
	else:
		return closest
