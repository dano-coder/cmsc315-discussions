
# CMSC 315 - Unit 7 Discussion

Student: Daniel Rehner
Project: Patient Acuity and Placement Prioritization

## Overview

For this assignment, I implemented Bubble Sort and Merge Sort
using fictional patient acuity scores. I wanted to continue
using healthcare examples to better understand how sorting
algorithms could be applied in a professional setting.

The program sorts patient acuity scores from highest to lowest
to help organize patients awaiting placement review.

## Sorting Algorithms

- Bubble Sort: Compares neighboring values and swaps them
  when they are out of order.
- Merge Sort: Uses recursion to divide a list into smaller
  groups before sorting and merging them together.

## Testing

I tested both algorithms using two different patient acuity
datasets and three edge cases:

- Empty list
- Already sorted list
- Duplicate values

I compared the results against Python's built-in sorting
function to check for accuracy.

## Performance

I generated 1,000 random acuity scores to compare the
execution times of both algorithms.

Bubble Sort has a best case time complexity of O(n) and
an average and worst case time complexity of O(n^2).

Merge Sort has a time complexity of O(n log n) across
its best, average, and worst cases.

Bubble Sort is easier to implement and may be useful for
smaller datasets. Merge Sort is generally more efficient
when working with larger amounts of data.

## Development Process

- Push 1: Implemented Bubble Sort and the first dataset.
- Push 2: Implemented Merge Sort and the second dataset.
- Push 3: Added edge cases, performance testing, a patient
  placement example, and documentation.

## Real-World Application

Sorting algorithms could be useful in healthcare when
organizing patients based on acuity and care needs.

All patient information and scores used in this assignment
are fictional and intended for educational purposes.

## Running the Program

Requires Python 3. No additional packages are needed.

    python unit7_sorting_algorithms.py

## Conclusion

This assignment helped me better understand sorting,
recursion, and algorithm efficiency. It also helped me
visualize how these concepts could be applied to patient
tracking and placement coordination in healthcare.
