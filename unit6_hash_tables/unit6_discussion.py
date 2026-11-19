
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

    # Use a dictionary to track fictional hospital patients.
    # Patient IDs are keys, and hospital units are values.
    patients = {}

    # Add five patient records.
    patients[1001] = "Emergency Department"
    patients[1002] = "Intensive Care Unit"
    patients[1003] = "Cardiac Unit"
    patients[1004] = "Medical Surgical Unit"
    patients[1005] = "Observation Unit"

    # Python dictionaries use hashing behind the scenes.
    # This lets us find records pretty quickly using their keys.
    print("Current patient records:")

    for patient_id, unit in patients.items():
        print("Patient ID:", patient_id, "| Unit:", unit)

    print("Total patient records:", len(patients))

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # get() lets us find a patient using their ID.
    # We don't have to search through every patient manually.
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

    # Patient 1002 is moving to another hospital unit.
    print("Before updating patient 1002:")
    print(patients)

    # Using the same key updates the value.
    # It doesn't create another patient with the same ID.
    patients[1002] = "Cardiac Unit"

    print("After updating patient 1002:")
    print(patients)

    print("Updated unit:", patients[1002])
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

    # Patient 1005 has been discharged.
    print("Before removing patient 1005:")
    print(patients)

    # pop() removes the patient and returns their old unit.
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

    # Edge case 1: Look up a patient who isn't in our system.
    # get() lets us provide a message instead of getting an error.
    print("\nEdge case 1: Missing patient lookup")
    missing_patient = patients.get(9999, "Patient not found")
    print("Patient 9999:", missing_patient)

    # Edge case 2: Try removing a patient who doesn't exist.
    # Using pop() with a default value avoids a KeyError.
    print("\nEdge case 2: Remove missing patient")
    removed = patients.pop(9999, None)

    if removed is None:
        print("Patient 9999 wasn't found, so nothing was removed.")

    print("Total patient records:", len(patients))

    # Edge case 3: Try looking up a patient in an empty dictionary.
    print("\nEdge case 3: Empty dictionary")
    empty_patients = {}

    print("Empty patient records:", empty_patients)
    print("Looking up patient 1001:",
          empty_patients.get(1001, "Patient not found"))

    # Edge case 4: Try adding a patient ID that already exists.
    # The old value gets replaced instead of making a duplicate.
    print("\nEdge case 4: Duplicate patient ID")

    print("Patient 1003 before:", patients[1003])
    records_before = len(patients)

    patients[1003] = "Neurology Unit"

    print("Patient 1003 after:", patients[1003])
    print("Records before:", records_before)
    print("Records after:", len(patients))
    print("Same ID updated instead of adding another record.")

    # ===============================
    # COLLISION DEMONSTRATION
    # ===============================

    print("\n=== HASH COLLISION DEMONSTRATION ===")

    # A simple example using 5 possible buckets.
    # This isn't Python's actual dictionary hash function.
    # It just helps us see how collisions can happen.
    bucket_count = 5

    patient_a = 1001
    patient_b = 1006

    bucket_a = patient_a % bucket_count
    bucket_b = patient_b % bucket_count

    print("Patient", patient_a, "maps to bucket", bucket_a)
    print("Patient", patient_b, "maps to bucket", bucket_b)

    if bucket_a == bucket_b:
        print("Collision: Both IDs mapped to the same bucket.")

    # A real hash table needs a way to deal with collisions.
    # Separate chaining can keep multiple entries in one bucket.
    # Open addressing looks for another available location.
    #
    # Python dictionaries handle collisions internally.
    # Too many collisions can make lookups slower because
    # the table has more work to do to find the correct key.

    print("Separate chaining stores multiple entries in a bucket.")
    print("Open addressing searches for another available slot.")
    print("Python handles dictionary collisions automatically.")

    # ===============================
    # FINAL SUMMARY
    # ===============================

    print("\n=== FINAL SUMMARY ===")

    print("Final patient records:")
    for patient_id, unit in patients.items():
        print("Patient ID:", patient_id, "| Unit:", unit)

    print("Total records:", len(patients))
    print("All dictionary operations completed.")


if __name__ == "__main__":
    main()
