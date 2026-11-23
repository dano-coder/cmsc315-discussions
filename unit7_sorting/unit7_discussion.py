
"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.

Student: Daniel Rehner
Project: Patient Acuity Tracking for Placement Prioritization
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy of the original list
    sorted_list = lst.copy()

    # Get the number of patient acuity scores
    n = len(sorted_list)

    # Loop through the list to sort the values
    for i in range(n - 1):

        # Track whether any swaps are made
        swapped = False

        # Compare adjacent patient acuity scores
        for j in range(n - 1 - i):

            # Higher scores indicate higher placement priority
            if sorted_list[j] < sorted_list[j + 1]:

                # Swap values if they are out of order
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # Stop if no swaps were needed
        if not swapped:
            break

    # Return the sorted list
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    pass


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    pass


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")
    print("Student: Daniel Rehner")
    print("Patient Acuity and Placement Prioritization")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # Fictional patient acuity scores
    # Higher scores represent greater care needs
    acuity_scores = [45, 82, 30, 95, 67, 55, 88]

    # Display the original list
    print("Original acuity scores:", acuity_scores)

    # Sort the list using Bubble Sort
    bubble_result = bubble_sort(acuity_scores)

    # Display the sorted results
    print("Bubble Sort result:", bubble_result)

    # Compare against the expected descending order
    expected = sorted(acuity_scores, reverse=True)

    print("Expected result:  ", expected)

    if bubble_result == expected:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    # TODO: Run Merge Sort on Dataset #1 in Push 2


    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")


if __name__ == "__main__":
    main()
