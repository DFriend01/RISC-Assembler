import re
from RISCAssembler.Parser import instructions
from . import errorcodes

def get_instruction(line):
        return re.sub("#.*$", "", line).strip().upper().split()

class AssemblerSyntaxError(Exception):

    def __init__(self, linenumber=0, line="", errorcode=errorcodes.UNKNOWN_ERROR):
        self.message = AssemblerSyntaxError.get_message(linenumber, line, errorcode)
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
            elif name in instructions.INSTRUCTIONS_WITH_LITERALS:
                nargs = instructions.INSTRUCTIONS_WITH_LITERALS[name].numargs
            elif name in instructions.SPEICAL_INSTRUCTIONS:
                nargs = instructions.SPEICAL_INSTRUCTIONS[name].numargs
            else: # A constant
                nargs = 2
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
            message += str(badliteral) + " is not a valid 1-byte hexadecimal value prefixed with 0x"

        elif (errorcode == errorcodes.BIG_LITERAL):
            if (not instruction[1] in instructions.REGISTERS):
                bigliteral = instruction[1]
            else:
                bigliteral = instruction[2]
            message += "Literal value should be 2 bytes, but " + str(bigliteral) + " is too large"

        elif (errorcode == errorcodes.EMPTY_LABEL):
            message += "Cannot have empty label"

        elif (errorcode == errorcodes.LABEL_WITH_KWD):
            message += "Label name cannot be a keyword"

        elif (errorcode == errorcodes.LABEL_EXISTS):
            message += "Cannot have duplicate labels"

        elif (errorcode == errorcodes.CONST_WITH_KWD):
            message += "Constant name cannot be a keyword"

        elif (errorcode == errorcodes.CONST_EXISTS):
            message += "Cannot have duplicate constant names"

        elif (errorcode == errorcodes.MISUSED_LABEL):
            message += "Labels can only be used for jump instructions and the CALL instruction"

        elif (errorcode == errorcodes.INVALID_NAME):
            message += "Label and constant names cannot start with a digit"

        elif (errorcode == errorcodes.BAD_ARGS):
            message += "Instruction contains bad arguments. If using constants or labels, be sure\n" \
                    +  "that it exists. If using literals, be sure that they are prefixed with 0x."

        else:
            message += "An unknown error has occurred"
            
        return message
