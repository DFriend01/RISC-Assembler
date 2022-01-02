import unittest
from src.RISCAssembler.InstructionParser import InstructionParser
from src.RISCAssembler.SyntaxError import SyntaxError

class TestInstructionEncodings(unittest.TestCase):

    def test_halt(self):
        instruction = "HALT"
        hex_encoding = "70000000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_nop(self):
        instruction = "nop"
        hex_encoding = "00000000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mov_with_register(self):
        instruction = "mov r2 r3"
        hex_encoding = "18023000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_move_with_register(self):
        instruction = "move r2 r3"
        hex_encoding = "18123000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movne_with_register(self):
        instruction = "movne r2 r3"
        hex_encoding = "18223000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movc_with_register(self):
        instruction = "movc r2 r3"
        hex_encoding = "18323000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movnc_with_register(self):
        instruction = "movnc r2 r3"
        hex_encoding = "18423000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movle_with_register(self):
        instruction = "movle r2 r3"
        hex_encoding = "18523000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movge_with_register(self):
        instruction = "movge r2 r3"
        hex_encoding = "18623000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)
 
    def test_add_with_register(self):
        instruction = "add r1 r2"
        hex_encoding = "28212000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_addc_with_register(self):
        instruction = "addc r3 r3"
        hex_encoding = "28b33000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_and_with_register(self):
        instruction = "AND R5 R3"
        hex_encoding = "29253000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_cmp_with_register(self):
        instruction = "cmp R0 r8"
        hex_encoding = "29808000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mvn_with_register(self):
        instruction = "mvn r2 r7"
        hex_encoding = "2a227000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_not_with_register(self):
        instruction = "NOT R5 R2"
        hex_encoding = "2aa52000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_or_with_register(self):
        instruction = "or r9 r6"
        hex_encoding = "2b296000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sub_with_register(self):
        instruction = "sub r4 r5"
        hex_encoding = "2ba45000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_subc_with_register(self):
        instruction = "subc r3 r3"
        hex_encoding = "2c333000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_test_with_register(self):
        instruction = "test r2 r1"
        hex_encoding = "2c821000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_xor_with_register(self):
        instruction = "xor r0 r8"
        hex_encoding = "2d208000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sl0(self):
        instruction = "sl0 r1"
        hex_encoding = "2da10000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sl1(self):
        instruction = "sl1 r1"
        hex_encoding = "2e210000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sr0(self):
        instruction = "sr0 r1"
        hex_encoding = "2ea10000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sr1(self):
        instruction = "sr1 r1"
        hex_encoding = "2f210000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jmp_with_register(self):
        instruction = "jmp r5"
        hex_encoding = "38050000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_je_with_register(self):
        instruction = "je r5"
        hex_encoding = "38150000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jne_with_register(self):
        instruction = "jne r5"
        hex_encoding = "38250000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jle_with_register(self):
        instruction = "jle r5"
        hex_encoding = "38550000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jge_with_register(self):
        instruction = "jge r5"
        hex_encoding = "38650000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_fetch_with_register(self):
        instruction = "fetch r9 r8"
        hex_encoding = "58898000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_store_with_register(self):
        instruction = "store r9 r8"
        hex_encoding = "59098000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mov_with_literal(self):
        instruction = "mov r2 AB"
        hex_encoding = "100200ab"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_move_with_literal(self):
        instruction = "move r2 ff"
        hex_encoding = "101200ff"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movne_with_literal(self):
        instruction = "movne r2 71ED"
        hex_encoding = "102271ed"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movc_with_literal(self):
        instruction = "movc r2 0x99"
        hex_encoding = "10320099"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movnc_with_literal(self):
        instruction = "movnc r2 0"
        hex_encoding = "10420000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movle_with_literal(self):
        instruction = "movle r2 000"
        hex_encoding = "10520000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movge_with_literal(self):
        instruction = "movge r2 0x0065"
        hex_encoding = "10620065"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)
 
    def test_add_with_literal(self):
        instruction = "add r1 0XAA"
        hex_encoding = "202100aa"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_addc_with_literal(self):
        instruction = "addc r3 78F"
        hex_encoding = "20b3078f"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_and_with_literal(self):
        instruction = "AND R5 1c12"
        hex_encoding = "21251c12"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_cmp_with_literal(self):
        instruction = "cmp R0 16"
        hex_encoding = "21800016"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mvn_with_literal(self):
        instruction = "mvn r2 2307"
        hex_encoding = "22222307"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_not_with_literal(self):
        instruction = "NOT R5 1"
        hex_encoding = "22a50001"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_or_with_literal(self):
        instruction = "or r9 010"
        hex_encoding = "23290010"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sub_with_literal(self):
        instruction = "sub r4 7"
        hex_encoding = "23a40007"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_subc_with_literal(self):
        instruction = "subc r3 8"
        hex_encoding = "24330008"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_test_with_literal(self):
        instruction = "test r2 112"
        hex_encoding = "24820112"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_xor_with_literal(self):
        instruction = "xor r0 0x0"
        hex_encoding = "25200000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jmp_with_literal(self):
        instruction = "jmp 14"
        hex_encoding = "30000014"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_je_with_literal(self):
        instruction = "je 0"
        hex_encoding = "30100000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jne_with_literal(self):
        instruction = "jne 5"
        hex_encoding = "30200005"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jle_with_literal(self):
        instruction = "jle 0x112"
        hex_encoding = "30500112"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jge_with_literal(self):
        instruction = "jge 1000"
        hex_encoding = "30601000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_fetch_with_literal(self):
        instruction = "fetch r9 0x99"
        hex_encoding = "50899900"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_store_with_literal(self):
        instruction = "store r9 36"
        hex_encoding = "51093600"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_comment(self):
        instruction = "# This is a comment. There should be no instruction output"
        self.assertTrue(InstructionParser.parse(instruction) is None)
 

class TestBadInstructions(unittest.TestCase):

    def test_nonexistent_instruction(self):
        with self.assertRaises(SyntaxError):
            instruction = "MULT R1 R2"
            InstructionParser.parse(instruction)

    def test_too_many_arguments(self):
        with self.assertRaises(SyntaxError):
            instruction = "ADD R1 R2 R3"
            InstructionParser.parse(instruction)

    def test_too_little_arguments(self):
        with self.assertRaises(SyntaxError):
            instruction = "FETCH R5"
            InstructionParser.parse(instruction)

    def test_bad_register(self):
        with self.assertRaises(SyntaxError):
            instruction = "add r10 r9"
            InstructionParser.parse(instruction)

    def test_bad_register_with_literal(self):
        with self.assertRaises(SyntaxError):
            instruction = "FETCH R12 0x11"
            InstructionParser.parse(instruction)

    def test_invalid_literal_1(self):
        with self.assertRaises(SyntaxError):
            instruction = "JMP 0x"
            InstructionParser.parse(instruction)

    def test_invalid_literal_2(self):
        with self.assertRaises(SyntaxError):
            instruction = "JNE 0xgff0"
            InstructionParser.parse(instruction)

    def test_literal_too_large(self):
        with self.assertRaises(SyntaxError):
            instruction = "ADD R1 0x22100"
            InstructionParser.parse(instruction)

if __name__ == "__main__":
    unittest.main()
