from unittest import TestCase

from bst import Node, from_list


class FromListTestCase(TestCase):
    def test_empty_heap(self):
        array = []
        node = from_list(array)
        self.assertIsNone(node)

    def test_length_1_heap(self):
        array = [0]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_length_1_heap_with_missing_value(self):
        array = [None]
        node = from_list(array)
        self.assertIsNone(node)

    def test_length_2_heap(self):
        array = [0, 1]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNone(node.right)

    def test_length_2_heap_with_missing_value(self):
        array = [0, None]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_length_3_heap(self):
        array = [0, 1, 2]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)

    def test_length_3_heap_with_missing_value(self):
        array = [0, 1, None]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNone(node.right)

    def test_length_4_heap(self):
        array = [0, 1, 2, 3]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)
        self.assertIsNotNone(node.left.left)
        self.assertEqual(node.left.left.value, 3)

    def test_length_5_heap(self):
        array = [0, 1, 2, 3, 4]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)
        self.assertIsNotNone(node.left.left)
        self.assertEqual(node.left.left.value, 3)
        self.assertIsNotNone(node.left.right)
        self.assertEqual(node.left.right.value, 4)

    def test_length_6_heap(self):
        array = [0, 1, 2, 3, 4, 5]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)
        self.assertIsNotNone(node.left.left)
        self.assertEqual(node.left.left.value, 3)
        self.assertIsNotNone(node.left.right)
        self.assertEqual(node.left.right.value, 4)
        self.assertIsNotNone(node.right.left)
        self.assertEqual(node.right.left.value, 5)

    def test_length_7_heap(self):
        array = [0, 1, 2, 3, 4, 5, 6]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)
        self.assertIsNotNone(node.left.left)
        self.assertEqual(node.left.left.value, 3)
        self.assertIsNotNone(node.left.right)
        self.assertEqual(node.left.right.value, 4)
        self.assertIsNotNone(node.right.left)
        self.assertEqual(node.right.left.value, 5)
        self.assertIsNotNone(node.right.right)
        self.assertEqual(node.right.right.value, 6)

    def test_length_7_heap_with_missing_left_tree(self):
        array = [0, None, 2, None, None, 5, 6]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.value, 2)
        self.assertIsNotNone(node.right.left)
        self.assertEqual(node.right.left.value, 5)
        self.assertIsNotNone(node.right.right)
        self.assertEqual(node.right.right.value, 6)

    def test_length_7_heap_with_missing_right_tree(self):
        array = [0, 1, None, 3, 4]
        node = from_list(array)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 0)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.value, 1)
        self.assertIsNone(node.right)
        self.assertIsNotNone(node.left.left)
        self.assertEqual(node.left.left.value, 3)
        self.assertIsNotNone(node.left.right)
        self.assertEqual(node.left.right.value, 4)


class ValidateTestCase(TestCase):
    def test_tree(self):
        bst = Node(2, Node(1), Node(3))
        self.assertTrue(bst.validate())

    def test_invalid_tree(self):
        bst = Node(2, Node(3), Node(1))
        self.assertFalse(bst.validate())

    def test_leaf(self):
        bst = Node(1)
        self.assertTrue(bst.validate())

    def test_left_subtree(self):
        bst = Node(2, left=Node(1))
        self.assertTrue(bst.validate())

    def test_invalid_left_subtree(self):
        bst = Node(2, left=Node(3))
        self.assertFalse(bst.validate())

    def test_right_subtree(self):
        bst = Node(2, right=Node(3))
        self.assertTrue(bst.validate())

    def test_invalid_right_subtree(self):
        bst = Node(2, right=Node(1))
        self.assertFalse(bst.validate())


class MaximumTestCase(TestCase):
    def test_leaf(self):
        bst = Node(1)
        maximum = bst.maximum()
        self.assertEqual(maximum, 1)

    def test_tree(self):
        bst = Node(1, right=Node(2))
        maximum = bst.maximum()
        self.assertEqual(maximum, 2)


class MinimumTestCase(TestCase):
    def test_leaf(self):
        bst = Node(1)
        minimum = bst.minimum()
        self.assertEqual(minimum, 1)

    def test_tree(self):
        bst = Node(2, left=Node(1))
        minimum = bst.minimum()
        self.assertEqual(minimum, 1)


class ContainsTestCase(TestCase):
    def test_false(self):
        bst = Node(1)
        has = bst.contains(0)
        self.assertFalse(has)

    def test_root(self):
        bst = Node(1)
        has = bst.contains(1)
        self.assertTrue(has)

    def test_left_subtree(self):
        bst = Node(2, left=Node(1))
        has = bst.contains(1)
        self.assertTrue(has)

    def test_right_subtree(self):
        bst = Node(0, right=Node(1))
        has = bst.contains(1)
        self.assertTrue(has)


class InsertTestCase(TestCase):
    def test_root(self):
        bst = Node(1)
        node = bst.insert(1)
        self.assertEqual(bst, node)

    def test_left_leaf(self):
        bst = Node(2)
        exp = Node(1)
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(2, exp))

    def test_left(self):
        bst = Node(2, left=Node(0))
        exp = Node(1, left=Node(0))
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(2, left=exp))

    def test_left_subtree(self):
        bst = Node(3, left=Node(2))
        exp = Node(1)
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(3, left=Node(2, left=exp)))

    def test_right_leaf(self):
        bst = Node(0)
        exp = Node(1)
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(0, right=exp))

    def test_right(self):
        bst = Node(0, right=Node(2))
        exp = Node(1, right=Node(2))
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(0, right=exp))

    def test_right_subtree(self):
        bst = Node(-1, right=Node(0))
        exp = Node(1)
        node = bst.insert(1)
        self.assertEqual(node, exp)
        self.assertEqual(bst, Node(-1, right=Node(0, right=exp)))


class DeleteTestCase(TestCase):
    def test_root(self):
        bst = Node(1)
        with self.assertRaises(RuntimeError):
            bst.delete(1)

    def test_left_leaf(self):
        bst = Node(2)
        removed = bst.delete(1)
        self.assertFalse(removed)

    def test_left(self):
        bst = Node(2, left=Node(1))
        removed = bst.delete(1)
        self.assertTrue(removed)
        self.assertEqual(bst, Node(2))

    def test_left_subtree(self):
        bst = Node(2, left=Node(1, left=Node(0)))
        removed = bst.delete(1)
        self.assertTrue(removed)
        self.assertEqual(bst, Node(2, left=Node(0)))

    def test_right_leaf(self):
        bst = Node(0)
        removed = bst.delete(1)
        self.assertFalse(removed)

    def test_right(self):
        bst = Node(0, right=Node(1))
        removed = bst.delete(1)
        self.assertTrue(removed)
        self.assertEqual(bst, Node(0))

    def test_right_subtree(self):
        bst = Node(0, right=Node(1, right=Node(2)))
        removed = bst.delete(1)
        self.assertTrue(removed)
        self.assertEqual(bst, Node(0, right=Node(2)))
