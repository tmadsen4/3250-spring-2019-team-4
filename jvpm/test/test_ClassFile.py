
import unittest
from jvpm import ClassFile

class testClass(unittest.TestCase):
    ClassFile.JavaClassFile()
    def test_get_magic_number(self):
        self.assertEqual(ClassFile.JavaClassFile.get_magic_number(self), 'CAFEBABE')
        
    def test_get_major(self):
        self.assertEqual(ClassFile.JavaClassFile.get_minor(self), '0000')

    def test_get_minor(self):
        self.assertEqual(ClassFile.JavaClassFile.get_major(self), '0037')

    def test_pool_count_raw(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count(self), '000E')
        
    def test_pool_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count(self), '000E')
