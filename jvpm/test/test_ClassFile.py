
import unittest
from jvpm import ClassFile

class testClass(unittest.TestCase):
    data = ClassFile.JavaClassFile()
    
    def test_get_magic_number(self):
        self.assertEqual(ClassFile.JavaClassFile.get_magic_number(self.data), 'CAFEBABE')
        
    def test_get_major(self):
        self.assertEqual(ClassFile.JavaClassFile.get_minor(self.data), '0000')

    def test_get_minor(self):
        self.assertEqual(ClassFile.JavaClassFile.get_major(self.data), '0037')

    def test_get_pool_count_raw(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_raw(self.data), '000F')
        
    def test_get_pool_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count(self.data), '000E')
