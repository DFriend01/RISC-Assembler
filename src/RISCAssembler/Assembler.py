import os
import re

from .ErrorCheck import ErrorCheck
from .InstructionParser import InstructionParser

def get_file_extension(file):
    return os.path.splitext(file)[1]

class Assembler:

    @staticmethod
    def compile(infilename, outfilename, safe_mode=False, output_binary=False):
        if os.path.isdir(infilename):
            raise IsADirectoryError(f"{infilename} should be a text file, not a directory")
        if not os.path.exists(infilename):
            raise FileNotFoundError(f"{infilename} does not exist")
        if os.path.isdir(outfilename):
            raise IsADirectoryError(f"{outfilename} should be a text file, not a directory")
        if (safe_mode) and (os.path.exists(outfilename)):
            raise FileExistsError(f"{outfilename} exists. Cannot overwrite existing files since -s flag is set")
        if get_file_extension(infilename) != ".txt":
            raise ValueError(f"{infilename} should be a text file")
        if get_file_extension(outfilename) != ".txt":
            raise ValueError(f"{outfilename} should be a text file")
        if infilename == outfilename:
            raise OSError("Input and output files must be named differently")

        instructions, constants, labels = Assembler.scan_source_file(infilename)
        encodings = []

        for linenumber, instruction in instructions:
            instr = InstructionParser.parse(instruction, linenumber, output_binary, labels, constants)
            if instr is not None:
                encodings.append(instr + "\n")

        if (not os.path.exists(os.path.dirname(outfilename))) and (os.path.dirname(outfilename) != ""):
            os.makedirs(os.path.dirname(outfilename))

        outfile = open(outfilename, "w")
        outfile.writelines(encodings)
        outfile.close()

    @staticmethod
    def get_instruction(line):
        return re.sub("#.*$", "", line).strip().upper().split()

    @staticmethod
    def scan_source_file(infilename):
        instructions = []
        constants = {}
        labels = {}

        infile = open(infilename, "r")
        Lines = infile.readlines()
        infile.close()

        for linenumber, line in enumerate(Lines):
            parsed_line = Assembler.get_instruction(line)
            
            if parsed_line:
                if Assembler.line_has_label(parsed_line):
                    ErrorCheck.validLabel(parsed_line[0], linenumber, line, labels.keys())
                    labels[Assembler.get_label_name(parsed_line[0])] = str(hex(len(instructions)))
                     
                    # Check for constant or instruction
                    if (len(parsed_line) > 1):
                        if Assembler.line_has_constant(parsed_line[1:]):
                            ErrorCheck.validConstant(parsed_line[1:], linenumber, line, constants.keys())
                            constants[Assembler.get_const_name(parsed_line[1:])] = Assembler.get_const_value(parsed_line[1:])
                        else:
                            instructions.append((linenumber + 1, parsed_line[1:]))

                elif Assembler.line_has_constant(parsed_line):
                    ErrorCheck.validConstant(parsed_line, linenumber, line, constants.keys())
                    constants[Assembler.get_const_name(parsed_line)] = Assembler.get_const_value(parsed_line)

                else:
                    instructions.append((linenumber + 1, parsed_line))

        return instructions, constants, labels   


    @staticmethod
    def line_has_label(parsed_line):
        return parsed_line[0][-1] == ":"

    @staticmethod
    def get_label_name(label):
        return label[:-1]

    @staticmethod
    def line_has_constant(parsed_line):
        return parsed_line[0] == "CONSTANT"

    @staticmethod
    def get_const_name(parsed_line):
        return parsed_line[1]

    @staticmethod
    def get_const_value(parsed_line):
        return parsed_line[2]

                    


