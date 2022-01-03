import os
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

        instructions = []
        Lines = open(infilename, "r").readlines()

        for linenumber, line in enumerate(Lines):
            instr = InstructionParser.parse(line, linenumber + 1, output_binary)
            if instr is not None:
                instructions.append(instr + "\n")

        if (not os.path.exists(os.path.dirname(outfilename))) and (os.path.dirname != ""):
            os.makedirs(os.path.dirname(outfilename))

        outfile = open(outfilename, "w")
        outfile.writelines(instructions)
        outfile.close()
