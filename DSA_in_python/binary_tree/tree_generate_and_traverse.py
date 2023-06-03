class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def insert(self, child):
        child.parent = self
        self.children.append(child)
    
    def insert_multiple(self, *child):
        for element in child:
            self.insert(element)
    
    def traverse_in_order(self):
        if self.children:
            for child in self.children:
                child.traverse_in_order()
        print(self.data)

    def traverse_pre_order(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.traverse_pre_order()

    def traverse_post_order(self):
        if self.children:
            for child in self.children:
                child.traverse_post_order()
        print(self.data)

def build_tree():
    root = TreeNode("Data Structure")
    
    dynamic_ds = TreeNode("Dynamic Data Structure")
    dynamic_ds.insert_multiple(TreeNode("Queue"), TreeNode("Stack"), TreeNode("Linked List"))
    
    static_ds = TreeNode("Static Data Structure")
    static_ds.insert(TreeNode("Array"))

    linear_ds = TreeNode("Linear Data Structure")
    linear_ds.insert_multiple(static_ds, dynamic_ds)

    non_linear_ds = TreeNode("Non-Linear Data Structure")
    non_linear_ds.insert_multiple(TreeNode("Tree"), TreeNode("Graph"))

    root.insert(linear_ds)
    root.insert(non_linear_ds)

    print("In-Order Traversal:")
    root.traverse_in_order()

    print("\nPre-Order Traversal:")
    root.traverse_pre_order()

    print("\nPost-Order Traversal:")
    root.traverse_post_order()

    root.print_tree()


build_tree()