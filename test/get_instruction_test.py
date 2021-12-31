import unittest
import re

def get_instruction(line):
    return re.sub("#.*$", "", line).strip().split()

class TestGetInstruction(unittest.TestCase):

    def test_only_comment(self):
        s = "  # Hello World! \n"
        self.assertTrue(not get_instruction(s))

    def test_only_whitespace(self):
        s = "                 "
        self.assertTrue(not get_instruction(s))

    def test_empty_line(self):
        s = ""
        self.assertTrue(not get_instruction(s))

    def test_newline_char(self):
        s = "\n"
        self.assertTrue(not get_instruction(s))

    def test_only_special_chars(self):
        s = "\n\r\t\n\n"
        self.assertTrue(not get_instruction(s))

    def test_instruction_with_comment(self):
        s = "ADD R1 R2     # Adds registers R1 and R2  \n"
        expected = ["ADD", "R1", "R2"]
        self.assertListEqual(get_instruction(s), expected)

    def test_instruction_with_comment_partway(self):
        s = "\tSUB R5 R1#0 This is a comment partway!\n"
        expected = ["SUB", "R5", "R1"]
        self.assertListEqual(get_instruction(s), expected)

    def test_commented_instruction(self):
        s = "\t\t # XOR R1 9083"
        self.assertTrue(not get_instruction(s))

    def test_only_instruction(self):
        s = "FETCH R4 ABCD"
        expected = ["FETCH", "R4", "ABCD"]

    def test_instruction_with_trailing_and_leading_whitespace(self):
        s = "      MOV R4 R1        "

if __name__ == "__main__":
    unittest.main()
    