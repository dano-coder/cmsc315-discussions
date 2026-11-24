
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

import time
import random


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

    # Making a copy so I don't change the original scores
    sorted_list = lst.copy()

    # Checking how many scores I'm working with
    n = len(sorted_list)

    # Going through the list to get everything in order
    for i in range(n - 1):

        # Keeping track of whether anything needed to be swapped
        swapped = False

        # Looking at two scores next to each other
        for j in range(n - 1 - i):

            # Higher acuity means higher priority, so it goes first
            if sorted_list[j] < sorted_list[j + 1]:

                # Switching the scores if they're in the wrong order
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # If nothing changed, the list is already sorted
        if not swapped:
            break

    # Sending back the sorted scores
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

    # A list with one or no scores doesn't need sorting
    if len(lst) <= 1:
        return lst.copy()

    # Finding the middle so I can split the list
    middle = len(lst) // 2

    # Splitting the scores into two smaller groups
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Running merge sort again on each smaller group
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Putting the two sorted groups back together
    return merge(left_sorted, right_sorted)


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

    # Starting with an empty list for the final scores
    result = []

    # Using these to keep track of where I am in each list
    i = 0
    j = 0

    # Comparing scores until one of the lists runs out
    while i < len(left) and j < len(right):

        # Putting the higher acuity score into the new list first
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Adding anything left over from the first group
    result.extend(left[i:])

    # Adding anything left over from the second group
    result.extend(right[j:])

    # Returning the finished list
    return result


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

    # Using made-up patient acuity scores for this example
    # Higher numbers mean the patient has greater care needs
    acuity_scores = [45, 82, 30, 95, 67, 55, 88]

    # Showing the scores before doing anything to them
    print("Original acuity scores:", acuity_scores)

    # Trying both sorting methods on the same scores
    bubble_result = bubble_sort(acuity_scores)
    merge_result = merge_sort(acuity_scores)

    # Printing both results so I can compare them
    print("Bubble Sort result:", bubble_result)
    print("Merge Sort result: ", merge_result)

    # Using Python's built-in sort to check my answers
    expected = sorted(acuity_scores, reverse=True)

    print("Expected result:  ", expected)

    # Making sure both methods gave me the right order
    if bubble_result == expected and merge_result == expected:
        print("RESULT: PASS")
        print("Both algorithms correctly prioritized Dataset 1.")
    else:
        print("RESULT: FAIL")


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

    # Trying another group of patients with different scores
    acuity_scores_2 = [72, 28, 91, 64, 39, 85, 51, 96]

    # Showing the second group before sorting
    print("Original acuity scores:", acuity_scores_2)

    # Running both methods again with the new scores
    bubble_result_2 = bubble_sort(acuity_scores_2)
    merge_result_2 = merge_sort(acuity_scores_2)

    # Comparing what each method came up with
    print("Bubble Sort result:", bubble_result_2)
    print("Merge Sort result: ", merge_result_2)

    # Checking against the order Python gives me
    expected_2 = sorted(acuity_scores_2, reverse=True)

    print("Expected result:  ", expected_2)

    # Checking whether both methods match the expected result
    if bubble_result_2 == expected_2 and merge_result_2 == expected_2:
        print("RESULT: PASS")
        print("Both algorithms correctly prioritized Dataset 2.")
    else:
        print("RESULT: FAIL")


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

    # EDGE CASE 1: Empty patient list
    # This could happen when nobody is waiting for placement

    print("\n--- Edge Case 1: Empty List ---")

    empty_list = []

    bubble_empty = bubble_sort(empty_list)
    merge_empty = merge_sort(empty_list)

    print("Original list:     ", empty_list)
    print("Bubble Sort result:", bubble_empty)
    print("Merge Sort result: ", merge_empty)

    if bubble_empty == [] and merge_empty == []:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    print("Explanation: There are no scores to sort.")
    print("Both methods return an empty list without errors.")


    # EDGE CASE 2: Already sorted patient list
    # Patients are already organized by acuity

    print("\n--- Edge Case 2: Already Sorted List ---")

    sorted_scores = [95, 85, 75, 65, 55]

    bubble_sorted = bubble_sort(sorted_scores)
    merge_sorted = merge_sort(sorted_scores)

    print("Original list:     ", sorted_scores)
    print("Bubble Sort result:", bubble_sorted)
    print("Merge Sort result: ", merge_sorted)

    if bubble_sorted == sorted_scores and merge_sorted == sorted_scores:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    print("Explanation: The scores are already in order.")
    print("Bubble Sort can stop early, while Merge Sort")
    print("still divides and merges the list.")


    # EDGE CASE 3: Patients with the same acuity score
    # More than one patient could have similar care needs

    print("\n--- Edge Case 3: Duplicate Acuity Scores ---")

    duplicate_scores = [85, 60, 95, 85, 60, 95, 40]

    bubble_duplicates = bubble_sort(duplicate_scores)
    merge_duplicates = merge_sort(duplicate_scores)

    expected_duplicates = sorted(duplicate_scores, reverse=True)

    print("Original list:     ", duplicate_scores)
    print("Bubble Sort result:", bubble_duplicates)
    print("Merge Sort result: ", merge_duplicates)
    print("Expected result:  ", expected_duplicates)

    if (bubble_duplicates == expected_duplicates
            and merge_duplicates == expected_duplicates):
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    print("Explanation: Patients can have the same acuity score.")
    print("Both methods keep the duplicate values while sorting.")


    # ===============================
    # PERFORMANCE ANALYSIS
    # ===============================
    #
    # Compare the efficiency of both sorting algorithms
    # using a larger dataset.

    print("\n=== PERFORMANCE ANALYSIS ===")

    # Using a seed so I get the same random scores each time
    random.seed(7)

    # Creating a larger fictional patient dataset
    large_dataset = [
        random.randint(1, 100) for _ in range(1000)
    ]

    print("Number of patient acuity scores:", len(large_dataset))

    # Checking how long Bubble Sort takes
    start_time = time.perf_counter()

    bubble_large = bubble_sort(large_dataset)

    bubble_time = time.perf_counter() - start_time

    # Checking how long Merge Sort takes on the same data
    start_time = time.perf_counter()

    merge_large = merge_sort(large_dataset)

    merge_time = time.perf_counter() - start_time

    # Printing the times so I can compare them
    print(f"Bubble Sort time: {bubble_time:.6f} seconds")
    print(f"Merge Sort time:  {merge_time:.6f} seconds")

    # Making sure both methods still give the correct result
    expected_large = sorted(large_dataset, reverse=True)

    if bubble_large == expected_large and merge_large == expected_large:
        print("RESULT: PASS")
        print("Both algorithms correctly sorted the larger dataset.")
    else:
        print("RESULT: FAIL")

    # Comparing which method was faster during this run
    if bubble_time < merge_time:
        print("Bubble Sort was faster during this test.")

    elif merge_time < bubble_time:
        print("Merge Sort was faster during this test.")

    else:
        print("Both methods took the same measured time.")

    print("\nTime Complexity Comparison:")
    print("Bubble Sort best case: O(n)")
    print("Bubble Sort average and worst case: O(n^2)")
    print("Merge Sort best, average and worst case: O(n log n)")

    print("\nBubble Sort is easier to follow and can work well")
    print("with smaller or already sorted lists.")
    print("Merge Sort generally scales better with larger datasets.")


    # ===============================
    # REAL-WORLD SORTING EXAMPLE
    # ===============================
    #
    # Use patient acuity scores to organize patients
    # who are waiting for placement review.

    print("\n=== PATIENT PLACEMENT REVIEW ===")

    # Using fictional IDs instead of actual patient information
    patients = [
        {"id": "PT001", "acuity": 45},
        {"id": "PT002", "acuity": 82},
        {"id": "PT003", "acuity": 30},
        {"id": "PT004", "acuity": 95},
        {"id": "PT005", "acuity": 67},
        {"id": "PT006", "acuity": 55},
        {"id": "PT007", "acuity": 88}
    ]

    # Showing the patients before organizing them
    print("\nOriginal patient list:")

    for patient in patients:
        print(f"{patient['id']} | Acuity: {patient['acuity']}")

    # Pulling the acuity scores out of the patient records
    patient_scores = [
        patient["acuity"] for patient in patients
    ]

    # Using Merge Sort to organize the acuity scores
    prioritized_scores = merge_sort(patient_scores)

    # Making a copy so I can match scores back to patient IDs
    remaining_patients = patients.copy()

    prioritized_patients = []

    # Matching each sorted score to its original patient
    for score in prioritized_scores:

        for patient in remaining_patients:

            if patient["acuity"] == score:

                prioritized_patients.append(patient)

                # Removing the matched record from the working list
                # This also helps if two patients have the same score
                remaining_patients.remove(patient)

                break

    # Printing the new order for placement review
    print("\nPrioritized patient placement review list:")

    for position, patient in enumerate(prioritized_patients, start=1):

        print(
            f"Priority {position} | "
            f"Patient: {patient['id']} | "
            f"Acuity: {patient['acuity']}"
        )

    print("\nThis example shows how sorting could help organize")
    print("patients who are waiting for placement review.")
    print("Higher acuity scores appear earlier in the list.")
    print("Actual placement decisions require clinical judgment")
    print("and consideration of other patient needs.")

    print("\n=== END OF PROGRAM ===")


if __name__ == "__main__":
    main()
