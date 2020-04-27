# Iterative approach

# Average: O(log(N)) time | O(1) space
# Worst: O(N) time | O(1) space 


def findClosestValueInBst(tree, target):
	return z_helper(tree, target, float("inf"))

# Helper method to keep track of closest value
def z_helper(tree, target, closest):
	# Current node will be whatever we start on the tree
	current_node = tree
	while current_node is not None:
		if abs(target - closest) > abs(target - current_node.value):
			closest = current_node.value
		if target > current_node.value:
			current_node = current_node.right
		elif target < current_node.value:
			current_node = current_node.left
		else:
			break
	# Break if none and return closest
	return closest
