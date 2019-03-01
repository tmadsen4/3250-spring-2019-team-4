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

    def test_opcode05(self): #load 2 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code05(test_stack)
        self.assertEqual(test_stack.pop(), 2)

    def test_opcode06(self): #load 3 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code06(test_stack)
        self.assertEqual(test_stack.pop(), 3)

    def test_opcode07(self): #load 4 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code07(test_stack)
        self.assertEqual(test_stack.pop(), 4)

    def test_opcode08(self): #load 5 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code08(test_stack)
        self.assertEqual(test_stack.pop(), 5)

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
        test_stack = [1,2,2147483647,2147483647,-2147483647,-2147483647]
        test_stack = op_codes1.op_codes.op_code60(test_stack)
        self.assertEqual(test_stack.pop(), -2147483647)
        test_stack = op_codes1.op_codes.op_code60(test_stack)
        self.assertEqual(test_stack.pop(), 2147483647)
        test_stack = op_codes1.op_codes.op_code60(test_stack)
        self.assertEqual(test_stack.pop(), 3)

    def test_op_code7e(self): # bitwise AND
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code7e(test_stack)
        self.assertEqual(test_stack.pop(), 1&2)

    def test_op_code6c(self): # integer division
        test_stack = [1,2,2,0]
        self.assertRaises(ArithmeticError, test_stack = op_codes1.op_codes.op_code6c(test_stack))
        test_stack = op_codes1.op_codes.op_code6c(test_stack)
        self.assertEqual(test_stack.pop(), 1 // 2)

    def test_op_code68(self): # multiplication
        test_stack = [1, 2, 2147483647, 2147483647, 2147483647, 4, 2147483647, 5, -2147483647, -2147483647, -2147483647, 4, -2147483647, 5]
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), -2147483647)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 0)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 0)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 2147483643)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), -4)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 1)
        test_stack = op_codes1.op_codes.op_code68(test_stack)
        self.assertEqual(test_stack.pop(), 1 * 2)

    def test_op_code74(self): # negative
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code74(test_stack)
        self.assertEqual(test_stack.pop() , -1 * 2)

    def test_opcode02(self): #load -1 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code02(test_stack)
        self.assertEqual(test_stack.pop(), -1)

    def test_opcode03(self): #load 0 onto stack
        test_stack = [1,2]
        test_stack = op_codes1.op_codes.op_code03(test_stack)
        self.assertEqual(test_stack.pop(), 0)

    def test_opcode04(self): #load 1 onto stack
        test_stack = []
        test_stack = op_codes1.op_codes.op_code04(test_stack)
        self.assertEqual(test_stack.pop(), 1)