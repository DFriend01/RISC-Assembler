import os
from .InstructionParser import InstructionParser

def get_file_extension(file):
    return os.path.splitext(file)[1]

class Assembler:

    @staticmethod
    def compile(infilename, outfilename):
        if os.path.isdir(infilename):
            raise IsADirectoryError(f"{infilename} should be a text file, not a directory")
        if not os.path.exists(infilename):
            raise FileNotFoundError(f"{infilename} does not exist")
        if os.path.isdir(outfilename):
            raise IsADirectoryError(f"{outfilename} should be a text file, not a directory")
        if os.path.exists(outfilename):
            raise FileExistsError(f"{outfilename} exists. Cannot overwrite existing files")
        assert get_file_extension(infilename) == ".txt"
        assert get_file_extension(outfilename) == ".txt"

        instructions = []
        Lines = open(infilename, "r").readlines()

        for linenumber, line in enumerate(Lines):
            instr = InstructionParser.parse(line, linenumber + 1)
            if instr is not None:
                instructions.append(instr + "\n")

        outfile = open(outfilename, "w")
        outfile.writelines(instructions)
        outfile.close()
