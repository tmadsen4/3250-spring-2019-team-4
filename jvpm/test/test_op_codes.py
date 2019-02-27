import unittest
from jvpm import op_codes1

class test_op_codes(unittest.TestCase):

    test_stack = [1,2]

    def test_op_code70(self):# remainder
        self.assertEqual(op_codes1.op_codes.op_code70(11,2),1)
    def test_op_code78(self):# shift left
        self.assertEqual(op_codes1.op_codes.op_code78(1,2),4)
    def test_op_code80(self):# bitwise OR
        self.assertEqual(op_codes1.op_codes.op_code80(4,1),5)

    def test_op_code60(self):
        self.assert_(self, stack_z != 0)

    def test_op_code7e(self):
        self.assert_(self, stack_z != 0)

    def test_op_code6c(self):
        self.assert_(self, stack_z != 0)

    def test_op_code68(self):
        self.assert_(self, stack_z != 0)

    def test_op_code74(self):
        self.assert_(self, stack_z != 0)
