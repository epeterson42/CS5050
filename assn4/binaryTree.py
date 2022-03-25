from tkinter.messagebox import NO


root = None;

class BSTNode:
    def __init__(self, val=None, parent=None):
        self.left = None
        self.right = None
        self.val = val
        self.sum = val
        self.size = 1
        self.parent = parent

    def insert(self, val):
        if not self.val:
            self.val = val
            self.sum = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val, self)
            self.left.UpdateSum()
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val, self)

        self.right.UpdateSum()

    def nodeSum(self):

        leftSum = 0
        rightSum = 0
        if self.left is not None:
            leftSum = self.left.sum
        if self.right is not None:
            rightSum = self.right.sum
        return leftSum + rightSum + self.val

    def UpdateSum(self):
        self.sum = self.nodeSum()
        if self.parent is not None:
            self.parent.UpdateSum()

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def successorH(self, value, current, successor):
            if current == None:
                return successor
            elif current.val == value:
                return current.val
            elif value < current.val:
                return self.successorH(value, current.left, current.val)
            else:
                return self.successorH(value, current.right, successor)



    def successor(self, value):
        return self.successorH(value, self, None)


    def rangeQ(self, min, max, out):

        # Recurse down left tree
        if self.left is not None:
            # If the left node is greater than the min keep going left
            if (self.left is not None and self.left.val >= min):
                self.left.rangeQ(min, max, out)
            # If the left node is below the range but has a right child, some of
            # the children may be in range.
            elif(self.left.right is not None):
                self.left.right.rangeQ(min, max, out) # Skips to the child
            else:
                pass
        # Add current node to output        
        if self.val is not None and min <= self.val <= max:
            out.append(self.val)
        
        # Recurse right tree
        if self.right is not None:
            # if the right node's value is less than the max keep going right
            if (self.right is not None and self.right.val <= max):
                self.right.rangeQ(min, max, out)
            # If the right node has a left node, left nodes may be in range so they need to be searched
            elif(self.right.left is not None):
                self.right.left.rangeQ(min, max, out) # Skips to the child
            else:
                pass
        return out

    def rangeSum(self, min, max):
        sum = 0
        node = self.lca(min, max)
        if node is None:
            return None
        sum = node.val
        leftNode = node.left
        while leftNode:
            if leftNode.val >= min:
                if leftNode.right:
                    sum += leftNode.right.sum
                sum += leftNode.val
                leftNode = leftNode.left

            else:
                leftNode = leftNode.right

        rightNode = node.right
        while rightNode:
            if rightNode.val <= max:
                if rightNode.left:
                    sum += rightNode.left.sum
                sum += rightNode.val
                rightNode = rightNode.right

            else:
                rightNode = rightNode.left
        
        return sum
             

    def lca(self, min, max):
     
        # Base Case
        if self is None:
            return None
    
        # If both min and max are smaller than self, then LCA
        # lies in left
        if(self.val > min and self.val > max and self.left is not None):
            return self.left.lca(min, max)
    
        # If both min and max are greater than self, then LCA
        # lies in right
        if(self.val < min and self.val < max and self.right is not None):
            return self.right.lca(min, max)
    
        return self
        

    

def main():
    # nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    nums = [25, 16, 48, 46, 47, 8, 9, 5, 20, 18, 23, 59]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)

    print(bst.lca(1, 14).val)

    print(bst.rangeSum(6,24))
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    print(f'Successor of 19 is {bst.successor(19)}')
    print(f'Successor of 48 is {bst.successor(48)}')
    print(f'Successor of 70 is {bst.successor(70)}')
    print()
    print()

    array = []
    bst.rangeQ(1, 19, array)
    print(f'range from  {array}')
    # nums = [2, 6, 20]
    # print("deleting " + str(nums))
    # for num in nums:
    #     bst.delete(num)
    # print("#")

    # print("4 exists:")
    # print(bst.exists(4))
    # print("2 exists:")
    # print(bst.exists(2))
    # print("12 exists:")
    # print(bst.exists(12))
    # print("18 exists:")
    # print(bst.exists(18))

if __name__ == "__main__":
    main()