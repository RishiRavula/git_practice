class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root):
    if root is None:
        return []
    return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)

if __name__ == "__main__":
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(6, TreeNode(5), TreeNode(7)))
    
    sorted_values = inOrderTraversal(root)
    print(sorted_values)  # out: [1, 2, 3, 4, 5, 6, 7]
