from RISCAssembler.Parser import instructions
from .SyntaxError import AssemblerSyntaxError
from . import errorcodes

MAXNIBBLES = 2
PREFIX_LEN = 2
CONSTANT_NARGS = 2
LITERAL_PREFIX = "0x"
NEG_SIGN = "-"
JMP_OPCODE = "0011"
CALL_OPCODE = "0110"

class ErrorCheck:

    @staticmethod
    def validInstructionName(name, linenumber, line):
        if (not name in instructions.INSTRUCTIONS_WITH_REGISTERS) and \
            (not name in instructions.SPEICAL_INSTRUCTIONS) and \
             (not name in instructions.INSTRUCTIONS_WITH_LITERALS):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.UNDEFINED_INSTRUCTION)

    @staticmethod
    def validNumberOfArguments(actual_numargs, expected_numargs, linenumber, line):
        if actual_numargs != expected_numargs:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.INCORRECT_NARGS)

    @staticmethod
    def validHex(x, linenumber=0, line=""):
        
        # Check if hex value is formatted correctly
        hexlower = x.lower()
        if (hexlower[0] == NEG_SIGN) or (len(hexlower) < PREFIX_LEN + 1) or (hexlower[:2] != LITERAL_PREFIX):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_LITERAL)
        
        # Check if the hex value is valid
        num = hexlower.split("x")[1]
        try:
            int(num, 16)
        except:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_LITERAL)

        # Ignore leading zeroes
        num = num.lstrip("0")
        if(not num):
            num = "0"

        # Check if the hex value does not exceed 1 byte
        if (len(num) > MAXNIBBLES):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BIG_LITERAL)
        
    @staticmethod
    def validRegister(register, linenumber, line):
        if(not register in instructions.REGISTERS):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_REGISTER)

    @staticmethod
    def validLabel(label, linenumber, line, existing_labels):
        if len(label) == 1:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.EMPTY_LABEL)

        keywords = list(instructions.INSTRUCTIONS_WITH_REGISTERS.keys())\
                 + list(instructions.INSTRUCTIONS_WITH_LITERALS.keys()) \
                 + list(instructions.REGISTERS.keys())
        name = label[:-1]

        if name[0].isdigit():
            raise AssemblerSyntaxError(linenumber, line, errorcodes.INVALID_NAME)
        if name in keywords:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.LABEL_WITH_KWD)
        if name in existing_labels:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.LABEL_EXISTS)

    @staticmethod
    def validConstant(parsed_line, linenumber, line, existing_consts):
        if len(parsed_line) - 1 != CONSTANT_NARGS:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.INCORRECT_NARGS)

        name = parsed_line[1]
        value = parsed_line[2]

        ErrorCheck.validHex(value, linenumber, line)
        keywords = list(instructions.INSTRUCTIONS_WITH_REGISTERS.keys()) \
                 + list(instructions.INSTRUCTIONS_WITH_LITERALS.keys()) \
                 + list(instructions.REGISTERS.keys())

        if name[0].isdigit():
            raise AssemblerSyntaxError(linenumber, line, errorcodes.INVALID_NAME)
        if name in keywords:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.CONST_WITH_KWD)
        if name in existing_consts:
            raise AssemblerSyntaxError(linenumber, line, errorcodes.CONST_EXISTS)

    @staticmethod
    def validLabelForJumpAndCall(opcode, linenumber, line):
        if (opcode != JMP_OPCODE) and (opcode != CALL_OPCODE):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.MISUSED_LABEL)
