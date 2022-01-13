# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

rock_to_number = {'.': 1, ':': 2,  '-': 3, ' ': 0}
numbers_to_rocks = {v:k for k,v in rock_to_number.items()}

def stack_wall(wall):
    stacked_wall = ['' for i in range(len(wall))]
    n_piles = len(wall[0])
    for i in range(n_piles):
        pile = [row[i] for row in wall]
        stacked_pile = stack_rock_pile(pile)
        append_transposed(stacked_wall, stacked_pile)
    return stacked_wall

def stack_rock_pile(rocks):
    tmp, result = [], []
    for e in rocks:
        tmp = stack_rock(rock_to_number[e], tmp)
        if e == '-':
            result.extend(sorted(tmp))
            tmp = []
    if tmp:
        result.extend(sorted(tmp))
    return translate_back(result)

def translate_back(pile):
    return ''.join([numbers_to_rocks[e] for e in pile])

def append_transposed(wall, pile):
    for i in range(len(wall)):
        wall[i] += pile[i]
        
# This could be simplified by adding a RocksStack class
# that would inherit from list which performs that logic
# when adding a new element
def stack_rock(rock, stack):
    if not stack:
        return [rock]
    if rock == 1:
        if stack[0] == 1:
            stack[0] = 2
            stack.append(0)
        else:
            stack.insert(0, rock)
        return stack
    if rock == 2:
        stack.insert(0, rock)
    else:
        stack.append(rock)
    return stack

import unittest
class test_stack_rock(unittest.TestCase):
    def test_stack_rock_with_empty_stack(self):
        stack = []
        result = stack_rock(1,stack)
        self.assertEquals(result, [1])
    def test_stack_one_rock(self):
        stack = [1]
        result = stack_rock(1,stack)
        self.assertEquals(result, [2,0])
    def test_add_one_rock(self):
        stack = [2]
        result = stack_rock(1,stack)
        self.assertEquals(result, [1,2]) 
    def test_add_two_rocks(self):
        stack = [1]
        result = stack_rock(2,stack)
        self.assertEquals(result, [2,1])
    def test_add_table_or_empty(self):
        stack = [1]
        result = stack_rock(3,stack)
        self.assertEquals(result, [1,3])

class test_stack_rock_pile(unittest.TestCase):
    def test_stack_rocks_no_table(self):
        rocks = ' :. .: '
        result = stack_rock_pile(rocks)
        self.assertEquals(result, '    :::')
    def test_stack_rocks_with_table(self):
        rocks = ' :.-.: '
        result = stack_rock_pile(rocks)
        self.assertEquals(result, ' .:- .:')
    def test_stack_rocks_with_tables_only(self):
        rocks = '----'
        result = stack_rock_pile(rocks)
        self.assertEquals(result, '----')

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
        self.assertEquals(result, expe)
    
if __name__ == '__main__':
    unittest.main()