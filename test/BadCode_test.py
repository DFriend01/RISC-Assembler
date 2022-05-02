import unittest
import os
from RISCAssembler.Assembler import Assembler
from RISCAssembler.Parser.InstructionParser import InstructionParser
from RISCAssembler.SyntaxError import AssemblerSyntaxError

FILEPATH = os.path.dirname(__file__)


class TestBadInstructions(unittest.TestCase):

    def test_nonexistent_instruction(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["MULT", "R1", "R2"]
            InstructionParser.parse(instruction)

    def test_jump_with_register(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["JMP", "R1"]
            InstructionParser.parse(instruction)

    def test_too_many_arguments(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["ADD", "R1", "R2", "R3"]
            InstructionParser.parse(instruction)

    def test_too_little_arguments(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["FETCH", "R5"]
            InstructionParser.parse(instruction)

    def test_bad_register(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["ADD", "R10", "R9"]
            InstructionParser.parse(instruction)

    def test_bad_register_with_literal(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["FETCH", "R12", "0x11"]
            InstructionParser.parse(instruction)

    def test_invalid_literal_1(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["JMP", "0x"]
            InstructionParser.parse(instruction)

    def test_invalid_literal_2(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["JNE", "0xgf"]
            InstructionParser.parse(instruction)

    def test_literal_too_large(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["ADD", "R1", "0x22100"]
            InstructionParser.parse(instruction)

    def test_literal_without_prefix(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["ADD", "R1", "22"]
            InstructionParser.parse(instruction)

    def test_negative_literal(self):
        with self.assertRaises(AssemblerSyntaxError):
            instruction = ["ADD", "R1", "-0x22"]
            InstructionParser.parse(instruction)


class TestBadLabels(unittest.TestCase):

    def test_empty_label(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "empty_label.txt"))

    def test_label_with_keyword(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "label_with_keyword.txt"))

    def test_empty_label_with_instruction(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "empty_label_with_instruction.txt"))

    def test_duplicate_labels(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "duplicate_labels.txt"))

    def test_numerical_label_name(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "label_start_with_digit.txt"))

    
class TestBadConstants(unittest.TestCase):

    def test_bad_constant_literal(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "bad_constant_literal.txt"))

    def test_constant_missing_args(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "constant_missing_args.txt"))

    def test_constant_with_keyword(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "constant_with_keyword.txt"))

    def test_duplicate_constant(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "duplicate_constant.txt"))

    def test_numerical_constant_name(self):
        with self.assertRaises(AssemblerSyntaxError):
            Assembler.scan_source_file(os.path.join(FILEPATH, "testcode", "error_checking_tests", "constant_start_with_digit.txt"))

if __name__ == "__main__":
    unittest.main()
    