import sys

sys.setrecursionlimit(2000)


class Node:
    def __init__(self, node_data):
        self.data = node_data[0] + 1
        self.x = node_data[1][0]
        self.y = node_data[1][1]
        self.right = self.left = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, Node):
        if not self.root:
            self.root = Node
        else:
            parent = self.root
            self._insert_node(Node, parent)

    def _insert_node(self, Node, parent):
        if parent.x <= Node.x and not parent.right:
            parent.right = Node

        elif parent.x <= Node.x and parent.right:
            parent = parent.right
            self._insert_node(Node, parent)

        elif Node.x < parent.x and not parent.left:
            parent.left = Node

        elif Node.x < parent.x and parent.left:
            parent = parent.left
            self._insert_node(Node, parent)

    def pre_order_traversal(self):
        order = []

        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                order.append(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)

        return order

    def post_order_traversal(self):
        order = []

        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                order.append(root.data)

        _post_order_traversal(self.root)

        return order


def solution(nodeinfo):
    node_info_data = sorted(enumerate(nodeinfo), key=lambda x: x[1][1], reverse=True)
    tree = BinaryTree()
    for node_data in node_info_data:
        tree.insert(Node(node_data))
    answer = [tree.pre_order_traversal(),
              tree.post_order_traversal()]
    return answer


if __name__ == "__main__":
    print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
