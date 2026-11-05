
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each value represents a patient medical record ID.
        self.value = value

        # New nodes start without any children.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # The root is the starting point for the tree.
        # It remains None until the first record is added.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        pass

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        pass


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Medical Records Management System")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Explain how a BST reduces search space.

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty tree for patient medical record IDs.
    medical_records = BST()

    print("Medical records BST initialized.")
    print("Root node:", medical_records.root)

    # The remaining insertion requirements will be
    # completed in Push 2.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    print("Traversal will be implemented in a later push.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print("Recursive search will be implemented in Push 3.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    print("Edge case testing will be implemented in Push 4.")


if __name__ == "__main__":
    main()
