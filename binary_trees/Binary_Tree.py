from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return 0 if not node else max(self.height(node.left), self.height(node.right) + 1)

    def isBalanced(self, node):
        if not node:
            return 0
        left_subtree = self.isBalanced(node.left)
        right_subtree = self.isBalanced(node.right)
        if left_subtree == -1 or right_subtree == -1 or abs(left_subtree - right_subtree) > 1:
            return -1
        return max(left_subtree, right_subtree) + 1

    def height_iter(self):
        if not self.root:
            return 0
        q = deque()
        h = 0
        q.append(self.root)
        while q:
            n = len(q)
            h += 1
            for i in range(n):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return h

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        q = deque()
        q.append(self.root)
        while q:
            curr = q.popleft()
            if not curr.left:
                curr.left = Node(value)
                return
            else:
                q.append(curr.left)
            if not curr.right:
                curr.right = Node(value)
                return
            else:
                q.append(curr.right)

    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def preorder_iter(self):
        if not self.root:
            return
        curr = self.root
        st = []
        while st or curr:
            if curr:
                print(curr.val)
                if curr.right:
                    st.append(curr.right)
                curr = curr.left
            else:
                curr = st.pop()

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def level_order(self):
        if not self.root:
            return
        q = deque()
        q.append(self.root)
        levels = []
        while q:
            level = []
            n = len(q)
            for i in range(n):
                elem = q.popleft()
                level.append(elem.val)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            levels.append(level)
        return levels

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)

    def postorder_two_stacks(self):
        if not self.root:
            return
        st_1 = []
        st_2 = []
        curr = self.root
        st_1.append(curr)
        while st_1:
            curr = st_1.pop()
            st_2.append(curr)
            if curr.left:
                st_1.append(curr.left)
            if curr.right:
                st_1.append(curr.right)
        while st_2:
            print(st_2.pop().val)

    def postorder_iter(self):
        if not self.root:
            return
        curr = self.root
        st = []
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right
                if temp is None:
                    temp = st.pop()
                    print(temp.val)
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        print(temp.val)
                else:
                    curr = temp


bin_tree = BinaryTree()
nodes = [1, 2, 3, 4, 5, 7, 8]
for node in nodes:
    bin_tree.insert(node)
# bin_tree.preorder(bin_tree.root)
# bin_tree.preorder_iter()
# bin_tree.inorder(bin_tree.root)
# print(bin_tree.level_order())
# print(bin_tree.postorder_two_stacks())
# print(bin_tree.postorder_iter())
print(bin_tree.height(bin_tree.root))
# print(bin_tree.height_iter())
