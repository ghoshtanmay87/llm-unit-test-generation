class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

import pytest

def test_empty_tree_returns_height_0():
    node = None
    expected = 0
    assert max_height(node) == expected

def test_single_node_tree_returns_height_1():
    node = Node(10)
    expected = 1
    assert max_height(node) == expected

def test_tree_with_left_child_only_returns_height_2():
    node = Node(10)
    node.left = Node(5)
    expected = 2
    assert max_height(node) == expected

def test_tree_with_right_child_only_returns_height_2():
    node = Node(10)
    node.right = Node(15)
    expected = 2
    assert max_height(node) == expected

def test_balanced_tree_with_two_levels_returns_height_2():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    expected = 2
    assert max_height(node) == expected

def test_unbalanced_tree_with_left_subtree_deeper_returns_correct_height_3():
    node = Node(10)
    node.left = Node(5)
    node.left.left = Node(3)
    expected = 3
    assert max_height(node) == expected

def test_unbalanced_tree_with_right_subtree_deeper_returns_correct_height_4():
    node = Node(10)
    node.right = Node(15)
    node.right.right = Node(20)
    node.right.right.right = Node(25)
    expected = 4
    assert max_height(node) == expected

def test_complex_balanced_tree_returns_correct_height_3():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)
    expected = 3
    assert max_height(node) == expected