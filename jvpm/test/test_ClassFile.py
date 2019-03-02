
import unittest
from jvpm import ClassFile

class testClass(unittest.TestCase):
    unittest_file = ClassFile.JavaClassFile("test.class")
    
    def test_get_magic_number(self):
        self.assertEqual(ClassFile.JavaClassFile.get_magic_number(self.unittest_file), 'CAFEBABE')
        
    def test_get_major(self):
        self.assertEqual(ClassFile.JavaClassFile.get_minor(self.unittest_file), '0000')

    def test_get_minor(self):
        self.assertEqual(ClassFile.JavaClassFile.get_major(self.unittest_file), '0037')

    def test_get_pool_count_raw(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_raw(self.unittest_file), '000F')
        
    def test_get_pool_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count(self.unittest_file), '000E')

    def test_get_constant_table(self):
        print("TODO")

    def test_get_constant_table_size(self):
        print("TODO")

    def test_get_interface_table(self):
        print("TODO")