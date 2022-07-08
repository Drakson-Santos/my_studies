class BTSNode:

    def __init__(self, value=None):
        self.left_node: BTSNode = None
        self.value_node = value
        self.right_node: BTSNode = None

    def show_tree(self):
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.value_node
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left_node child.
        if self.right_node is None:
            lines, n, p, x = self.left_node.display_aux()
            s = '%s' % self.value_node
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right_node child.
        if self.left_node is None:
            lines, n, p, x = self.right_node.display_aux()
            s = '%s' % self.value_node
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left_node, n, p, x = self.left_node.display_aux()
        right_node, m, q, y = self.right_node.display_aux()
        s = '%s' % self.value_node
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_node += [n * ' '] * (q - p)
        elif q < p:
            right_node += [m * ' '] * (p - q)
        zipped_lines = zip(left_node, right_node)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def setValueNode(self, value):
        self.value_node = value

    def insert(self, value_node):

        if value_node == self.value_node:
            pass

        elif not self.value_node:
            self.setValueNode(value_node)

        elif value_node > self.value_node:
            if self.right_node:
                self.right_node.insert(value_node)
            else:
                self.right_node = BTSNode(value_node)

        else:
            if self.left_node:
                self.left_node.insert(value_node)
            else:
                self.left_node = BTSNode(value_node)

        return


bts_node = BTSNode()

bts_node.insert(3)
bts_node.insert(1)
bts_node.insert(10)
bts_node.insert(9)
bts_node.insert(20)

bts_node.show_tree()
