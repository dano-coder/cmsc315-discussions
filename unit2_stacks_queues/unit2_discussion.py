"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The last chart change added will be the first one removed  (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Stack empty = should return a message instead of closing/crashing
        # Upon completion, method will remove most recent chart change
         if self.is_empty():
                    raise IndexError("pop from empty stack")
                return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek will show the most recent chart change w/o removing it
        if self.is_empty():
                    raise IndexError("peek from empty stack")
                return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Will return True when there are no chart changes
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # Stores patients waiting to be registered
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New Patients are added to the end of the registration line - FIFO
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Removes the patient who has been waiting the longest - FIFO
        # If no patients are waiting, return a message instead of crashing
                if self.is_empty():
                    raise IndexError("dequeue from empty queue")
                return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Shows the next patient waiting to register without removing them.
                if self.is_empty():
                    raise IndexError("front from empty queue")
                return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True when no patients are waiting to be registered
        return len(self.items) == 0



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: PATIENT CHART CHANGES ===")

    # Create a stack to track changes made to a patient chart.
    chart_changes = Stack()

    # Add four chart changes in the order they were made.
    chart_changes.push("Updated medication list")
    chart_changes.push("Added patient note")
    chart_changes.push("Updated discharge plan")
    chart_changes.push("Updated patient contact information")

    print("Four changes have been added to the patient chart.")

    # LIFO means the last chart change added is removed first.
    print("Undo most recent change:", chart_changes.pop())
    print("Undo next change:", chart_changes.pop())

    # Peek shows the most recent remaining change without removing it.
    print("Next change to undo:", chart_changes.peek())

    # Remove the remaining changes so the stack becomes empty.
    print("Undo change:", chart_changes.pop())
    print("Undo change:", chart_changes.pop())

    print("Is the chart change stack empty?", chart_changes.is_empty())

    # Test what happens when trying to remove a change from an empty stack.
    # The try/except prevents the program from crashing.
    try:
        chart_changes.pop()
    except IndexError:
        print("Cannot undo a change because the stack is empty.")

    # Test empty stack
    try:
        chart_changes.peek()
    except IndexError:
        print("Cannot view a chart change because the stack is empty.")

    # Test a stack containing only one chart change.
    single_change = Stack()
    single_change.push("Updated patient allergies")

    print("Single chart change:", single_change.pop())

    # Verify that removing the only item leaves the stack empty.
    print("Is the single-change stack empty?", single_change.is_empty())




    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: PATIENT REGISTRATION ===")

    # Create a queue for patients waiting to register.
    patient_queue = Queue()

    # Add four patients in the order they arrive.
    patient_queue.enqueue("Patient A")
    patient_queue.enqueue("Patient B")
    patient_queue.enqueue("Patient C")
    patient_queue.enqueue("Patient D")

    print("Four patients have arrived for registration.")

    # FIFO means the first patient added is the first one removed.
    print("First patient registered:", patient_queue.dequeue())
    print("Second patient registered:", patient_queue.dequeue())

    # Front shows the next patient without removing them.
    print("Next patient waiting:", patient_queue.front())

    # Register the remaining patients.
    print("Next patient registered:", patient_queue.dequeue())
    print("Last patient registered:", patient_queue.dequeue())

    # Check whether any patients remain in the registration line.
    print("Is the registration queue empty?", patient_queue.is_empty())

    # Test removing a patient when the queue is empty.
    # The try/except prevents the program from crashing.
    try:
        patient_queue.dequeue()
    except IndexError:
        print("Cannot register another patient because the queue is empty.")

    # Test viewing the front of an empty queue.
    try:
        patient_queue.front()
    except IndexError:
        print("Cannot view the next patient because the queue is empty.")

    # Test a queue containing only one patient.
    single_patient = Queue()
    single_patient.enqueue("Patient E")

    print("Single patient registered:", single_patient.dequeue())

    # Verify the queue is empty after registering the only patient.
    print("Is the single-patient queue empty?", single_patient.is_empty())


    if __name__ == "__main__":
        main()
