import unittest
from src.RISCAssembler.InstructionParser import InstructionParser

class TestInstructionParser(unittest.TestCase):

    def test_basic_instruction(self):
        instruction = "add r1 r2"
        hex_encoding = "28212000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

if __name__ == "__main__":
    unittest.main()
