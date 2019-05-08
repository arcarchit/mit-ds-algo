class TreeNode:
    def __init__(self, val):
        self.left, self.right = None, None
        self.parent = None
        self.val = val
        self.height = 1


class AVL_tree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        # Traverse from root to find a place to add
        if not self.root:
            self.root = TreeNode(val)
            return

        current = self.root
        while True:

            if val <= current.val:
                if current.left:
                    current = current.left
                else:
                    new_node = TreeNode(val)
                    current.left = new_node
                    new_node.parent = current
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    new_node = TreeNode(val)
                    current.right = new_node
                    new_node.parent = current
                    break
        self.rebalance(new_node)


    def height(self, node):
        return node.height if node else 0


    def update_height(self, node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        node.height = max(left_height, right_height) + 1


    def rebalance(self, node):
        while node: # TODO This loop is not needed, no need to balance till root
            self.update_height(node)
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height >= 2 + right_height:
                focus = node.left
                ll = self.height(focus.left)
                rr = self.height(focus.right)
                if ll >= rr:
                    self.rotate_right(node)
                else:
                    self.rotate_left(focus)
                    self.rotate_right(node)
            elif right_height >= 2 + left_height:
                focus = node.right
                ll = self.height(focus.left)
                rr = self.height(focus.right)
                if rr >= ll:
                    self.rotate_left(node)
                else:
                    self.rotate_right(focus)
                    self.rotate_left(node)
            node = node.parent


    def rotate_left(self, node):
        x, y, p = node, node.right, node.parent

        y.parent = p
        if not p:
            self.root = y
        else:
            if p.right == x:
                p.right = y
            elif p.left == x:
                p.left = y

        x.right = y.left
        if x.right:
            x.right.parent = x


        y.left = x
        x.parent = y


        self.update_height(y.left)
        self.update_height(y.right)


    def rotate_right(self, node):
        x, y, p = node, node.left, node.parent

        y.parent = p
        if not p:
            self.root = y
        else:
            if p.right == x:
                p.right = y
            else:
                p.left == x
                p.left = y

        x.left = y.right
        if x.left:
            x.left.parent = y

        y.right = x
        x.parent = y

        self.update_height(y.left)
        self.update_height(y.right)


    def level_order(self):
        frontier = [self.root]
        ans = []
        while frontier:
            new_frontier = []
            temp = []
            for n in frontier:
                temp.append(n.val)
                if n.left:
                    new_frontier.append(n.left)
                if n.right:
                    new_frontier.append(n.right)
            ans.append(temp)
            frontier = new_frontier
        return ans


def main():
    # bst = AVL_tree()
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(15)
    # bst.insert(2)
    # bst.insert(7)
    # bst.insert(19)
    # bst.insert(12)
    # print bst.level_order()

    bst = AVL_tree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    print bst.level_order()


    bst = AVL_tree()
    bst.insert(7)
    bst.insert(6)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    print bst.level_order()


if __name__=="__main__":
    main()