
# Unit 4 Discussion: Binary Search Trees

## Project Overview

For this assignment, I chose to create a medical records management system using a Binary Search Tree (BST). The purpose of this project was to demonstrate how patient medical record IDs could be organized and searched efficiently using a tree structure.

I continued using a healthcare example from my previous programming assignments to demonstrate how data structures could be applied in a real-world setting.

## Push 1: Initial BST Structure

For the first part of this project, I established the basic structure of the Binary Search Tree.

I created a Node class that stored a numerical patient record ID. Each node also contained references to its left and right children. These references were initially set to None because new nodes did not have any children.

I also created a BST class that initialized the root as None. This represented an empty tree before any patient records were inserted.

### Implementation

The Node class contained three attributes:

1. value: Stored the patient's numerical record ID.
2. left: Referenced the left child node.
3. right: Referenced the right child node.

The BST class contained a root attribute that identified the starting point of the tree.

I retained the original TODO prompts for recursive insertion, searching, and in-order traversal. These operations were reserved for later stages of development.

### Testing and Results

I ran the Python program through the IntelliJ terminal and confirmed that the initial BST was created successfully.

The program displayed the following output:

    === UNIT 4: BINARY SEARCH TREES ===
    Medical Records Management System

    === TREE CONSTRUCTION ===
    Medical records BST initialized.
    Root node: None

The root displayed None because no patient records had been inserted yet. This was the expected result for an empty Binary Search Tree.

### Reflection

During this initial stage, I learned how a Binary Search Tree was structured using individual nodes and references to child nodes. I also learned that the root served as the starting point for accessing the tree.

One important concept was understanding how nodes would eventually be organized based on their numerical values. Smaller patient record IDs would be placed in the left subtree, while larger IDs would be placed in the right subtree.

This organization could improve searching compared to checking every record individually, provided the tree remained reasonably balanced.

The initial implementation established the foundation for adding recursive insertion, searching, traversal, and edge case testing in later stages.

## Push 2: Recursive BST Insertion

For the second part of this project, I implemented recursive insertion to organize patient medical record IDs within the Binary Search Tree.

I updated the insert() method to use the _insert_recursive() helper method. This allowed the program to compare each patient ID with the current node and determine where the new record belonged.

If the patient ID was smaller than the current node, the program moved to the left subtree. If the ID was larger, it moved to the right subtree. Once an empty position was found, a new node was created.

I also included a condition to ignore duplicate patient IDs since each medical record should have a unique identifier.

### Patient Records

I inserted the following seven fictional patient record IDs:

1050, 1025, 1075, 1010, 1040, 1060, 1090

I selected these values to demonstrate how insertion order could create a balanced Binary Search Tree.

The root node was 1050, with smaller patient IDs organized on the left and larger IDs organized on the right.

The resulting tree had a height of 2.

### Implementation

The insert() method started the insertion process at the root of the tree.

The _insert_recursive() method compared the new patient ID with the current node and recursively moved left or right until an empty position was found.

The method then returned the updated node reference to maintain the connections between nodes.

This approach followed the recursive insertion process discussed in Section 6.9 of the zyBooks material.

### Testing and Results

I ran the updated Python program through the IntelliJ terminal and confirmed that all seven patient IDs were inserted successfully.

The program displayed the following output:

    Inserting patient medical record IDs:
    Inserted patient ID: 1050
    Inserted patient ID: 1025
    Inserted patient ID: 1075
    Inserted patient ID: 1010
    Inserted patient ID: 1040
    Inserted patient ID: 1060
    Inserted patient ID: 1090

    BST construction completed.
    Root patient ID: 1050

The program completed without errors, and the root remained 1050 after all records were inserted.

### Reflection

This part of the assignment helped me better understand how recursion worked when inserting values into a Binary Search Tree.

One concept I found useful was how the program could organize patient records by comparing numerical IDs rather than manually determining where each record should go.

I also learned that insertion order affected the overall structure of the tree. By starting with a middle value, I was able to create a balanced tree that could support more efficient searching.

However, inserting patient IDs in sequential order could create an unbalanced tree that behaved more like a linked list. This would reduce the performance benefits of using a BST.

## Remaining Development

The following functionality was planned for the remaining stages of the assignment:

Push 3: Implement recursive searching to locate existing and missing patient record IDs.

Push 4: Implement in-order traversal and demonstrate edge cases, including empty trees and duplicate patient IDs.

Push 5: Complete the medical records demonstration, perform final testing, and update the project documentation and discussion reflection.
