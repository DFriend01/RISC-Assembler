import re
from . import instructions
from .SyntaxError import AssemblerSyntaxError
from . import errorcodes

REGLEN = 2
MINREG = 0
MAXREG = 9
MAXNIBBLES = 4
MEMORY_OPCODE = "0101"
INSTRUCTION_LENGTH_BINARY = 32
INSTRUCTION_LENGTH_HEX = 4 #bytes

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
    def validInstructionName(name, linenumber, line):
        if (not name in instructions.INSTRUCTIONS_WITH_REGISTERS) and (not name in instructions.SPEICAL_INSTRUCTIONS):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.UNDEFINED_INSTRUCTION)

    @staticmethod
    def validNumberOfArguments(actual_numargs, expected_numargs, linenumber, line):
        if actual_numargs != expected_numargs:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.INCORRECT_NARGS)

    @staticmethod
    def validHex(x, linenumber=0, line=""):

        hexsplit = x.lower().split('x')
        num = hexsplit[0] if len(hexsplit) < 2 else hexsplit[1]

        try:
            int(num, 16)
            if (x == "0x"):
                raise ValueError
        except:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_LITERAL)

        if (len(num) > MAXNIBBLES):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BIG_LITERAL)
        
    @staticmethod
    def validRegister(register, linenumber, line):
        if(not register in instructions.REGISTERS):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_REGISTER)


class InstructionParser:

    @staticmethod
    def parse(line, linenumber=0, output_binary=False):
        instruction = InstructionParser.__get_instruction(line)

        if not instruction:
            return None
        else:
            return InstructionParser.__encode_instruction(instruction, line, linenumber, output_binary)

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
    def __encode_instruction(instruction, line, linenumber, output_binary):
        name = instruction[0]
        ErrorCheck.validInstructionName(name, linenumber, line)

        has_literal = False

        actual_numargs = len(instruction) - 1
        if (actual_numargs == 0) and (name in instructions.SPEICAL_INSTRUCTIONS):
            instruction_info = instructions.SPEICAL_INSTRUCTIONS[name]
        elif (InstructionParser.__contains_literal(instruction[1:])) and (name in instructions.INSTRUCTIONS_WITH_LITERALS):
            instruction_info = instructions.INSTRUCTIONS_WITH_LITERALS[name]
            has_literal = True
        elif name in instructions.INSTRUCTIONS_WITH_REGISTERS:
            instruction_info = instructions.INSTRUCTIONS_WITH_REGISTERS[name]
        else:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.UNKNOWN_ERROR)

        expected_numargs = instruction_info.numargs
        ErrorCheck.validNumberOfArguments(actual_numargs, expected_numargs, linenumber, line)

        encoding = ""

        # Assumes only HALT or NOP
        if actual_numargs == 0:
            encoding += instruction_info.opcode + instruction_info.op \
                     + instruction_info.cond + (20 * "0")
        elif actual_numargs == 1:
            # Single argument instruction that takes a literal
            if has_literal:
                ErrorCheck.validHex(instruction[1], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + (4 * "0") \
                         + binbits(int(instruction[1], 16), 16)

            # Single argument instruction that takes a register
            else:
                ErrorCheck.validRegister(instruction[1], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                         + (16 * "0")
            
        elif actual_numargs == 2:
            ErrorCheck.validRegister(instruction[1], linenumber, line)

            if has_literal:
                ErrorCheck.validHex(instruction[2], linenumber, line)
                if instruction_info.opcode == MEMORY_OPCODE:
                    encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                             + binbits(int(instruction[2][-2:], 16), 8) + (8 * "0")
                else:
                    encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                             + binbits(int(instruction[2], 16), 16)
            else:
                ErrorCheck.validRegister(instruction[2], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                             + instructions.REGISTERS[instruction[2]] + (12 * "0")
        else:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.UNKNOWN_ERROR)

        if output_binary:
            return encoding
        else:
            return hexbytes(int(encoding, 2), INSTRUCTION_LENGTH_HEX)
