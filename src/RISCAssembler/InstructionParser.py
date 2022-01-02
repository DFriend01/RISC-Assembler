import re
from .InstructionTuples import Instruction
from .SyntaxError import SyntaxError
import pdb

REGLEN = 2
MINREG = 0
MAXREG = 9
MAXNIBBLES = 4
MEMORY_OPCODE = "101"
INSTRUCTION_LENGTH_BINARY = 32
INSTRUCTION_LENGTH_HEX = 4 #bytes

INSTRUCTIONS_WITH_LITERALS = {
    "MOV"     : Instruction("001", "00000", "000", 2),
    "MOVE"    : Instruction("001", "00000", "001", 2),
    "MOVNE"   : Instruction("001", "00000", "010", 2),
    "MOVC"    : Instruction("001", "00000", "011", 2),
    "MOVNC"   : Instruction("001", "00000", "100", 2),
    "MOVLE"   : Instruction("001", "00000", "101", 2),
    "MOVGE"   : Instruction("001", "00000", "110", 2),

    "ADD"     : Instruction("010", "00000", "010", 2),
    "ADDC"    : Instruction("010", "00001", "011", 2),
    "AND"     : Instruction("010", "00010", "010", 2),
    "CMP"     : Instruction("010", "00011", "000", 2),
    "MVN"     : Instruction("010", "00100", "010", 2),
    "NOT"     : Instruction("010", "00101", "010", 2),
    "OR"      : Instruction("010", "00110", "010", 2),
    "SUB"     : Instruction("010", "00111", "010", 2),
    "SUBC"    : Instruction("010", "01000", "011", 2),
    "TEST"    : Instruction("010", "01001", "000", 2),
    "XOR"     : Instruction("010", "01010", "010", 2),

    "JMP"     : Instruction("011", "00000", "000", 1),
    "JE"      : Instruction("011", "00000", "001", 1),
    "JNE"     : Instruction("011", "00000", "010", 1),
    "JLE"     : Instruction("011", "00000", "101", 1),
    "JGE"     : Instruction("011", "00000", "110", 1),

    "FETCH"   : Instruction("101", "00001", "000", 2),
    "STORE"   : Instruction("101", "00010", "000", 2)
}

INSTRUCTIONS_WITH_REGISTERS = {
    "MOV"     : Instruction("001", "10000", "000", 2),
    "MOVE"    : Instruction("001", "10000", "001", 2),
    "MOVNE"   : Instruction("001", "10000", "010", 2),
    "MOVC"    : Instruction("001", "10000", "011", 2),
    "MOVNC"   : Instruction("001", "10000", "100", 2),
    "MOVLE"   : Instruction("001", "10000", "101", 2),
    "MOVGE"   : Instruction("001", "10000", "110", 2),

    "ADD"     : Instruction("010", "10000", "010", 2),
    "ADDC"    : Instruction("010", "10001", "011", 2),
    "AND"     : Instruction("010", "10010", "010", 2),
    "CMP"     : Instruction("010", "10011", "000", 2),
    "MVN"     : Instruction("010", "10100", "010", 2),
    "NOT"     : Instruction("010", "10101", "010", 2),
    "OR"      : Instruction("010", "10110", "010", 2),
    "SUB"     : Instruction("010", "10111", "010", 2),
    "SUBC"    : Instruction("010", "11000", "011", 2),
    "TEST"    : Instruction("010", "11001", "000", 2),
    "XOR"     : Instruction("010", "11010", "010", 2),
    "SL0"     : Instruction("010", "11011", "010", 1),
    "SL1"     : Instruction("010", "11100", "010", 1),
    "SR0"     : Instruction("010", "11101", "010", 1),
    "SR1"     : Instruction("010", "11110", "010", 1),

    "JMP"     : Instruction("011", "10000", "000", 1),
    "JE"      : Instruction("011", "10000", "001", 1),
    "JNE"     : Instruction("011", "10000", "010", 1),
    "JLE"     : Instruction("011", "10000", "101", 1),
    "JGE"     : Instruction("011", "10000", "110", 1),

    "FETCH"   : Instruction("101", "10001", "000", 2),
    "STORE"   : Instruction("101", "10010", "000", 2)
}

SPEICAL_INSTRUCTIONS = {
    "HALT"    : Instruction("111", "00000", "000", 0),
    "NOP"     : Instruction("000", "00000", "000", 0)
}

REGISTERS = {
    "R0" : "0000",
    "R1" : "0001",
    "R2" : "0010",
    "R3" : "0011",
    "R4" : "0100",
    "R5" : "0101",
    "R6" : "0110",
    "R7" : "0111",
    "R8" : "1000",
    "R9" : "1001"
}

def binbits(x, n):
    bits = bin(x).split('b')[1]

    if len(bits) < n:
        bits = '0' * (n - len(bits)) + bits
    return bits

def hexbytes(x, n):
    num_nibbles = 2 * n
    bytes = hex(x).lower().split('x')[1]

    if len(bytes) < num_nibbles:
        bytes = '0' * (num_nibbles - len(bytes)) + bytes
    return bytes

class ErrorCheck:

    @staticmethod
    def validInstructionName(name):
        if name in INSTRUCTIONS_WITH_REGISTERS:
            d = INSTRUCTIONS_WITH_LITERALS
        elif name in SPEICAL_INSTRUCTIONS:
            d = SPEICAL_INSTRUCTIONS
        else:
            raise SyntaxError()

    @staticmethod
    def validNumberOfArguments(actual_numargs, expected_numargs):
        if actual_numargs != expected_numargs:
            raise SyntaxError()

    @staticmethod
    def validHex(x):

        hexsplit = x.lower().split('x')
        num = hexsplit[0] if len(hexsplit) < 2 else hexsplit[1]
        try:
            int(num, 16)
            if (len(num) > MAXNIBBLES) or (x == "0x"):
                raise ValueError
        except:
            raise SyntaxError()

    @staticmethod
    def validRegister(register):
        if(not register in REGISTERS):
            raise SyntaxError()


class InstructionParser:

    @staticmethod
    def parse(line):
        instruction = InstructionParser.__get_instruction(line)

        if not instruction:
            return None
        else:
            return InstructionParser.__encode_instruction(instruction)

    @staticmethod
    def __get_instruction(line):
        return re.sub("#.*$", "", line).strip().upper().split()

    @staticmethod
    def __contains_literal(instruction):
        for i in instruction:
            try:
                ErrorCheck.validHex(i)
                return True
            except:
                continue
        return False
    
    @staticmethod
    def __encode_instruction(instruction):
        name = instruction[0]
        ErrorCheck.validInstructionName(name)

        actual_numargs = len(instruction) - 1
        if (actual_numargs == 0) and (name in SPEICAL_INSTRUCTIONS):
            instruction_info = SPEICAL_INSTRUCTIONS[name]
        elif (InstructionParser.__contains_literal(instruction[1:])) and (name in INSTRUCTIONS_WITH_LITERALS):
            instruction_info = INSTRUCTIONS_WITH_LITERALS[name]
        elif name in INSTRUCTIONS_WITH_REGISTERS:
            instruction_info = INSTRUCTIONS_WITH_REGISTERS[name]
        else:
            raise SyntaxError()

        expected_numargs = instruction_info.numargs
        ErrorCheck.validNumberOfArguments(actual_numargs, expected_numargs)

        encoding = ""

        # Assumes only HALT or NOP
        if actual_numargs == 0:
            encoding += instruction_info.opcode + instruction_info.op \
                     + instruction_info.cond + (20 * "0")
        elif actual_numargs == 1:
            # Single argument instruction that takes a literal
            try:
                ErrorCheck.validHex(instruction[1])
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + (4 * "0") \
                         + binbits(int(instruction[1], 16), 16)

            # Single argument instruction that takes a register
            except:
                ErrorCheck.validRegister(instruction[1])
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + REGISTERS[instruction[1]] \
                         + (16 * "0")
            
        elif actual_numargs == 2:
            ErrorCheck.validRegister(instruction[1])

            if instruction_info is INSTRUCTIONS_WITH_LITERALS[name]:
                ErrorCheck.validHex(instruction[2])
                if instruction_info.opcode == MEMORY_OPCODE:
                    encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + REGISTERS[instruction[1]] \
                             + binbits(int(instruction[2][-2:], 16), 8) + (8 * "0")
                else:
                    encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + REGISTERS[instruction[1]] \
                             + binbits(int(instruction[2], 16), 16)
            else:
                ErrorCheck.validRegister(instruction[2])
                encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + REGISTERS[instruction[1]] \
                             + REGISTERS[instruction[2]] + (12 * "0")
        else:
            raise SyntaxError()

        return hexbytes(int(encoding, 2), INSTRUCTION_LENGTH_HEX)

    


