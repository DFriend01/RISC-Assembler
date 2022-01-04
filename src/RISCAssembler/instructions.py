from .InstructionTuples import Instruction

INSTRUCTIONS_WITH_LITERALS = {
    "MOV"     : Instruction("0001", "00000", "000", 2),
    "MOVE"    : Instruction("0001", "00000", "001", 2),
    "MOVNE"   : Instruction("0001", "00000", "010", 2),
    "MOVC"    : Instruction("0001", "00000", "011", 2),
    "MOVNC"   : Instruction("0001", "00000", "100", 2),
    "MOVL"   : Instruction("0001", "00000", "101", 2),
    "MOVG"   : Instruction("0001", "00000", "110", 2),

    "ADD"     : Instruction("0010", "00000", "010", 2),
    "ADDC"    : Instruction("0010", "00001", "011", 2),
    "AND"     : Instruction("0010", "00010", "010", 2),
    "CMP"     : Instruction("0010", "00011", "000", 2),
    "MVN"     : Instruction("0010", "00100", "010", 2),
    "NOT"     : Instruction("0010", "00101", "010", 2),
    "OR"      : Instruction("0010", "00110", "010", 2),
    "SUB"     : Instruction("0010", "00111", "010", 2),
    "SUBC"    : Instruction("0010", "01000", "011", 2),
    "TEST"    : Instruction("0010", "01001", "000", 2),
    "XOR"     : Instruction("0010", "01010", "010", 2),

    "JMP"     : Instruction("0011", "00000", "000", 1),
    "JE"      : Instruction("0011", "00000", "001", 1),
    "JNE"     : Instruction("0011", "00000", "010", 1),
    "JL"     : Instruction("0011", "00000", "101", 1),
    "JG"     : Instruction("0011", "00000", "110", 1),

    "FETCH"   : Instruction("0101", "00001", "000", 2),
    "STORE"   : Instruction("0101", "00010", "000", 2),

    "CALL"    : Instruction("0110", "00000", "000", 1)
}

INSTRUCTIONS_WITH_REGISTERS = {
    "MOV"     : Instruction("0001", "10000", "000", 2),
    "MOVE"    : Instruction("0001", "10000", "001", 2),
    "MOVNE"   : Instruction("0001", "10000", "010", 2),
    "MOVC"    : Instruction("0001", "10000", "011", 2),
    "MOVNC"   : Instruction("0001", "10000", "100", 2),
    "MOVL"   : Instruction("0001", "10000", "101", 2),
    "MOVG"   : Instruction("0001", "10000", "110", 2),

    "ADD"     : Instruction("0010", "10000", "010", 2),
    "ADDC"    : Instruction("0010", "10001", "011", 2),
    "AND"     : Instruction("0010", "10010", "010", 2),
    "CMP"     : Instruction("0010", "10011", "000", 2),
    "MVN"     : Instruction("0010", "10100", "010", 2),
    "NOT"     : Instruction("0010", "10101", "010", 2),
    "OR"      : Instruction("0010", "10110", "010", 2),
    "SUB"     : Instruction("0010", "10111", "010", 2),
    "SUBC"    : Instruction("0010", "11000", "011", 2),
    "TEST"    : Instruction("0010", "11001", "000", 2),
    "XOR"     : Instruction("0010", "11010", "010", 2),
    "SL0"     : Instruction("0010", "11011", "010", 1),
    "SL1"     : Instruction("0010", "11100", "010", 1),
    "SR0"     : Instruction("0010", "11101", "010", 1),
    "SR1"     : Instruction("0010", "11110", "010", 1),

    "JMP"     : Instruction("0011", "10000", "000", 1),
    "JE"      : Instruction("0011", "10000", "001", 1),
    "JNE"     : Instruction("0011", "10000", "010", 1),
    "JL"     : Instruction("0011", "10000", "101", 1),
    "JG"     : Instruction("0011", "10000", "110", 1),

    "FETCH"   : Instruction("0101", "10001", "000", 2),
    "STORE"   : Instruction("0101", "10010", "000", 2)
}

SPEICAL_INSTRUCTIONS = {
    "HALT"    : Instruction("0111", "00000", "000", 0),
    "NOP"     : Instruction("0000", "00000", "000", 0),
    "RETURN"  : Instruction("0110", "00001", "000", 0)
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
    "R9" : "1001",
    "SP" : "1010"
}
