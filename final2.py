class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_val = self._get_min(node.right)
            node.key = min_val
            node.right = self._delete(node.right, min_val)
        
        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def print_bst(self):
        self._print_bst(self.root)

    def _print_bst(self, node):
        if node is not None:
            self._print_bst(node.left)
            print(node.key, end=' ')
            self._print_bst(node.right)


# Example usage:

# Create a BST
bst = BST()

# Insert data
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Print BST
print("BST contents:")
bst.print_bst()

# Delete data
bst.delete(30)

# Print BST after deletion
print("\nBST contents after deletion:")
bst.print_bst()
