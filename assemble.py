import os
import sys
import argparse
import src.RISCAssembler.Assembler as asm

DEBUG = False

if not DEBUG:
    sys.tracebacklimit = 0

# Define argument parser
parser = argparse.ArgumentParser(description='RISC Assembler')
parser.add_argument('-i', '--input-path', help='Input path to assembly text file')
parser.add_argument('-o', '--output-path', help='Output path to write to text file')
parser.add_argument('-s', '--safe-mode', help='If outfile already exists, do not overwrite it', 
                    action='store_true', required=False)
parser.add_argument('-b', '--binary', help='Output binary instruction encodings',
                    action='store_true', required=False)

# Extract arguments
args = parser.parse_args()
infilename = args.input_path
outfilename = args.output_path
safe_mode = args.safe_mode
output_binary = args.binary

# Compile the assembly code
asm.Assembler.compile(infilename, outfilename, safe_mode, output_binary)
