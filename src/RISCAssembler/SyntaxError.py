import re
from . import instructions
from . import errorcodes

def get_instruction(line):
        return re.sub("#.*$", "", line).strip().upper().split()

class SyntaxError(Exception):

    def __init__(self, linenumber=0, line="", errorcode=errorcodes.UNKNOWN_ERROR):
        self.message = SyntaxError.get_message(linenumber, line, errorcode)
        super().__init__(self.message)

    def __str__(self):
        return self.message

    @staticmethod
    def get_message(linenumber, line, errorcode):
        instruction = get_instruction(line)
        name = instruction[0]
        args = instruction[1:] if len(instruction) > 1 else []
        message = f"SYNTAX ERROR on Line {linenumber}: " + line + "\n"

        if (errorcode == errorcodes.UNDEFINED_INSTRUCTION):
            message += "Undefined instruction " + name
        elif (errorcode == errorcodes.INCORRECT_NARGS):
            if name in instructions.INSTRUCTIONS_WITH_REGISTERS:
                nargs = instructions.INSTRUCTIONS_WITH_REGISTERS[name].numargs
            else:
                nargs = instructions.SPEICAL_INSTRUCTIONS[name]
            message += "Instruction " + name + " expected " + str(nargs) \
                    +  " arguments, but " + str(len(args)) + " arguments were given"
        elif (errorcode == errorcodes.BAD_REGISTER):
            if (not instruction[1] in instructions.REGISTERS):
                badreg = instruction[1]
            else:
                badreg = instruction[2]
            message += badreg + " is expected to be a register R0 - R9"
        elif (errorcode == errorcodes.BAD_LITERAL):
            if (not instruction[1] in instructions.REGISTERS):
                badliteral = instruction[1]
            else:
                badliteral = instruction[2]
            message += badliteral + " is not a valid 2-byte hexadecimal value"
        elif (errorcode == errorcodes.BIG_LITERAL):
            if (not instruction[1] in instructions.REGISTERS):
                bigliteral = instruction[1]
            else:
                bigliteral = instruction[2]
            message += "Literal value should be 2 bytes, but " + bigliteral + " is too large"
        else:
            message += "An unknown error has occurred"
        return message
