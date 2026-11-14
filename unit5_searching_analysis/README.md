
# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search using
a hospital admission tracking example. I used fictional patient
admission IDs to demonstrate how both algorithms search for
records and how their efficiency changes with larger datasets.

I chose this example because I work in healthcare and wanted
to connect the assignment to something familiar, such as
locating patient admissions and identifying assigned units.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency
- Understand how different search methods handle edge cases

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Search Algorithms

### Linear Search

Linear search checks each admission ID individually until
it finds the requested record or reaches the end of the list.

It has O(n) time complexity because it may need to check
every record. One advantage is that the admission IDs
do not need to be sorted beforehand.

### Binary Search

Binary search starts by checking the middle of a sorted list.
Depending on the value, it continues searching either the
lower or upper half.

It has O(log n) time complexity because it reduces the
remaining search area by approximately half each time.

Binary search requires the list to already be sorted.

## Testing

### Small Dataset

I created a sorted list containing five fictional
hospital admission IDs.

I tested an admission that existed and another that
was not included in the list.

Both algorithms returned the expected results.

### Large Dataset

I created a larger dataset containing 10,000 fictional
admission IDs and searched for the last record.

Results:

- Linear search index: 9999
- Binary search index: 9999
- Linear search comparisons: 10000
- Binary search comparisons: 14

This demonstrated how binary search can be more efficient
when searching a large sorted dataset.

## Edge Cases

I also tested several situations to make sure both
algorithms handled different inputs correctly.

1. Empty admission list: Both returned -1.
2. Single admission: Both returned index 0.
3. Missing admission: Both returned -1.
4. First admission: Both returned index 0.
5. Last admission: Both returned index 4.

These tests helped me understand why checking unusual
situations is important when writing programs.

## Real-World Hospital Admission Scenario

For the final example, I created fictional admission
records connected to different hospital units.

A social worker needs to locate admission ID 1015
and identify the assigned unit.

The program uses binary search to find the admission
ID in a sorted list and then retrieves the unit
from the patient records.

Expected result:

Admission ID: 1015
Assigned unit: Cardiac Unit

This is a simplified example of how searching
algorithms could help locate information in a
hospital admission tracking system.

## Discussion Board Reflection

For this assignment, I used a hospital admission tracking
example to better understand how linear search and binary
search work. I wanted to connect the algorithms to something
familiar from my experience in healthcare, where locating
patient records and identifying assigned units are common tasks.

Linear search was easier for me to understand because it checks
each admission ID individually until it finds a match. Binary
search was more challenging because I had to understand how
the middle index changes and how the search area gets smaller
with each comparison. Testing different admission IDs helped
me better understand the process.

The biggest difference I noticed was when searching through
10,000 admission IDs. Linear search required 10,000 comparisons
to locate the last record, while binary search only required 14.

I can see linear search being useful for smaller or unsorted
admission lists, while binary search would make more sense for
larger sorted datasets. Testing empty lists, missing records,
and single admissions also helped me understand why edge
cases matter.

## GitHub Development Progress

Push 1: Implemented linear search and tested a small
hospital admission dataset.

Push 2: Added binary search and compared performance
using 10,000 admission IDs.

Push 3: Completed edge case testing and added the
hospital admission lookup scenario.
