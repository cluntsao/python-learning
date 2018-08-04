from Tree import Tree
class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    def left(self, p):
        """Return a Position representing p's left child

        Return None if p does not have a left child
        """
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)

        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)