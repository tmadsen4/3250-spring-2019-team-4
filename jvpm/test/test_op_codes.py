import unittest
from jvpm import op_codes1
        
'''
   def test_OP_code60(self): 
       	self.assert_(self, stack_z != 0)

    def test_OP_code7e(self):
    	self.assert_(self, stack_z != 0)

    def test_OP_code6c(self):
    	self.assert_(self, stack_z != 0)

    def test_OP_code68(self):
    	self.assert_(self, stack_z != 0)

    def test_OP_code74(self):
        self.assert_(self, stack_z != 0)

    def test_push_to_stack(self):'''

class test_op_codes(unittest.TestCase):
    data = op_codes1.Op_codes()
    
    def test_op_code70(self):
        self.assertEqual(op_codes1.Op_codes.OP_code70(11,2),1)
