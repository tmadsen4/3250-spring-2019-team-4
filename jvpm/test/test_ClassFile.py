
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

    def test_get_pool_count_raw_int(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_raw_int(self.unittest_file), int("000F", 16))

    def test_get_pool_count_int(self):
        self.assertEqual(ClassFile.JavaClassFile.get_pool_count_int(self.unittest_file), int("000E", 16))

    def test_get_constant_table(self):
        expected_table = ['0A0003000C',
                          '07000D',
                          '07000E',
                          '0100063C696E69743E',
                          '010003282956',
                          '010004436F6465',
                          '01000F4C696E654E756D6265725461626C65',
                          '0100046D61696E',
                          '010016285B4C6A6176612F6C616E672F537472696E673B2956',
                          '01000A536F7572636546696C65',
                          '010009746573742E6A617661',
                          '0C00040005',
                          '01000474657374',
                          '0100106A6176612F6C616E672F4F626A656374']

        self.assertEqual(ClassFile.JavaClassFile.get_constant_table(self.unittest_file), expected_table)

    def test_get_constant_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_constant_table_size(self.unittest_file), 139)

    def test_get_access_flag(self):
        self.assertEqual(ClassFile.JavaClassFile.get_access_flag(self.unittest_file), "0021")

    def test_get_class_identifier(self):
        self.assertEqual(ClassFile.JavaClassFile.get_class_identifier(self.unittest_file), "07000E")

    def test_get_superclass_identifier(self):
        self.assertEqual(ClassFile.JavaClassFile.get_superclass_identifier(self.unittest_file), "0100063C696E69743E")

    def test_get_interface_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_interface_count(self.unittest_file), "0000")

    def test_get_interface_table(self):
        expected_table = []

        self.assertEqual(ClassFile.JavaClassFile.get_interface_table(self.unittest_file), expected_table)

    def test_get_interface_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_interface_table_size(self.unittest_file), 0)

    def test_get_interfaces(self):
        expected_table = []

        self.assertEqual(ClassFile.JavaClassFile.get_interfaces(self.unittest_file), expected_table)

    def test_get_field_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_field_count(self.unittest_file), "0000")

    def test_get_field_table(self):
        expected_table = []
        self.assertEqual(ClassFile.JavaClassFile.get_field_table(self.unittest_file), expected_table)

    def test_get_field_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_field_table_size(self.unittest_file), 0)

    def test_get_fields(self):
        expected_table = []
        self.assertEqual(ClassFile.JavaClassFile.get_fields(self.unittest_file), expected_table)

    def test_get_method_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_method_count(self.unittest_file), "0002")

    def test_get_method_table(self):
        expected_table = ['000100040005000100060000001D00010001000000052AB70001B100000001000700000006000100000001',
                          '00090008000900010006000000260001000200000006043C840101B10000000100070000000E0003000000030002000400050006']

        self.assertEqual(ClassFile.JavaClassFile.get_method_table(self.unittest_file), expected_table)

    def test_get_method_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_method_table_size(self.unittest_file), 95)

    def test_get_methods(self):
        expected_table = {'Method 1': '010003282956',
                          'Method 1 Descriptor': '010004436F6465',
                          'Method 1 Attributes':
                              {'Attribute 1': '01000F4C696E654E756D6265725461626C65',
                               'Attribute 1 Length': '0000001D',
                               'Attribute 1 Code': '00010001000000052AB70001B100000001000700000006000100000001'},
                          'Method 2': '010016285B4C6A6176612F6C616E672F537472696E673B2956',
                          'Method 2 Descriptor': '01000A536F7572636546696C65',
                          'Method 2 Attributes':
                              {'Attribute 1': '01000F4C696E654E756D6265725461626C65',
                               'Attribute 1 Length': '00000026',
                               'Attribute 1 Code': '0001000200000006043C840101B10000000100070000000E0003000000030002000400050006'}}

        self.assertEqual(ClassFile.JavaClassFile.get_methods(self.unittest_file), expected_table)

    def test_get_attribute_count(self):
        self.assertEqual(ClassFile.JavaClassFile.get_attribute_count(self.unittest_file), "0001")

    def test_get_attribute_table(self):
        expected_table = ['000A00000002000B']

        self.assertEqual(ClassFile.JavaClassFile.get_attribute_table(self.unittest_file), expected_table)

    def test_get_attribute_table_size(self):
        self.assertEqual(ClassFile.JavaClassFile.get_attribute_table_size(self.unittest_file), 8)
