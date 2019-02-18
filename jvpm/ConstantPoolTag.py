from enum import Enum


class ConstantPoolTag(Enum):
    tag_01 = "01"
    tag_03 = "03"
    tag_04 = "04"
    tag_05 = "05"
    tag_06 = "06"
    tag_07 = "07"
    tag_08 = "08"
    tag_09 = "09"
    tag_10 = "0A"
    tag_11 = "0B"
    tag_12 = "0C"
    tag_15 = "0F"
    tag_16 = "10"
    tag_18 = "12"

    # Returns number of bytes for specific constant based on
    def get_byte_length(self, tag):
        return {
            "01": 2,    # This represents how many bytes the string size variable is [e.g 00 05 means total size is 5]
            "03": 4,
            "04": 4,
            "05": 8,
            "06": 8,
            "07": 2,
            "08": 2,
            "09": 4,
            "0A": 4,
            "0B": 4,
            "0C": 4,
            "0F": 3,
            "10": 2,
            "12": 4
        }.get(tag, None)

    def __init__(self, tag):
        self.data = self.get_byte_length(tag)
