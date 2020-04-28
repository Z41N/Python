# O(N) time (constant time)
# O(N) space (returning list of sums. Length = N)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    running_list = []
	z_helper(root, 0, running_list)
	return running_list

# keep track of running sum (for branch sums)
# keep track of running list (answer to this q)
def z_helper(node, running_sum, running_list):
	if node is None:
		return
	new_running_sum = running_sum + node.value
	# If we're at a leaf, just add the sum to list
	if node.left is None and node.right is None:
		running_list.append(new_running_sum)
		return
	# Recursively call helper on 2 children nodes
	# Passes the new running sum and constant list
	z_helper(node.left, new_running_sum, running_list)
	z_helper(node.right, new_running_sum, running_list)
	
