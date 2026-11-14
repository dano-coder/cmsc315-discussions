
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
    # Linear search is O(n) because we may need
    # to check every ID before finding a match.
    for index in range(len(lst)):

        if lst[index] == target:
            return index

    # No matching admission was found.
    return -1


def binary_search(lst, target):
    """
    Search a sorted list for an admission ID.

    Binary search starts in the middle and
    reduces the search area with each comparison.
    """

    # Start at both ends of the sorted list.
    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find the middle admission ID.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            # The ID must be in the upper half.
            # We can ignore everything below middle.
            left = middle + 1

        else:
            # The ID must be in the lower half.
            # We can ignore everything above middle.
            right = middle - 1

    # Return -1 if the admission is missing.
    return -1

    # Binary search is O(log n) because each
    # comparison cuts the remaining list in half.


def count_linear_comparisons(lst, target):
    """
    Count how many admission IDs linear search checks.
    """

    comparisons = 0

    for value in lst:
        comparisons += 1

        if value == target:
            return comparisons

    return comparisons


def count_binary_comparisons(lst, target):
    """
    Count how many admission IDs binary search checks.
    """

    comparisons = 0
    left = 0
    right = len(lst) - 1

    while left <= right:

        middle = (left + right) // 2
        comparisons += 1

        if lst[middle] == target:
            return comparisons

        elif lst[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return comparisons


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Hospital Admission Tracking")

    # ===============================
    # SMALL DATASET
    # ===============================

    # A small sorted list of fictional admission IDs.
    admissions = [1001, 1005, 1010, 1015, 1020]

    print("\n=== SMALL DATASET TEST ===")
    print("Admission IDs:", admissions)

    # Search for an admission that exists.
    target = 1015

    print("\nSearching for admission:", target)

    print("Linear search index:",
          linear_search(admissions, target))

    print("Binary search index:",
          binary_search(admissions, target))

    # Both methods should return index 3.

    # Search for an admission that does not exist.
    target = 1099

    print("\nSearching for admission:", target)

    print("Linear search index:",
          linear_search(admissions, target))

    print("Binary search index:",
          binary_search(admissions, target))

    # Both methods should return -1.

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create 10,000 fictional hospital admission IDs.
    large_admissions = list(range(10001, 20001))

    # Search for the last admission ID.
    target = 20000

    print("Total admissions:", len(large_admissions))
    print("Searching for admission:", target)

    print("\nLinear search index:",
          linear_search(large_admissions, target))

    print("Binary search index:",
          binary_search(large_admissions, target))

    # Count how many comparisons each algorithm makes.
    linear_checks = count_linear_comparisons(
        large_admissions, target
    )

    binary_checks = count_binary_comparisons(
        large_admissions, target
    )

    print("\nLinear search comparisons:", linear_checks)
    print("Binary search comparisons:", binary_checks)

    # Linear search checks all 10,000 IDs because
    # the admission we want is at the end.

    # Binary search only needs 14 comparisons.
    # It keeps removing half of the remaining IDs.

    # This is why binary search is more efficient
    # when working with large sorted datasets.

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
