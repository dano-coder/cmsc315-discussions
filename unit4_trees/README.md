
# Unit 4 Discussion: Binary Search Trees

## Project Overview

For this assignment, I chose to create a medical records management system using a Binary Search Tree (BST). The purpose of this project was to demonstrate how patient medical record IDs could be organized and searched efficiently using a tree structure.

I continued using a healthcare example from my previous programming assignments to demonstrate how data structures could be applied in a real-world setting.

## Push 1: Initial BST Structure

For the first part of this project, I established the basic structure of the Binary Search Tree.

I created a Node class that stored a numerical patient record ID. Each node also contained references to its left and right children. These references were initially set to None because new nodes did not have any children.

I also created a BST class that initialized the root as None. This represented an empty tree before any patient records were inserted.

## Implementation

The Node class contained three attributes:

1. value: Stored the patient's numerical record ID.
2. left: Referenced the left child node.
3. right: Referenced the right child node.

The BST class contained a root attribute that identified the starting point of the tree.

I retained the original TODO prompts for recursive insertion, searching, and in-order traversal. These operations were reserved for later stages of development.

## Testing and Results

I ran the Python program through the IntelliJ terminal and confirmed that the initial BST was created successfully.

The program displayed the following output:

    === UNIT 4: BINARY SEARCH TREES ===
    Medical Records Management System

    === TREE CONSTRUCTION ===
    Medical records BST initialized.
    Root node: None

The root displayed None because no patient records had been inserted yet. This was the expected result for an empty Binary Search Tree.

## Reflection

During this initial stage, I learned how a Binary Search Tree was structured using individual nodes and references to child nodes. I also learned that the root served as the starting point for accessing the tree.

One important concept was understanding how nodes would eventually be organized based on their numerical values. Smaller patient record IDs would be placed in the left subtree, while larger IDs would be placed in the right subtree.

This organization could improve searching compared to checking every record individually, provided the tree remained reasonably balanced.

The initial implementation established the foundation for adding recursive insertion, searching, traversal, and edge case testing in later stages.
