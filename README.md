# RISC-Assembler

This is an assembler written in python that translates a custom assembly language into 32-bit binary instructions.

## Instruction Set

Refer to the [instruction set](https://github.com/DFriend01/RISC-Assembler/blob/main/docs/InstructionSet.pdf) to see which instructions are supported and how they function.

## Syntax Rules

- Instructions are **case insensitive** and indentation/extra spaces are ignored
- Valid registers are denoted as R0 through R9 (R0, R1, R2, ... R9)
- Literals cannot exceed 1 byte and must be expressed as hexadecimal values
  - Example: 0xCD, bd, and 0x0056 are all acceptable, but not 0xDCEF
- Instructions must be written on their own lines
- Arguments are separated by spaces, and are **not** comma-separated
- Comments can be denoted with a `#` either inline with an instruction or on its own line
- All instructions must follow the instruction set

A violation of any of the above will result in a syntax error and compilation will fail.

## Example Program

```
# This is an example program

MOV R1 1         # Move 1 into register R1
mov r2 2         # Move 2 into register R2

CMP r1 r2

MOVL R3 0x00AA  # R3 gets 0xaa if R1 < R2
MOVE R3 0        # R3 gets 0x0 if R1 = R2
MOVG R3 ab      # R3 get 0xab if R1 > R2

jmp R3           # Jump to the address stored in R3
```

## Usage

### Execution
```
Usage: python3 assemble.py -i [INPUT PATH] -o [OUTPUT PATH] [OPTIONS]
Example: python3 assemble.py -i foo/input.txt -o bar/output.txt -s -b
```
- Compiles an assembly file formatted as a **text file (.txt)**
- The input assembly file must exist and must be a text file
- The output path does not necessarily need to already exist, but needs to be a path to a text file

### Options
```
-s        If output file already exists, do not overwrite it
-b        Output binary instruction encodings. By default,
            instruction encodings are in hexadecimal
--help    Display this message
```

## TODO

### Minimum Requirements
- [x] Convert instructions to their corresponding encoding
- [x] Throw an error for invalid instructions
- [x] Allow for comments
- [x] Instruction encodings are printed to a text file on its own line

### Additional Features
- [x] Declaring constants
- [x] Support literal labels for subroutines
- [ ] Support pipelining instructions by stalling the processor for causal dependencies
- [x] Support using a stack pointer register
- [x] Provide error description for syntax errors
