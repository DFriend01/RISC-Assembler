from collections import namedtuple

Instruction = namedtuple("Instruction", ["opcode", "op", "cond", "numargs"])
ALUInstruction = namedtuple("ALUInstruction", ["opcode", "op", "writeback", "carry", "numargs"])
