from jvpm.ConstantPoolTag import *


class JavaClassFile:

    # Python "Constructor"
    def __init__(self):
        # TODO: Make it so that the .class file can be specified by name, this could help in testing opcode reading

        # "with" operator deals with closing the input stream and also handles some exceptions
        # Second parameter simply means "read binary"
        with open("test.class", 'rb') as class_file:
            # Literally sets the object of this class to whatever is on the other side of the equals sign
            # For example with object a of class x and self.data = 0 in constructor, print(a.data) would print 0
            self.data = class_file.read()

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
            if data_value == "01":
                print("TODO")
            else:
                tag = ConstantPoolTag(data_value)
                num_bytes = tag.get_byte_length(data_value)
                byte_location += 1
                for j in range(byte_location, byte_location + int(num_bytes)):
                    constant += format(self.data[j], "02X")
                    size += 1

                constant_table.append(constant)
                constant = ""
                byte_location += int(num_bytes)
                print(byte_location)

        return constant_table, size

a = JavaClassFile()
print(a.data)
print(a.get_magic_number())
print(a.get_major())
print(a.get_minor())
print(a.get_pool_count_raw())
print(a.get_pool_count())
print(a.get_constant_table())