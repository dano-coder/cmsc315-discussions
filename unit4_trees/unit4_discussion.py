
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
        # TODO (Student): Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value  # Fictional patient medical record ID
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student): Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST using the recursive helper.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Create a node when empty, insert smaller values left,
        larger values right, and return the updated node reference.
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Equal IDs are ignored to keep patient record IDs unique.
        return node

    def search(self, value):
        """
        TODO (Student):
        Return True if found and False otherwise.
        BST searching can skip unrelated subtrees instead
        of checking every ID.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return values from an in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Visit left subtree, current node, then right subtree.
        This produces ascending values because smaller IDs
        are on the left.
        """
        if node is None:
            return

        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Medical Records Management System")

    # TODO (Student): BUILD A TREE
    # Create a BST, insert at least 7 IDs on both sides,
    # and display them.

    print("\n=== TREE CONSTRUCTION ===")

    medical_records = BST()
    print("Medical records BST initialized.")
    print("Root node:", medical_records.root)

    patient_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]

    print("\nInserting patient medical record IDs:")

    for patient_id in patient_ids:
        medical_records.insert(patient_id)
        print("Inserted patient ID:", patient_id)

    print("\nBST construction completed.")
    print("Root patient ID:", medical_records.root.value)

    # TODO (Student): IN-ORDER TRAVERSAL
    # Display sorted output and explain why
    # the left-node-right order sorts it.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("Patient IDs in ascending order:", medical_records.inorder())

    # TODO (Student): SEARCH TESTS
    # Test at least two existing IDs and two missing IDs.

    print("\n=== SEARCH TESTS ===")

    print("Searching for existing patient IDs:")

    for patient_id in [1040, 1090]:
        print("Patient ID:", patient_id,
              "| Found:", medical_records.search(patient_id))

    print("\nSearching for missing patient IDs:")

    for patient_id in [1035, 1100]:
        print("Patient ID:", patient_id,
              "| Found:", medical_records.search(patient_id))

    # TODO (Student): EDGE CASES
    # Demonstrate an empty tree, duplicate IDs,
    # and a single-node tree.

    print("\n=== EDGE CASES ===")

    empty_records = BST()
    print("Empty tree traversal:", empty_records.inorder())
    print("Search 1050 in empty tree:", empty_records.search(1050))

    medical_records.insert(1040)
    print("After inserting duplicate 1040:", medical_records.inorder())
    print("Number of records after duplicate:",
          len(medical_records.inorder()))

    single_record = BST()
    single_record.insert(2000)

    print("Single-node tree traversal:", single_record.inorder())
    print("Search 2000 in single-node tree:",
          single_record.search(2000))
    print("Search 2001 in single-node tree:",
          single_record.search(2001))

    print("\nFinal BST testing completed.")


if __name__ == "__main__":
    main()
