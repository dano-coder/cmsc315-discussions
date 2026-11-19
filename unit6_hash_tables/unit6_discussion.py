
"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.
----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Start with an empty dictionary to track hospital patients.
    # Patient IDs are our keys, and hospital units are the values.
    patients = {}

    # Add five fictional patient records.
    patients[1001] = "Emergency Department"
    patients[1002] = "Intensive Care Unit"
    patients[1003] = "Cardiac Unit"
    patients[1004] = "Medical Surgical Unit"
    patients[1005] = "Observation Unit"

    # Dictionaries use hashing to store and find keys.
    # We can look up a patient without checking every record.
    print("Current patient records:")

    for patient_id, unit in patients.items():
        print("Patient ID:", patient_id, "| Unit:", unit)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # get() finds the hospital unit connected to a patient ID.
    print("Looking up patient 1002:")
    print("Assigned unit:", patients.get(1002))

    print("Looking up patient 1004:")
    print("Assigned unit:", patients.get(1004))

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Patient 1002 is transferring to another hospital unit.
    print("Before updating patient 1002:")
    print(patients)

    # Using an existing key changes its value.
    # It doesn't create a second patient record.
    patients[1002] = "Cardiac Unit"

    print("After updating patient 1002:")
    print(patients)

    print("Patient 1002 is now in:", patients[1002])
    print("Total patient records:", len(patients))

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # Let's say patient 1005 has been discharged.
    print("Before removing patient 1005:")
    print(patients)

    # pop() removes the key and its connected value.
    # It also gives us the old value if we want to print it.
    removed_unit = patients.pop(1005)

    print("Removed patient 1005 from:", removed_unit)

    print("After removing patient 1005:")
    print(patients)

    print("Total patient records:", len(patients))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")


if __name__ == "__main__":
    main()
