
class BinaryTree:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def visit(val, res):
        res.append(val)

    def preorder_traversal(self):
        def preorder(root1):
            if root1 is not None:
                self.visit(root1.val, res)
                preorder(root1.left)
                preorder(root1.right)
        res = []
        preorder(self)
        return res

    @staticmethod
    def preorder_create_binary_tree(root, nodes):
        def create_tree(root1):
            if nodes[0]:
                root1 = BinaryTree(nodes[0])
                nodes.pop(0)
                root1.left = create_tree(root1.left)
                root1.right = create_tree(root1.right)
                return root1
            else:
                root1 = None
                nodes.pop(0)
            pass
        return create_tree(root)


if __name__ == '__main__':
    data_input2 = [2, 3, 4, 0, 5, 0, 0, 0, 6, 7, 0, 0, 8, 0, 0]  # 创建二叉树需要的数据当data=0的时候就递归停止
    Root = BinaryTree()
    Root = Root.preorder_create_binary_tree(None, data_input2)
    print(Root.preorder_traversal())
