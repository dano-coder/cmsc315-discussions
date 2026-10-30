# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?


## My Implementation

For this assignment, I used a hospital admissions list to practice
inserting, deleting, and searching for values in Python. I used
made-up admission labels instead of actual patient information.

### Insertion

I started with three admissions and added new ones at the beginning,
middle, and end of the list.

I learned that inserting something at the beginning or middle causes
the other items to shift over to make room. This takes O(n) time
because Python may need to move several items. Adding to the end
usually takes O(1) amortized time.

### Deletion

I tested removing admissions from the beginning, middle, and end.

When an admission is removed from the beginning or middle, the items
after it shift left to fill the empty space. Deleting from these
positions takes O(n) time, while removing the last item takes O(1)
time.

### Searching

I used a linear search to look through the admissions list.

The program checks each admission one at a time until it finds a
match. Searching for Admission E returned index 1.

I also searched for Admission Z, which wasn't in the list.
The program returned -1 because no match was found.

Linear search has a worst-case time complexity of O(n).

### Edge Cases

I also tested a few situations where the list might not behave
as expected.

I tried deleting an admission using an invalid index, which
returned None instead of causing an error.

I also inserted an admission into an empty list and tried deleting
from another empty list.

These tests helped me understand why checking indexes is important
before removing items.

### What I Learned

This assignment helped me understand how Python lists change
when items are added or removed. I also learned that the position
of an item can affect how much work Python has to do.

Using hospital admissions as an example made it easier for me
to understand how these operations could be used in a real
application.
