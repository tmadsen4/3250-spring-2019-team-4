import unittest

class TestClassFile(unittest.TestCase):
    def setUp(self):
    jvpm.ClassFile.ClassFile()

    def test_magic(self):
        self.assertEqual(self.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.get_minor(), 1)

    def test_major(self):
        self.assertEqual(self.get_major(), 5)

    def test_pool_count(self):
        self.assertEqual(self.get_pool_count(), 16)
