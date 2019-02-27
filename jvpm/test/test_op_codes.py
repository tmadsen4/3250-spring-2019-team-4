import unittest
from jvpm import op_codes1

test_stack = [1,2]

class test_op_codes(unittest.TestCase):



    def test_op_code70(self):# remainder
        self.assertEqual(op_codes1.op_codes.op_code70(11,2),1)
    def test_op_code78(self):# shift left
        self.assertEqual(op_codes1.op_codes.op_code78(1,2),4)
    def test_op_code80(self):# bitwise OR
        self.assertEqual(op_codes1.op_codes.op_code80(4,1),5)

    def test_op_code60(self): # add
        self.assert_(self, test_stack.size() != 0)
        self.assertEqual (self, op_codes1.op_codes.op_code60(test_stack), test_stack.pop() == 3)

    def test_op_code7e(self): # bitwise AND
        self.assert_(self, test_stack.size() != 0)
        self.assertEqual(self, op_codes1.op_codes.op_code7e(test_stack), test_stack.pop() == (1 & 2))

    def test_op_code6c(self): # integer division
        self.assert_(self, test_stack.size() != 0)
        self.assertEqual(self, op_codes1.op_codes.op_code6c(test_stack), test_stack.pop() == (1 / 2))

    def test_op_code68(self): # multiplication
        self.assert_(self, test_stack.size() != 0)
        self.assertEqual(self, op_codes1.op_codes.op_code68(test_stack), test_stack.pop() == (1 * 2))

    def test_op_code74(self): # negative
        self.assert_(self, test_stack.size() != 0)
        self.assertEqual(self, op_codes1.op_codes.op_code74(test_stack), test_stack.pop() == (-1 * 2))
