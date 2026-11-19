
# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

For this assignment, I used Python dictionaries to demonstrate
how hash tables store and retrieve information.

I created a basic hospital patient tracking system using
fictional patient IDs and their assigned hospital units.

Each patient ID was used as a key, and the assigned hospital
unit was stored as its value.

## Learning Objectives

During this assignment, I practiced:

- Inserting key-value pairs into a dictionary
- Looking up values using their keys
- Updating existing patient records
- Removing records from a dictionary
- Handling missing and duplicate keys
- Understanding basic hashing and collisions

## Requirements Completed

### 1. Create and Populate a Dictionary

I created an empty dictionary and added five fictional
patient records.

### 2. Lookup Operations

I used get() to look up patients 1002 and 1004.

Both lookups returned their assigned hospital units.

### 3. Update Operations

I updated patient 1002 from the Intensive Care Unit
to the Cardiac Unit.

The record changed without increasing the dictionary size.

### 4. Delete Operations

I removed patient 1005 using pop().

The dictionary decreased from five records to four.

### 5. Edge Cases

I tested four edge cases:

- Looking up a missing patient
- Trying to delete a missing patient
- Searching an empty dictionary
- Updating an existing patient ID

These tests showed how to handle missing records safely
and avoid accidentally creating duplicate patient IDs.

### 6. Real-World Scenario

I used a hospital patient tracking system as my example.

A hospital might need to look up a patient's assigned unit,
update their location after a transfer, or remove a record
from an active tracking list after discharge.

Using a dictionary allowed these operations to be performed
using patient IDs instead of manually searching through
every record.

## Hash Collisions

I also demonstrated a simplified hash collision using
five possible buckets.

Patient IDs 1001 and 1006 both mapped to bucket 1
using the calculation ID % 5.

I learned that a collision happens when different keys
map to the same location in a hash table.

Separate chaining and open addressing are two common
ways to handle collisions.

Python dictionaries handle collisions internally.
While dictionary lookups are usually O(1) on average,
excessive collisions can reduce lookup efficiency.

## Program Results

The program successfully demonstrated inserting,
looking up, updating, and deleting patient records.

It also handled missing keys and duplicate IDs
without crashing.

## Discussion Board Reflection

I learned how Python dictionaries use keys and values
to organize information and why hash tables are useful
for applications that need quick lookups.

The main challenge was understanding how missing keys
and collisions affect the way a dictionary works.

Testing edge cases helped me understand how to make
the program more reliable.
