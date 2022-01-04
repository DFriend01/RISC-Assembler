from . import instructions
from .SyntaxError import AssemblerSyntaxError
from . import errorcodes

MAXNIBBLES = 2

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

        num = num.lstrip("0")
        if(not num):
            num = "0"

        if (len(num) > MAXNIBBLES):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BIG_LITERAL)
        
    @staticmethod
    def validRegister(register, linenumber, line):
        if(not register in instructions.REGISTERS):
            raise AssemblerSyntaxError(linenumber, line, errorcodes.BAD_REGISTER)