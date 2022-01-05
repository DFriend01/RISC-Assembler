from collections import namedtuple

Instruction = namedtuple("Instruction", ["opcode", "op", "cond", "numargs"])
