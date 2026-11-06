
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

        # Start at the root and use recursion to find
        # the correct location for the patient ID.
        self.root = self._insert_recursive(self.root, value)

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

        # An empty position means we can create a new node.
        if node is None:
            return Node(value)

        # Smaller patient IDs belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger patient IDs belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate IDs are ignored because each patient
        # record should have a unique identifier.

        # Return the node to maintain the tree connections.
        return node

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

        # Start searching at the root of the tree.
        # A BST can avoid checking unrelated branches
        # because values are organized by size.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If we reach an empty position, the ID
        # does not exist in the tree.
        if node is None:
            return False

        # If the ID matches, the record was found.
        if value == node.value:
            return True

        # Search the left subtree for smaller IDs.
        elif value < node.value:
            return self._search_recursive(node.left, value)

        # Search the right subtree for larger IDs.
        else:
            return self._search_recursive(node.right, value)

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
    # 5. Use comments to explain why a BST is efficient
    #    at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty BST to organize patient records.
    medical_records = BST()

    print("Medical records BST initialized.")
    print("Root node:", medical_records.root)

    # Fictional patient IDs chosen to create a balanced tree.
    patient_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]

    print("\nInserting patient medical record IDs:")

    for patient_id in patient_ids:
        medical_records.insert(patient_id)
        print("Inserted patient ID:", patient_id)

    # Each comparison reduces the search to one subtree.
    # This avoids checking unrelated branches when the
    # tree is reasonably balanced.

    print("\nBST construction completed.")
    print("Root patient ID:", medical_records.root.value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Explain why traversal produces sorted output.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("Traversal will be implemented in Push 4.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two existing values.
    # 2. Search for at least two missing values.
    # 3. Explain the results.

    print("\n=== SEARCH TESTS ===")

    # Two patient IDs that exist in the tree.
    existing_ids = [1040, 1090]

    # Two patient IDs that do not exist in the tree.
    missing_ids = [1035, 1100]

    print("Searching for existing patient IDs:")

    for patient_id in existing_ids:
        result = medical_records.search(patient_id)
        print("Patient ID:", patient_id, "| Found:", result)

    print("\nSearching for missing patient IDs:")

    for patient_id in missing_ids:
        result = medical_records.search(patient_id)
        print("Patient ID:", patient_id, "| Found:", result)

    # True means the patient ID was found.
    # False means the ID was not in the tree.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    # Examples: empty tree, duplicates, or single node.

    print("\n=== EDGE CASES ===")
    print("Edge case testing will be implemented in Push 4.")


if __name__ == "__main__":
    main()
