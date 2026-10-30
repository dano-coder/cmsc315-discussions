
"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Add a new admission to the specified position.
    # Existing items shift right to make room for the new admission.
    # Inserting at the beginning or middle takes O(n) time.
    # Inserting at the end usually takes O(1) amortized time.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index exists before removing an admission.
    # This prevents errors and unintended deletions.
    if 0 <= index < len(lst):
        # Remove the admission and return its value.
        return lst.pop(index)

    # Return None if the index is invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Search each admission one at a time, starting at index 0.
    # This is a linear search because each item is checked in order.
    # The worst-case time complexity is O(n).
    for index, admission in enumerate(lst):
        if admission == value:
            return index

    # Return -1 when the admission is not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.


    print("\n=== INSERTION TESTS ===")

    # Start with three example hospital admissions.
    admissions = ["Admission A", "Admission B", "Admission C"]
    print("Original admissions:", admissions)

    # Add an admission at the beginning.
    # The other admissions move over one spot.
    insert_at(admissions, 0, "Admission D")
    print("After inserting at the beginning:", admissions)

    # Add an admission in the middle.
    insert_at(admissions, 2, "Admission E")
    print("After inserting in the middle:", admissions)

    # Add an admission at the end.
    insert_at(admissions, len(admissions), "Admission F")
    print("After inserting at the end:", admissions)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.


    print("\n=== DELETION TESTS ===")

    # Remove the first admission from the list.
    removed = delete_at(admissions, 0)
    print("Removed from beginning:", removed)
    print("Updated admissions:", admissions)

    # Remove an admission from the middle.
    removed = delete_at(admissions, 2)
    print("Removed from middle:", removed)
    print("Updated admissions:", admissions)

    # Remove the last admission.
    removed = delete_at(admissions, len(admissions) - 1)
    print("Removed from end:", removed)
    print("Updated admissions:", admissions)


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for an admission that is still in the list.
    found_index = search_value(admissions, "Admission E")
    print("Searching for Admission E:", found_index)

    # Search for something that isn't in the list.
    missing_index = search_value(admissions, "Admission Z")
    print("Searching for Admission Z:", missing_index)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.


    print("\n=== EDGE CASES ===")

    # Try deleting an admission at an index that doesn't exist.
    # It should return None instead of causing an error.
    removed = delete_at(admissions, 20)
    print("Deleting at invalid index:", removed)
    print("List after invalid deletion:", admissions)

    # Try adding an admission to an empty list.
    empty_admissions = []
    insert_at(empty_admissions, 0, "Admission G")
    print("After inserting into an empty list:", empty_admissions)

    # Try deleting from an empty list.
    # Since nothing is there, it should return None.
    empty_list = []
    removed = delete_at(empty_list, 0)
    print("Deleting from an empty list:", removed)



if __name__ == "__main__":
    main()
