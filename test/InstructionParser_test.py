import unittest
from src.RISCAssembler.InstructionParser import InstructionParser

class TestInstructionEncodings(unittest.TestCase):

    def test_halt(self):
        instruction = ["HALT"]
        hex_encoding = "70000000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_nop(self):
        instruction = ["NOP"]
        hex_encoding = "00000000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mov_with_register(self):
        instruction = ["MOV", "R2", "R3"]
        hex_encoding = "18023000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_move_with_register(self):
        instruction = ["MOVE", "R2", "R3"]
        hex_encoding = "18123000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movne_with_register(self):
        instruction = ["MOVNE", "R2", "R3"]
        hex_encoding = "18223000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movc_with_register(self):
        instruction = ["MOVC", "R2", "R3"]
        hex_encoding = "18323000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movnc_with_register(self):
        instruction = ["MOVNC", "R2", "R3"]
        hex_encoding = "18423000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movl_with_register(self):
        instruction = ["MOVL", "R2", "R3"]
        hex_encoding = "18523000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movg_with_register(self):
        instruction = ["MOVG", "R2", "R3"]
        hex_encoding = "18623000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)
 
    def test_add_with_register(self):
        instruction = ["ADD", "R1", "R2"]
        hex_encoding = "28212000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_addc_with_register(self):
        instruction = ["ADDC", "R3", "R3"]
        hex_encoding = "28b33000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_and_with_register(self):
        instruction = ["AND", "R5", "R3"]
        hex_encoding = "29253000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_cmp_with_register(self):
        instruction = ["CMP", "R0", "R8"]
        hex_encoding = "29808000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mvn_with_register(self):
        instruction = ["MVN", "R2", "R7"]
        hex_encoding = "2a227000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_not_with_register(self):
        instruction = ["NOT", "R5", "R2"]
        hex_encoding = "2aa52000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_or_with_register(self):
        instruction = ["OR", "R9", "R6"]
        hex_encoding = "2b296000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sub_with_register(self):
        instruction = ["SUB", "R4", "R5"]
        hex_encoding = "2ba45000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_subc_with_register(self):
        instruction = ["SUBC", "R3", "R3"]
        hex_encoding = "2c333000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_test_with_register(self):
        instruction = ["TEST", "R2", "R1"]
        hex_encoding = "2c821000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_xor_with_register(self):
        instruction = ["XOR", "R0", "R8"]
        hex_encoding = "2d208000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sl0(self):
        instruction = ["SL0", "R1"]
        hex_encoding = "2da10000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sl1(self):
        instruction = ["SL1", "R1"]
        hex_encoding = "2e210000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sr0(self):
        instruction = ["SR0", "R1"]
        hex_encoding = "2ea10000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sr1(self):
        instruction = ["SR1", "R1"]
        hex_encoding = "2f210000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jmp_with_register(self):
        instruction = ["JMP", "R5"]
        hex_encoding = "38050000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_je_with_register(self):
        instruction = ["JE", "R5"]
        hex_encoding = "38150000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jne_with_register(self):
        instruction = ["JNE", "R5"]
        hex_encoding = "38250000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jl_with_register(self):
        instruction = ["JL", "R5"]
        hex_encoding = "38550000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jg_with_register(self):
        instruction = ["JG", "R5"]
        hex_encoding = "38650000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_fetch_with_register(self):
        instruction = ["FETCH", "R9", "R8"]
        hex_encoding = "58898000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_store_with_register(self):
        instruction = ["STORE", "R9", "R8"]
        hex_encoding = "59098000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mov_with_literal(self):
        instruction = ["MOV", "R2", "AB"]
        hex_encoding = "100200ab"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_move_with_literal(self):
        instruction = ["MOVE", "R2", "FF"]
        hex_encoding = "101200ff"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movne_with_literal(self):
        instruction = ["MOVNE", "R2", "ED"]
        hex_encoding = "102200ed"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movc_with_literal(self):
        instruction = ["MOVC", "R2", "0X99"]
        hex_encoding = "10320099"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movnc_with_literal(self):
        instruction = ["MOVNC", "R2", "0"]
        hex_encoding = "10420000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movl_with_literal(self):
        instruction = ["MOVL", "R2", "000"]
        hex_encoding = "10520000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_movg_with_literal(self):
        instruction = ["MOVG", "R2", "0X0065"]
        hex_encoding = "10620065"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)
 
    def test_add_with_literal(self):
        instruction = ["ADD", "R1", "0XAA"]
        hex_encoding = "202100aa"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_addc_with_literal(self):
        instruction = ["ADDC", "R3", "8F"]
        hex_encoding = "20b3008f"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_and_with_literal(self):
        instruction = ["AND", "R5", "12"]
        hex_encoding = "21250012"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_cmp_with_literal(self):
        instruction = ["CMP", "R0", "16"]
        hex_encoding = "21800016"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_mvn_with_literal(self):
        instruction = ["MVN", "R2", "07"]
        hex_encoding = "22220007"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_not_with_literal(self):
        instruction = ["NOT", "R5", "1"]
        hex_encoding = "22a50001"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_or_with_literal(self):
        instruction = ["OR", "R9", "010"]
        hex_encoding = "23290010"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_sub_with_literal(self):
        instruction = ["SUB", "R4", "7"]
        hex_encoding = "23a40007"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_subc_with_literal(self):
        instruction = ["SUBC", "R3", "8"]
        hex_encoding = "24330008"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_test_with_literal(self):
        instruction = ["TEST", "R2", "12"]
        hex_encoding = "24820012"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_xor_with_literal(self):
        instruction = ["XOR", "R0", "0x0"]
        hex_encoding = "25200000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jmp_with_literal(self):
        instruction = ["JMP", "14"]
        hex_encoding = "30000014"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_je_with_literal(self):
        instruction = ["JE", "0"]
        hex_encoding = "30100000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jne_with_literal(self):
        instruction = ["JNE", "5"]
        hex_encoding = "30200005"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jl_with_literal(self):
        instruction = ["JL", "0x12"]
        hex_encoding = "30500012"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_jg_with_literal(self):
        instruction = ["JG", "10"]
        hex_encoding = "30600010"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_fetch_with_literal(self):
        instruction = ["FETCH", "R9", "0x99"]
        hex_encoding = "50890099"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_store_with_literal(self):
        instruction = ["STORE", "R9", "36"]
        hex_encoding = "51090036"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_call(self):
        instruction = ["CALL", "10"]
        hex_encoding = "60000010"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)

    def test_return(self):
        instruction = ["RETURN"]
        hex_encoding = "60800000"
        self.assertEqual(InstructionParser.parse(instruction), hex_encoding)


class TestInstructionsWithConstants(unittest.TestCase):

    def test_alu_instr(self):
        instruction = ["ADD", "R1", "VAR"]
        constants = {"VAR" : "0XAA"}
        hex_encoding = "202100aa"
        self.assertEqual(InstructionParser.parse(instruction=instruction, constants=constants), hex_encoding)

    def test_mov_instr(self):
        instruction = ["MOV", "R2", "FOO"]
        constants = {"FOO" : "CB", "BAR" : "0XDC"}
        hex_encoding = "100200cb"
        self.assertEqual(InstructionParser.parse(instruction=instruction, constants=constants), hex_encoding)

    def test_je_instr(self):
        instruction = ["JE", "BAR"]
        constants = {"FOO" : "CB", "BAR" : "0XDC"}
        hex_encoding = "301000dc"
        self.assertEqual(InstructionParser.parse(instruction=instruction, constants=constants), hex_encoding)

    def test_fetch_instr(self):
        instruction = ["FETCH", "R9", "X"]
        constants = {"FOO" : "CB", "X" : "0X99"}
        hex_encoding = "50890099"
        self.assertEqual(InstructionParser.parse(instruction=instruction, constants=constants), hex_encoding)

    def test_call_instr(self):
        instruction = ["CALL", "FOO"]
        constants = {"FOO" : "0X10"}
        hex_encoding = "60000010"
        self.assertEqual(InstructionParser.parse(instruction=instruction, constants=constants), hex_encoding)

class TestInstructionsWithLabels(unittest.TestCase):

    def test_jmp_with_label(self):
        instruction = ["JMP", "HELLO"]
        labels = {"HELLO" : "0x14"}
        hex_encoding = "30000014"
        self.assertEqual(InstructionParser.parse(instruction=instruction, labels=labels), hex_encoding)

    def test_call_with_label(self):
        instruction = ["CALL", "FOO"]
        labels = {"FOO" : "0X19"}
        hex_encoding = "60000019"
        self.assertEqual(InstructionParser.parse(instruction=instruction, labels=labels), hex_encoding)


if __name__ == "__main__":
    unittest.main()
