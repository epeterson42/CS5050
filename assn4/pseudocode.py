# Finds the successor given a value.
# Returns None if no node exists that is larger 
#   or equal to the value.
# For the initial call use None for the value
#   of the successor
def successor(value, node, successor):
        # reached the end of the tree
        if node == None:
            return successor
        # Found the value
        elif node.value == value:
            return node.value
        # value lies to the left
        elif value < node.value:
            return successor(value, node.left, node.value)
        # value lies to the right
        else:
            return successor(value, node.right, successor)




# returns the elements between min and max inclusive and in order
def rangeQ(root, min, max, out):

    # Recurse down left tree
    if root.left != None:
        # If the left node is greater than the min keep going left
        if (root.left != None and root.left.val >= min):
            rangeQ(root.left, min, max, out)
        # If the left node is below the range but has a right child, some of
        # the children may be in range.
        elif(root.left.right != None):
            rangeQ(root.left.right, min, max, out) # Skips to the child
        else:
            pass
    # Add current node to output        
    if root.val != None and min <= root.val <= max:
        out.append(root.val)
    
    # Recurse right tree
    if root.right != None:
        # if the right node's value is less than the max keep going right
        if (root.right != None and root.right.val <= max):
            rangeQ(root.right, min, max, out)
        # If the right node has a left node, left nodes may be in range so they need to be searched
        elif(root.right.left != None):
            rangeQ(root.right.left, min, max, out) # Skips to the child
        else:
            pass
    return out

# Finds the sum of nodes between the given range
def rangeSum(root, min, max):
    # sum to keep track of total
    sum = 0

    # the least common ancestor to start the search
    node = root.lca(min, max)   
    if node is None:
        return None
    sum = node.value # LCA is included in the range
    
    # Add sums on the left side
    leftNode = node.left
    while leftNode:
        if leftNode.value >= min:
            # we can use the sum attribute of the right
            # nodes to add the sum on all its children
            # because we know its in range.
            if leftNode.right:
                sum += leftNode.right.sum
            sum += leftNode.value
            leftNode = leftNode.left  # keep going left

        else:
            leftNode = leftNode.right # check right to find min

    # add sums on the right side
    rightNode = node.right
    while rightNode:
        if rightNode.value <= max:
            if rightNode.left:
                sum += rightNode.left.sum
            sum += rightNode.value
            rightNode = rightNode.right # keep going right

        else:
            rightNode = rightNode.left # check left to keep going to max
    
    return sum
            

# Find the least common ancestor for any min and max in a tree
# if the range is not in the tree, it will give a value that is larger
#   than max which can be checked for in implementation
def lca(root, min, max):
    
    # Base Case
    if root is None:
        return None

    # If both min and max are smaller than root, then LCA lies in left
    if(root.value > min and root.value > max and root.left is not None):
        return root.left.lca(min, max)

    # If both min and max are greater than root, then LCA lies in right
    if(root.value < min and root.value < max and root.right is not None):
        return root.right.lca(min, max)

    return root
    
# find the rank of a node using size attribute
def rank(root, x):
    if root == None:
        return 0 # no size to be added
    # going down the right subtree
    if root.value <= x:
        if root.left == None:
            # no left node, just add current node and keep going
            return 1 + rank(root.right, x) 
        else:
             # add the size of left tree then keep going right
            1 + root.left.size + rank(root.right, x)
    # go left, to keep going down the right tree of the left child
    else:
        return rank(root.left, x)
    

counter = 0
def checkSmallest(node, k, x):
    if (node.value < x):
        counter = counter + 1
        if (counter > k):
            return
        checkSmallest(node.left, k, x)
        checkSmallest(node.right, k, x)


is_x_smaller_than_kth = False
checkSmallest(root, k, x)
if (counter <= k):
    is_x_smaller_than_kth = True



