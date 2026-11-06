
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



## Push 3: Recursive BST Searching

For the third part of this project, I implemented recursive searching to locate patient medical record IDs within the Binary Search Tree.

I updated the search() method to call the _search_recursive() helper method. The search started at the root and compared the requested patient ID with the current node.

If the patient ID matched the current node, the method returned True. If the ID was smaller, the program searched the left subtree. If the ID was larger, it searched the right subtree.

When the search reached an empty position, the method returned False because the patient ID was not found.



### Implementation

I used recursion to move through the BST without checking every patient record.

The search algorithm followed the ordering rules established during insertion. This allowed the program to eliminate unrelated branches from consideration.

For example, searching for patient ID 1040 followed the path from 1050 to 1025 and then to 1040.

### Testing and Results

I tested the search method using two patient IDs that existed in the tree and two that did not exist.

The program produced the following results:

    === SEARCH TESTS ===
    Searching for existing patient IDs:
    Patient ID: 1040 | Found: True
    Patient ID: 1090 | Found: True

    Searching for missing patient IDs:
    Patient ID: 1035 | Found: False
    Patient ID: 1100 | Found: False

The tests demonstrated how the program identified existing patient records and handled missing records without errors.

### Reflection

This stage helped me understand how recursive searching could improve efficiency when working with organized data.

Compared to a linear search, which might require checking every record, a balanced BST could reduce the number of comparisons needed to locate a patient ID.

I also learned that the efficiency depended on the tree's shape. A balanced BST generally supported searching in O(log N) time, while a highly unbalanced BST could require O(N) time.

This demonstrated why insertion order was important when building a Binary Search Tree.


## Push 4: Inorder Traversal and Final Testing

For the fourth and final part of this project, I completed the Binary Search Tree by implementing recursive inorder traversal and testing several edge cases.

I continued using the medical records management system to demonstrate how patient record IDs could be organized, searched, and displayed using a BST.


### Implementation

I updated the inorder() method to create an empty list and call the _inorder_recursive() helper method.

The recursive method visited the left subtree first, added the current node's value to the list, and then visited the right subtree.

Because smaller patient IDs were stored on the left and larger IDs were stored on the right, this process returned the patient records in ascending numerical order.

I also retained the recursive insertion and searching methods from the previous development stages.

### Inorder Traversal Results

I tested the completed traversal method using the seven fictional patient record IDs inserted during Push 2.

The program produced the following output:

    === IN-ORDER TRAVERSAL ===
    Patient IDs in ascending order: [1010, 1025, 1040, 1050, 1060, 1075, 1090]

This confirmed that the inorder traversal correctly organized the records from smallest to largest.

### Edge Case Testing

I also tested three edge cases to determine how the program handled different situations.

The first test involved an empty Binary Search Tree. The program returned an empty list for traversal and False when searching for a patient ID.

The second test involved inserting a duplicate patient ID. I attempted to insert patient ID 1040 again. The program ignored the duplicate, and the tree continued to contain seven unique records.

The third test involved creating a Binary Search Tree with only one patient ID. I inserted patient ID 2000 and confirmed that the traversal returned the single record. Searching for 2000 returned True, while searching for 2001 returned False.

The program produced the following results:

    === EDGE CASES ===
    Empty tree traversal: []
    Search 1050 in empty tree: False
    After inserting duplicate 1040: [1010, 1025, 1040, 1050, 1060, 1075, 1090]
    Number of records after duplicate: 7
    Single-node tree traversal: [2000]
    Search 2000 in single-node tree: True
    Search 2001 in single-node tree: False

These tests demonstrated that the BST handled empty trees, duplicate values, and single-node trees without errors.

### Real-World Application

I used a medical records management system because healthcare organizations often need to locate records using unique identifiers.

A Binary Search Tree demonstrated one way that numerical patient record IDs could be organized to support searching and retrieval.

In this project, each node represented a fictional patient ID rather than an actual medical record.

Although real healthcare systems would typically use databases and indexing systems, this example helped demonstrate how a BST could organize and search structured information.

### Final Reflection

Completing this project helped me better understand how Binary Search Trees worked and how recursion supported insertion, searching, and traversal.

One of the most useful concepts was seeing how the tree's structure affected searching. When the tree was balanced, the program could locate patient IDs without checking every node.

I also learned that insertion order mattered because inserting values in sequential order could create an unbalanced tree and reduce searching efficiency.

The inorder traversal demonstrated how the BST could display patient IDs in ascending order without requiring a separate sorting operation.

Testing empty trees, duplicate values, and single-node trees also helped me understand why edge cases were important when developing a program.

Overall, this assignment demonstrated how data structures could be applied to a healthcare-related example while reinforcing recursion, algorithm efficiency, and program testing.
