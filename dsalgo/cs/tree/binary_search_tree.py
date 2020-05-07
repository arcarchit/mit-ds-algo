class Tree:
    def __init__(self, val):
        self.left, self.right, self.val = None, None, val


class BST:

    def __init__(self):
        self.tree = None

    def insert(self, a):
        if not self.tree:
            self.tree = Tree(a)
            return
        parent = self.tree
        while True:
            if a <= parent.val:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = Tree(a)
                    break
            else:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = Tree(a)
                    break

    def search(self, a):
        parent = self.tree
        while parent:
            if a == parent.val:
                return True
            elif a < parent.val:
                parent = parent.left
            else:
                parent = parent.right
        return False

    def print_tree(self):
        ans = []
        frontier = [self.tree]
        while frontier:
            new_frontier = []
            for n in frontier:
                ans.append(n.val)
                if n.left:
                    new_frontier.append(n.left)
                if n.right:
                    new_frontier.append(n.right)
            frontier = new_frontier
        print ans

    def in_order(self):
        ans = []
        stack = []

        current = self.tree

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                popped = stack.pop()
                ans.append(popped.val)
                current = popped.right

        return ans

    def pre_order(self):
        ans = []
        current = self.tree
        stack = [current]
        while stack:
            popped = stack.pop()
            ans.append(popped.val)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)
        return ans


    def post_order(self):
        ans_stack = []
        stack = [self.tree]

        while stack:
            popped = stack.pop()
            ans_stack.append(popped.val)
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)

        return list(reversed(ans_stack))


    def delete_node(self, node):
        # Get node to replace it and parent of replacement
        parent = node
        replacement = node.right
        while replacement.left:
            parent = replacement
            replacement = replacement.left
        node.val = replacement.val

        if parent == node:
            parent.right = None
        else:
            parent.left = None


    def delete_val(self, a):
        parent = self.tree
        found = None
        while parent:
            if a == parent.val:
                found = parent
                break
            elif a < parent.val:
                parent = parent.left
            else:
                parent = parent.right
        if not found:
            raise ("Node not found")

        if not found.left and not found.right:
            found = None
        elif not found.left:
            temp = found.right
            found = temp
            temp = None
        elif not found.right:
            temp = found.left
            found = temp
            temp = None
        else:
            minn = self.delete_node(found)


    def find_greater(self, k):

        def sub_sol(node):
            if not node:return None

            if k < node.val:
                child = sub_sol(node.left)
                return child if child else node
            else:
                child = sub_sol(node.right)
                return child
        ans = sub_sol(self.tree)
        return ans.val

    def find_smaller(self, k):

        def sub_sol(node):
            if not node : return None

            if k > node.val:
                child = sub_sol(node.right)
                return child if child else node
            else:
                child = sub_sol(node.left)
                return child

        ans = sub_sol(self.tree)
        return ans.val





def main():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(19)
    bst.insert(12)
    bst.print_tree()

    print ("\nSuccessor/Predecessor\n")

    print bst.find_greater(4), bst.find_greater(6), bst.find_greater(8), bst.find_greater(10), \
        bst.find_greater(11), bst.find_greater(15)

    print bst.find_smaller(4), bst.find_smaller(6), bst.find_smaller(8), bst.find_smaller(10), \
        bst.find_smaller(11), bst.find_smaller(15)


    print bst.search(4)
    print bst.search(5)
    print bst.search(6)
    print bst.search(7)
    print bst.in_order()
    print bst.pre_order()
    print bst.post_order()
    print "==="
    bst.delete_val(5)
    print "**"
    print bst.print_tree()
    bst.delete_val(10)
    print "**"
    print bst.print_tree()





#         10
#
#     5        15
#
#   2   7   12  19
#
#

if __name__=="__main__":
    main()