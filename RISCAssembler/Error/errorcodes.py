UNKNOWN_ERROR = -1              # Unknown error occurred
UNDEFINED_INSTRUCTION = 0       # Undefined instruction
INCORRECT_NARGS = 1             # Incorrect number of args for an instruction
BAD_REGISTER = 2                # Expected a register but was something else
BAD_LITERAL = 3                 # Literal not formatted properly
BIG_LITERAL = 4                 # Literal exceeds 1 byte
EMPTY_LABEL = 5                 # Label with no name (only a :)
LABEL_WITH_KWD = 6              # Label name is a keyword
LABEL_EXISTS = 7                # Label was decalred twice
CONST_WITH_KWD = 8              # Constant name is a keyword
CONST_EXISTS = 9                # Constant was declared twice
MISUSED_LABEL = 10              # A label was used for an instruction other than a jump or CALL
INVALID_NAME = 11               # Bad label or constant name (starts with a digit)
BAD_ARGS = 12                   # Instruction arguments do not follow the instruction set
