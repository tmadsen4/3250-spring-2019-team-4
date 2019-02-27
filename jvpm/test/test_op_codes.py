import unittest
from jvpm import op_codes1

test_stack = [1,2]

'''
    def test_op_code70(self):# remainder
        self.assertEqual(op_codes1.op_codes.op_code70(11,2),1)
    def test_op_code78(self):# shift left
        self.assertEqual(op_codes1.op_codes.op_code78(1,2),4)
    def test_op_code80(self):# bitwise OR
        self.assertEqual(op_codes1.op_codes.op_code80(4,1),5)'''

class test_op_codes(unittest.TestCase):

    def test_op_code70(self): # remainder
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code70(test_stack)
        self.assertEqual(test_stack.pop() , 0)
        
    def test_op_code78(self): # shift left
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code78(test_stack)
        self.assertEqual(test_stack.pop() , 4)

    def test_op_code80(self): # bitwesi OR
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code80(test_stack)
        self.assertEqual(test_stack.pop() , 3)


    def test_op_code60(self): # add
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code60(test_stack)
        self.assertEqual(test_stack.pop() , 3)

    def test_op_code7e(self): # bitwise AND
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code7e(test_stack)
        self.assertEqual(test_stack.pop(), 1&2)

    def test_op_code6c(self): # integer division
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code6c(test_stack)
        self.assertEqual(test_stack.pop(), 2 // 1)

    def test_op_code68(self): # multiplication
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 1 * 2)

    def test_op_code74(self): # negative
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code74(test_stack)
        self.assertEqual(test_stack.pop() , -1 * 2)
