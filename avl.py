# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        if self.root == None:                       # add new node to empty tree
            self.root = TreeNode(value)
            return

        height = 0
        curr_node = self.root
        has_been_added = False
        while not has_been_added:                       # look through tree, branching left when
            if value < curr_node.value:                 # value to be added is smaller than current node.
                if curr_node.left is None:              # Continue until correct location is found, then
                    curr_node.left = TreeNode(value)    # add value.
                    curr_node.left.parent = curr_node
                    curr_node.left.height = height
                    has_been_added = True
                else:
                    curr_node = curr_node.left
            elif value > curr_node.value:              # look through tree, branching right when value
                if curr_node.right is None:             # to be added is greater than or equal to current
                    curr_node.right = TreeNode(value)   # node.  Continue until correct location is found,
                    curr_node.right.height = height     # then add node.
                    curr_node.right.parent = curr_node
                    has_been_added = True
                else:
                    curr_node = curr_node.right
            else:
                return
        while curr_node.parent != None:
            curr_node = curr_node.parent
            height += 1
        if curr_node.parent == None:
            curr_node.height = height

        if
        if self.root.left.height - self.root.right.height > 2:
            if self.root.left.left.height - self.root.left.right.height > 2:
                old_root = self.root
                curr_node = self.root.left
                old_right_child = curr_node.right
                self.root = curr_node
                old_root.parent = self.root
                old_root.left = old_right_child
                self.root.right = old_root
            else:
                curr_node = self.root.left
                temp = curr_node.right
                temp_left = temp.left
                self.root.left = temp
                temp.parent = self.root
                temp.left = curr_node
                curr_node.parent = temp
                curr_node.right = temp_left
                temp_left.parent = curr_node

                curr_node = self.root.left
                old_right_child = curr_node.right
                old_root = self.root
                self.root = curr_node
                old_root.left = old_right_child
                old_root.parent = self.root
                self.root.right = old_root

        elif elf.root.right.height - self.root.left.height > 2:
            if self.root.right.right.height - self.root.right.left.height > 2:
                old_root = self.root
                old_left_child = curr_node.left
                self.root = curr_node
                old_root.parent = self.root
                old_root.right = old_left_child
                self.root.left = old_root

            else:
                curr_node = self.root.right
                temp = curr_node.left
                temp_right = temp.right
                self.root.right = temp
                temp.parent = self.root
                temp.right = curr_node
                curr_node.parent = temp
                curr_node.left = temp_right
                temp_right.parent = curr_node

                curr_node = self.root.right
                old_left_child = curr_node.left
                old_root = self.root
                self.root = curr_node
                old_root.right = old_left_child
                old_root.parent = self.root
                self.root.left = old_root




    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)

    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),   # RR, RR
    #     (10, 20, 30, 50, 40),   # RR, RL
    #     (30, 20, 10, 5, 1),     # LL, LL
    #     (30, 20, 10, 1, 5),     # LL, LR
    #     (5, 4, 6, 3, 7, 2, 8),  # LL, RR
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     avl = AVL(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method add() example 3")
    # print("----------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL()
    #     for value in case:
    #         avl.add(value)
    #     if not avl.is_valid_avl():
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    # print('add() stress test finished')
    #
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),  # no AVL rotation
    #     ((1, 2, 3), 2),  # no AVL rotation
    #     ((1, 2, 3), 3),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # avl = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', avl, del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # avl = AVL(case)
    # for _ in case[:-2]:
    #     print('INPUT  :', avl, avl.root.value)
    #     avl.remove(avl.root.value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL(case)
    #     for value in case[::2]:
    #         avl.remove(value)
    #     if not avl.is_valid_avl():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('remove() stress test finished')
