# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def stack_wall(wall):
    stacked_wall = ['' for i in range(len(wall))]
    n_piles = len(wall[0])
    for i in range(n_piles):
        pile = [row[i] for row in wall]
        stacked_pile = stack_rock_pile(pile)
        append_transposed(stacked_wall, stacked_pile)
    return stacked_wall

def stack_rock_pile(rocks):
    result = ''
    stack = StackedRocks()
    for e in rocks:
        stack.add(e)
        if e == '-':
            result += stack.pile()
            stack = StackedRocks()
    if stack:
        result += stack.pile()
    return result

def append_transposed(wall, pile):
    for i in range(len(wall)):
        wall[i] += pile[i]

class StackedRocks():
    def __init__(self):
        self.n_elements = 0
        self.table = ''
        self.n_rocks = 0

    def add(self, e):
        if self.table:
            raise ValueError("can't add more elements after adding a table (-)")
        self.n_elements += 1
        if e == '.':
            self.n_rocks += 1
        if e == ':':
            self.n_rocks += 2
        if e == "-":
            self.table = '-'

    def pile(self):
        n_double = self.n_rocks // 2
        n_single = self.n_rocks % 2
        rocks = f"{'.' * n_single}{':' * n_double}"
        return f"{rocks}{self.table}".rjust(self.n_elements)

import unittest
class test_stacked_rock(unittest.TestCase):
    def test_add(self):
        stack = StackedRocks()
        stack.add('.')
        stack.add('.')
        stack.add(' ')
        stack.add(':')
        stack.add('-')
        self.assertEqual(stack.pile(), '  ::-')

    def test_exception(self):
        stack = StackedRocks()
        with self.assertRaises(ValueError) as ctx:
            stack.add('.')
            stack.add('.')
            stack.add('-')
            stack.add('.')

class test_stack_rock_pile(unittest.TestCase):
    def test_stack_rocks_no_table(self):
        rocks = ' :. .: '
        result = stack_rock_pile(rocks)
        self.assertEqual(result, '    :::')
    def test_stack_rocks_with_table(self):
        rocks = ' :.-.: '
        result = stack_rock_pile(rocks)
        self.assertEqual(result, ' .:- .:')
    def test_stack_rocks_with_tables_only(self):
        rocks = '----'
        result = stack_rock_pile(rocks)
        self.assertEqual(result, '----')

class test_stack_wall(unittest.TestCase):
    def test_stack_wall(self):
        wall = [".::..-",
                " ..  .",
                " -.-..",
                "  :   ",
                ".:   ."]
        result = stack_wall(wall)
        expe = [" .   -",
                " : .  ",
                " -:-  ",
                "  :  .",
                "::: ::"]
        self.assertEqual(result, expe)
    
if __name__ == '__main__':
    unittest.main()
