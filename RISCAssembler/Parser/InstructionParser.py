import re
from RISCAssembler.Parser import instructions
from .SyntaxError import AssemblerSyntaxError
from . import errorcodes
from .ErrorCheck import ErrorCheck

INSTRUCTION_LENGTH_HEX = 4       # bytes

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

class InstructionParser:

    @staticmethod
    def parse(instruction, linenumber=0, output_binary=False, labels={}, constants={}):
        line = " ".join(instruction)
        if not instruction:
            return None
        else:
            return InstructionParser.__encode_instruction(instruction, line, linenumber, output_binary, labels, constants)

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
    def __contains_constant(instruction, constants):
        for i in instruction:
            if i in constants:
                return True
        return False
    
    @staticmethod
    def __contains_label(instruction, labels):
        for i in instruction:
            if i in labels:
                return True
        return False

    @staticmethod
    def __contains_only_registers(instruction):
        for i in instruction:
            if i not in instructions.REGISTERS:
                return False
        return True
    
    @staticmethod
    def __encode_instruction(instruction, line, linenumber, output_binary, labels, constants):

        # Check if instruction exists
        name = instruction[0]
        ErrorCheck.validInstructionName(name, linenumber, line)

        # Determine the kind of arguments the instruction has and decode any labels and constants
        has_literal = False
        actual_numargs = len(instruction) - 1

        if name in instructions.SPEICAL_INSTRUCTIONS:
            instruction_info = instructions.SPEICAL_INSTRUCTIONS[name]

        elif (InstructionParser.__contains_literal(instruction[1:])) and (name in instructions.INSTRUCTIONS_WITH_LITERALS):
            instruction_info = instructions.INSTRUCTIONS_WITH_LITERALS[name]
            has_literal = True

        elif (InstructionParser.__contains_constant(instruction[1:], constants)) and (name in instructions.INSTRUCTIONS_WITH_LITERALS):
            instruction_info = instructions.INSTRUCTIONS_WITH_LITERALS[name]
            has_literal = True
            if instruction[1] in constants:
                instruction[1] = constants[instruction[1]]
            elif instruction[2] in constants:
                instruction[2] = constants[instruction[2]]

        elif (InstructionParser.__contains_label(instruction[1:], labels)) and (name in instructions.INSTRUCTIONS_WITH_LITERALS):
            instruction_info = instructions.INSTRUCTIONS_WITH_LITERALS[name]
            ErrorCheck.validLabelForJumpAndCall(instruction_info.opcode, linenumber, line)
            has_literal = True
            instruction[1] = labels[instruction[1]]
            
        elif (name in instructions.INSTRUCTIONS_WITH_REGISTERS) and (InstructionParser.__contains_only_registers(instruction[1:])):
            instruction_info = instructions.INSTRUCTIONS_WITH_REGISTERS[name]

        else:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_ARGS)

        # Check that the number of arguments matches the expected number
        expected_numargs = instruction_info.numargs
        ErrorCheck.validNumberOfArguments(actual_numargs, expected_numargs, linenumber, line)

        # Get the instruction encoding
        encoding = ""

        # Assumes only HALT, NOP, or RETURN
        if actual_numargs == 0:
            encoding += instruction_info.opcode + instruction_info.op \
                     + instruction_info.cond + (20 * "0")

        elif actual_numargs == 1:

            # Single argument instruction that takes a literal
            if has_literal:
                ErrorCheck.validHex(instruction[1], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + (12 * "0") \
                         + binbits(int(instruction[1], 16), 8)

            # Single argument instruction that takes a register
            else:
                ErrorCheck.validRegister(instruction[1], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                         + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                         + (16 * "0")
            
        elif actual_numargs == 2:

            # If two arguments, the first one is always a register
            ErrorCheck.validRegister(instruction[1], linenumber, line)

            # If the second argument is a literal
            if has_literal:
                ErrorCheck.validHex(instruction[2], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                            + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                            + (8 * "0")  + binbits(int(instruction[2], 16), 8)

            # The second argument is a register
            else:
                ErrorCheck.validRegister(instruction[2], linenumber, line)
                encoding += instruction_info.opcode + instruction_info.op \
                             + instruction_info.cond + instructions.REGISTERS[instruction[1]] \
                             + instructions.REGISTERS[instruction[2]] + (12 * "0")

        # Arguments do not follow the instruction set
        else:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.UNKNOWN_ERROR)

        # Return the instruction encoding either in binary or hexadecimal
        if output_binary:
            return encoding
        else:
            return hexbytes(int(encoding, 2), INSTRUCTION_LENGTH_HEX)
