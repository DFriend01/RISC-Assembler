import unittest
import os
from src.RISCAssembler.Assembler import Assembler

class TestPrecompilationScan(unittest.TestCase):

    def test_simple_labels(self):
        instructions_expected = [
            (3,  ["MOV", "R1", "R2"]),
            (5,  ["ADD", "R1", "1"]),
            (6,  ["CMP", "R1", "R2"]),
            (12, ["XOR", "R4", "R9"])
        ]

        labels_expected = {
            "FOO"   : "0x0",
            "BAR"   : "0x1",
            "SILLY" : "0x3",
            "FUNNY" : "0x3"
        }

        constants_expected = {}

        instructions_actual, constants_actual, labels_actual = Assembler.scan_source_file(
            os.path.join("test", "testcode", "precompilation_scanning_tests", "simple_label_test.txt")
        )

        self.assertListEqual(instructions_actual, instructions_expected)
        self.assertDictEqual(labels_actual, labels_expected)
        self.assertDictEqual(constants_actual, constants_expected)

    def test_simple_constants(self):
        instructions_expected = [
            (5, ["MOV", "R8", "R3"])
        ]

        labels_expected = {}

        constants_expected = {
            "ZERO" : "0",
            "FOO"  : "0X11",
            "BAR"  : "BB"
        }

        instructions_actual, constants_actual, labels_actual = Assembler.scan_source_file(
            os.path.join("test", "testcode", "precompilation_scanning_tests", "simple_constant_test.txt")
        )

        self.assertListEqual(instructions_actual, instructions_expected)
        self.assertDictEqual(labels_actual, labels_expected)
        self.assertDictEqual(constants_actual, constants_expected)

    def test_no_labels_and_constants(self):
        instructions_expected = [
            (3,  ["MOVE", "R4", "0X12"]),
            (5,  ["SUB", "R1", "R4"]),
            (6,  ["MOVG", "R3", "R5"]),
            (10, ["TEST", "R3", "R1"])
        ]

        labels_expected = {}

        constants_expected = {}

        instructions_actual, constants_actual, labels_actual = Assembler.scan_source_file(
            os.path.join("test", "testcode", "precompilation_scanning_tests", "no_labels_or_constants.txt")
        )

        self.assertListEqual(instructions_actual, instructions_expected)
        self.assertDictEqual(labels_actual, labels_expected)
        self.assertDictEqual(constants_actual, constants_expected)

    def test_labels_and_constants(self):
        instructions_expected = [
            (5,  ["MOV", "R0", "0"]),
            (6,  ["MOV", "R1", "1"]),
            (7,  ["MOV", "R2", "2"]),
            (13, ["ADD", "R0", "0XA"]),
            (14, ["SUB", "R1", "R0"]),
            (15, ["CMP", "R0", "R2"])
        ]

        labels_expected = {
            "START" : "0x0",
            "MATH"  : "0x3",
            "ARITHMETIC" : "0x3"
        }

        constants_expected = {
            "FOO" : "0X55",
            "BAR" : "0"
        }

        instructions_actual, constants_actual, labels_actual = Assembler.scan_source_file(
            os.path.join("test", "testcode", "precompilation_scanning_tests", "labels_and_constants.txt")
        )

        self.assertListEqual(instructions_actual, instructions_expected)
        self.assertDictEqual(labels_actual, labels_expected)
        self.assertDictEqual(constants_actual, constants_expected)


