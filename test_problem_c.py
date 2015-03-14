# vim:filetype=python:fileencoding=utf-8

import nose.tools as NT


# Problem C
# 1.    Create a class that can be used to represent the nodes of a binary tree,
# and then populate a binary tree with the nodes below. (Don't worry about
# writing an insertion algorithm, since the nodes are already mapped out for
# you.)
#  (drawing in Word)
# 2. Write a search algorithm that, when given an integer, will return that
# integer's depth in the tree. For example, searching for 9 will return 2, while
# searching for 14 will return 0. If the provided integer doesn't exist in the
# tree, return –1.
# 3. Search for the integers 0 through 50, and output a file
# binary_tree_results.txt with the results in the following format:


class TestProblemC(object):

    def setup(self):
        self.tree = btree_generate()

    def test_solution_1(self):
        # Make sure we have all 14 nodes.  Don't have time to make this a super
        # pretty printer.  I'm sure I could google it.
        print self.tree
        NT.assert_equal(14, repr(self.tree).count('Node'))

    def test_solution_2(self):
        NT.assert_equal(0, find_depth(self.tree, 14))
        NT.assert_equal(1, find_depth(self.tree, 6))
        NT.assert_equal(1, find_depth(self.tree, 25))
        NT.assert_equal(2, find_depth(self.tree, 9))
        NT.assert_equal(3, find_depth(self.tree, 12))
        NT.assert_equal(3, find_depth(self.tree, 28))
        NT.assert_equal(-1, find_depth(self.tree, 'missing'))

    def test_solution_3(self):
        result = write_depth_report(self.tree, 'output/binary_tree_results.txt')
        NT.assert_true(result)


class Node(object):
    # (I had just written this for another kata I was doing! Win!)

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node("%s", "%s", "%s")' % (self.value, self.left, self.right)


def btree_generate():
    tree = \
        Node(14,
            Node(6,
                Node(2,
                    Node(1, None, None),
                    Node(5, None, None)
                ),
                Node(9,
                    None,
                    Node(12, None, None)
                )
            ),
            Node(25,
                Node(19,
                    Node(17, None, None),
                    Node(23, None, None)
                ),
                Node(33,
                    Node(28, None, None),
                    Node(38, None, None)
                )
            )
        )
    print tree
    return tree


def find_depth(node, value, current_depth = 0):
    # recursive search
    if node is None:
        return -1
    if value == node.value:
        return current_depth
    result = find_depth(node.left, value, current_depth + 1)
    if result == -1:
        result = find_depth(node.right, value, current_depth + 1)
    return result


def write_depth_report(tree, filename):
    with open(filename, 'w') as f:
        for i in range(51):
            f.write('{0}:{1}\n'.format(i, find_depth(tree, i)))
    return True
