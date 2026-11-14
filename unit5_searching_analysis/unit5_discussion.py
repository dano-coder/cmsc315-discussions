
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Search the list from beginning to end.
    Return the index if the target is found.
    Return -1 if the target is not found.
    """

    # Check each hospital admission ID one at a time.
    for index in range(len(lst)):

        if lst[index] == target:
            return index

    # No matching admission was found.
    return -1

    # Linear search has O(n) time complexity because
    # it may need to check every item in the list.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    pass


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Hospital Admission Tracking")

    # ===============================
    # SMALL DATASET
    # ===============================

    # Create a small sorted list of admission IDs.
    admissions = [1001, 1005, 1010, 1015, 1020]

    print("\n=== SMALL DATASET TEST ===")
    print("Admission IDs:", admissions)

    # Search for an admission that exists.
    target = 1015
    result = linear_search(admissions, target)

    print("\nSearching for admission:", target)
    print("Linear search index:", result)

    # The admission should be found at index 3.
    if result != -1:
        print("Admission found.")
    else:
        print("Admission not found.")

    # Search for an admission that does not exist.
    target = 1099
    result = linear_search(admissions, target)

    print("\nSearching for admission:", target)
    print("Linear search index:", result)

    # The result should be -1.
    if result == -1:
        print("Admission not found, as expected.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes
    #    more efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")


if __name__ == "__main__":
    main()
