from jvpm.ConstantPoolTag import *


class JavaClassFile:
    classfile_oonstant_table = []
    classfile_constant_table_size = -1

    # Python "Constructor"

    def get_magic_number(self):
        magic_num = ""

        # Magic number's length is 8 hexadecimal characters and are separated by 2 each [i.e CA FE BA BE]
        # So each "element" of the JavaClassFile type object with the data from the class file is 2 hexadecimal digits
        # This is not true for some of the other elements [e.g flags] but will work for getting the magic number
        # Especially since it is known that the magic number is always on the top of the file
        for i in range(4):
            # 02 for format's 2nd parameter means 2 digits, X means capital format, if I wanted it to be in 0xFF format
            # I would put in #04X, 0xff would be #04x
            magic_num += format(self.data[i], "02X")
        return magic_num

    def get_major(self):
        major_version = format(self.data[6], "02X") + format(self.data[7], "02X")

        return major_version

    def get_minor(self):
        minor_version = format(self.data[4], "02X") + format(self.data[5], "02X")

        return minor_version

    def get_pool_count_raw(self):
        pool_count_raw = format(self.data[8], "02X") + format(self.data[9], "02X")

        return pool_count_raw

    def get_pool_count(self):
        # Pool count should be made of 2 bytes so 04X is the format parameter
        pool_count = int(self.get_pool_count_raw(), 16) - 1
        pool_count = format(pool_count, "04X")

        return pool_count

    def get_pool_count_raw_int(self):
        return int(self.get_pool_count_raw(), 16)

    def get_pool_count_int(self):
        return int(self.get_pool_count(), 16)

    def get_constant_table(self):
        byte_location = 10  # First tag is at byte 10
        constant = ""
        constant_table = []
        size = 0

        # Loop will stop once all constant values have been collected
        for i in range(self.get_pool_count_int()):
            data_value = format(self.data[byte_location], "02X")
            # Tag represents a string, which means there is still a 2 byte size value that needs to be read
            if data_value == "01":
                constant += data_value
                # Get the 2 prefix bytes that describe the string size
                byte_location += 1
                data_value = format(self.data[byte_location], "02X")
                byte_location += 1
                data_value += format(self.data[byte_location], "02X")
                byte_location += 1
                constant += data_value
                size += 3
                # Get the offset for a string from the ConstantPoolTag Class
                tag = ConstantPoolTag("01")
                num_bytes = int(data_value, 16)
                for k in range(byte_location, byte_location + int(num_bytes)):
                    constant += format(self.data[k], "02X")
                    size += 1

                constant_table.append(constant)
                constant = ""
                byte_location += int(num_bytes)
            # Tag represents something else, which means only that value needs to be read
            else:
                tag = ConstantPoolTag(data_value)
                num_bytes = tag.get_byte_length(data_value)
                constant += data_value
                byte_location += 1
                size += 1
                for j in range(byte_location, byte_location + int(num_bytes)):
                    constant += format(self.data[j], "02X")
                    size += 1

                constant_table.append(constant)
                constant = ""
                byte_location += int(num_bytes)

        self.classfile_constant_table_size = size
        self.classfile_constant_table = constant_table
        return constant_table

    def get_constant_table_size(self):
        return self.classfile_constant_table_size

    # Following methods require the cpsize, which is returned with the constant table, might want a
    # separate constant later instead of calling the get_constant_table method for performance reasons

    # The access flags are "put together" [e.g ACC_PUBLIC and ACC_SUPER is 0x0021]
    def get_access_flag(self, cpsize):
        access_flag_byte1 = 10 + cpsize
        access_flag_byte2 = 11 + cpsize

        access_flag = (format(self.data[access_flag_byte1], "02X") +
                       format(self.data[access_flag_byte2], "02X"))
        return access_flag

    def get_class_identifier(self):
        constant_table = self.classfile_constant_table
        cpsize = self.get_constant_table_size()

        class_index_byte1 = 12 + cpsize
        class_index_byte2 = 13 + cpsize

        class_index = (format(self.data[class_index_byte1], "02X") +
                       format(self.data[class_index_byte2], "02X"))

        class_index = int(class_index, 16)
        class_identifier = constant_table[class_index]

        return class_identifier

    def get_superclass_identifier(self):
        constant_table = self.get_constant_table()
        cpsize = self.get_constant_table_size()

        superclass_index_byte1 = 14 + cpsize
        superclass_index_byte2 = 15 + cpsize
        # Index of the constant pool table
        superclass_index = (format(self.data[superclass_index_byte1], "02X") +
                            format(self.data[superclass_index_byte2], "02X"))
        superclass_index = int(superclass_index, 16)
        if superclass_index == 0:
            superclass_identifier = "None"
        else:
            superclass_identifier = constant_table[0][superclass_index]

        return superclass_identifier

    def get_interface_count(self, cpsize):
        count_index_byte1 = 16 + cpsize
        count_index_byte2 = 17 + cpsize

        interface_count = (format(self.data[count_index_byte1], "02X") +
                           format(self.data[count_index_byte2], "02X"))

        return interface_count

    def get_interface_table(self, cpsize):
        interface_count = int(self.get_interface_count(cpsize), 16)
        byte_location = 18 + cpsize
        interface_table = []

        for i in range(interface_count):
            interface_table.append(self.data[byte_location])
            byte_location += 1

        return interface_table

    def get_interfaces(self):
        interface_table = self.get_interface_table()


    # For Testing

    def print_data(self):
        print("Magic Number: " + self.get_magic_number())
        print("Major Version: " + self.get_major())
        print("Minor Version: " + self.get_minor())
        print("Pool Count: " + self.get_pool_count_raw())
        print("Pool Count - 1: " + self.get_pool_count())
        print("Constant Table: " + str(self.get_constant_table()))
        print("Constant Table Size: ")
        print("Access Flag: " + self.get_access_flag(self.get_constant_table_size()))
        print("Class Identifier: " + self.get_class_identifier())
        print("Super Class Identifier: " + self.get_superclass_identifier())
        print("Interface Count: " + self.get_interface_count(self.get_constant_table_size()))
        print("Interface Table: " + str(self.get_interface_table(self.get_constant_table_size())))


    def __init__(self):
        # TODO: Make it so that the .class file can be specified by name, this could help in testing opcode reading

        # "with" operator deals with closing the input stream and also handles some exceptions
        # Second parameter simply means "read binary"
        with open("test.class", 'rb') as class_file:
            # Literally sets the object of this class to whatever is on the other side of the equals sign
            # For example with object a of class x and self.data = 0 in constructor, print(a.data) would print 0
            self.data = class_file.read()

# -----END OF METHOD DEFINITIONS-----
a = JavaClassFile()
a.print_data()
