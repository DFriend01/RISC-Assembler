import os
import sys
import src.RISCAssembler.Assembler as asm

DEBUG = False

if not DEBUG:
    sys.tracebacklimit = 0

HELP_CONTENT = "Usage: python3 assemble.py -i [INPUT PATH] -o [OUTPUT PATH] [OPTIONS]" + "\n" \
    + "Compiles an assembly file formatted as a text file (.txt)" + "\n" \
    + "Example: python3 assemble.py -i foo/input.txt -o bar/output.txt -s -b" + "\n" \
    + "The input assembly file must exist and must be a text file" + "\n\n" \
    + "    -i        Input path to assembly text file\n" \
    + "    -o        Output path to write to text file\n" \
    + "    -s        If output file already exists, do not overwrite it\n" \
    + "    -b        Output binary instruction encodings. By default, instruction encodings are in hexadecimal\n" \
    + "    --help    Display this message\n"

def get_input_path():
    try:
        idx = sys.argv.index("-i")
        if (idx == len(sys.argv) - 1):
            raise LookupError
        if (not os.path.exists(sys.argv[idx + 1])):
            raise OSError
        return sys.argv[idx + 1]
    except ValueError:
        print("The -i flag was not found")
        raise
    except LookupError:
        print("Input path not found after -i flag")
        raise
    except OSError:
        idx = sys.argv.index("-i")
        path = sys.argv[idx + 1]
        print(f"The input path {path} does not exist")
        raise

def get_output_path():
    try:
        idx = sys.argv.index("-o")
        if (idx == len(sys.argv) - 1):
            raise LookupError
        return sys.argv[idx + 1]
    except LookupError:
        print("Output path not found after -o flag")
        raise
    except ValueError:
        print("The -o flag was not found")
        raise

if "--help" in sys.argv:
    print(HELP_CONTENT)
else:
    infilename = get_input_path()
    outfilename = get_output_path()
    safe_mode = "-s" in sys.argv
    output_binary = "-b" in sys.argv
    asm.Assembler.compile(infilename, outfilename, safe_mode, output_binary)
