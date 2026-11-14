
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

Example: Hospital admission and patient tracking.
All admission IDs are fictional.
"""


def linear_search(lst, target):
    """
    Search the list from beginning to end.
    Return the index if the target is found.
    Return -1 if the target is not found.
    """

    # Check each hospital admission ID one at a time.
    # Linear search is O(n) because we might need
    # to check every ID before finding a match.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # No matching admission was found.
    return -1


def binary_search(lst, target):
    """
    Search a sorted list by checking the middle value.
    Return the index if found, or -1 if missing.
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
            # Ignore the lower half of the list.
            left = middle + 1

        else:
            # Ignore the upper half of the list.
            right = middle - 1

    # Binary search is O(log n) because it cuts
    # the remaining search area in half each time.
    return -1


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
    Count how many middle values binary search checks.
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


def show_results(admissions, target):
    """
    Compare both search algorithms on the same list.
    The admission IDs must be sorted for binary search.
    """

    print("\nSearching for admission:", target)

    linear_result = linear_search(admissions, target)
    binary_result = binary_search(admissions, target)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Check that both algorithms agree.
    if linear_result == binary_result:
        print("Both searches returned the same result.")
    else:
        print("Search results did not match.")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Hospital Admission Tracking")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # A small sorted list of fictional admission IDs.
    small_admissions = [1001, 1005, 1010, 1015, 1020]

    print("Admission IDs:", small_admissions)

    # Search for an admission that exists.
    show_results(small_admissions, 1015)

    # Search for an admission that is missing.
    show_results(small_admissions, 1099)

    # Both methods should find 1015 at index 3.
    # Both should return -1 for missing ID 1099.

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create 10,000 sorted admission IDs.
    large_admissions = list(range(10001, 20001))

    # Search for the last admission ID.
    target = 20000

    print("Total admissions:", len(large_admissions))

    show_results(large_admissions, target)

    # Compare how many IDs each algorithm checks.
    linear_checks = count_linear_comparisons(
        large_admissions, target
    )

    binary_checks = count_binary_comparisons(
        large_admissions, target
    )

    print("\nLinear search comparisons:", linear_checks)
    print("Binary search comparisons:", binary_checks)

    # Linear search checks all 10,000 admission IDs.
    # Binary search only needs 14 comparisons.
    # This shows why binary search is more efficient
    # when working with large sorted datasets.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty admission list.
    print("\nEdge Case 1: Empty admission list")

    empty_admissions = []
    show_results(empty_admissions, 1001)

    # Both methods return -1 because the list is empty.

    # Edge case 2: Only one admission in the list.
    print("\nEdge Case 2: Single admission")

    one_admission = [1001]
    show_results(one_admission, 1001)

    # Both methods return index 0.

    # Edge case 3: Admission is missing.
    print("\nEdge Case 3: Missing admission")

    show_results(small_admissions, 9999)

    # Both methods return -1.

    # Edge case 4: First admission in the list.
    print("\nEdge Case 4: First admission")

    show_results(small_admissions, 1001)

    # Both methods return index 0.

    # Edge case 5: Last admission in the list.
    print("\nEdge Case 5: Last admission")

    show_results(small_admissions, 1020)

    # Both methods return index 4.

    # ===============================
    # REAL-WORLD HOSPITAL EXAMPLE
    # ===============================

    print("\n=== HOSPITAL ADMISSION LOOKUP ===")

    # Fictional admission records and assigned units.
    patient_records = {
        1001: "Emergency Department",
        1005: "Medical Surgical Unit",
        1010: "Intensive Care Unit",
        1015: "Cardiac Unit",
        1020: "Observation Unit"
    }

    # Sort the IDs before using binary search.
    admission_ids = sorted(patient_records.keys())

    # A social worker needs to locate an admission.
    target = 1015

    print("Looking up admission ID:", target)

    result = binary_search(admission_ids, target)

    if result != -1:
        admission_id = admission_ids[result]

        print("Admission found.")
        print("Admission ID:", admission_id)
        print("Assigned unit:", patient_records[admission_id])

    else:
        print("Admission not found.")

    # In a hospital, staff often need to locate
    # admission records and assigned units quickly.

    # Linear search could work for a small list
    # of recent admissions that is not sorted.

    # Binary search is useful when working with
    # thousands of sorted admission IDs.

    # Sorting also takes time, so binary search
    # makes more sense when records are already
    # sorted or will be searched repeatedly.

    # ===============================
    # FINAL COMPARISON
    # ===============================

    print("\n=== FINAL COMPARISON ===")

    print("Linear search: O(n)")
    print("Binary search: O(log n)")

    print("\nLinear search checks IDs one at a time.")
    print("Binary search repeatedly cuts the search area in half.")

    print("\nAll search tests completed.")


if __name__ == "__main__":
    main()
