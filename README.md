# RISC-Assembler

This is an assembler written in python that translates a custom assembly language into 32-bit binary instructions.

## Instruction Set

Refer to the [instruction set](https://github.com/DFriend01/RISC-Assembler/blob/main/docs/InstructionSet.pdf) to see which instructions are supported and how they function. Take a look at the [instruction encodings](https://github.com/DFriend01/RISC-Assembler/blob/main/docs/InstructionEncodings.pdf) to see how all the instructions are encoded into 32 bits.

## Syntax Rules

### Instructions
- Instructions are **case insensitive** and indentation/extra spaces are ignored
- Valid registers are denoted as R0 through R9 and SP (R0, R1, R2, ... R9, SP)
- Literals cannot exceed 1 byte and must be expressed as hexadecimal values prefixed with `0x`
  - Example: `0xCD`, `0xbd`, and `0x0056` are all acceptable, but not `0xDCEF` and `AA`
- Instructions must be written on their own lines
- Arguments are separated by spaces, and are **not** comma-separated
- Comments can be denoted with a `#` either inline with an instruction or on its own line
- All instructions must follow the instruction set

### Constants
- Names of constants cannot be keywords (register names or instruction names)
- Constant names may not contain spaces and cannot start with a digit
- Constant names are **case insensitive**
- Constant values are 1-byte literals and can be declared by the following:
  - `CONSTANT <name> <literal>`
  - Example: `CONSTANT foo 0xAB`
- There cannot be duplicate constant names
- If both a label and a constant share the same name, the constant will always take precedence over the label

### Labels
- Names of labels cannot be keywords (register names or instruction names)
- Label names may not contain spaces and cannot start with a digit
- Label names are **case insensitive**
- Labels may be declared either on its own line or inline with an instruction, and are declared like the following:
  - `<name>: <optional instruction>`
  - Example: `bar: mov r1 0x0`
  - Notice how the `:` is not separated by a space from the label name
- Labels may only be used by jump instructions and the `CALL` instruction.

A violation of any of the above will result in a syntax error and compilation will fail.

## Example Program

```
# This is an example program

CONSTANT foo 0x1
constant bar 0x2

MOV R1 foo         # Move 1 into register R1
mov r2 bar         # Move 2 into register R2

# Labelling
subroutine: CMP r1 r2

            MOVL R3 0x00AA
            MOVE R3 0x0
            MOVG R3 0xab

sillylabel:

            jmp subroutine

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

## Setup

### Step 1: Set up the virtual environment (optional)
A virtual environment is optional, but highly recommended. Refer to the [python docs](https://docs.python.org/3/tutorial/venv.html) if you are
unfamiliar with virtual environments. Execute the following **in the project
root directory**:

```
# Install virtualenv globally if not already installed
python3 -m pip install virtualenv

# Create the virtual environment
python3 -m venv env

# Activate the virtual environment
env/Scripts/activate (Windows)
source env/bin/activate (Unix)
```

### Step 2: Install the RISCAssembler package
If you are using a virtual environment, activate it first. Then, execute
`pip install -e .`. **Make sure you are in the project root directory when
running this command**.

## Running the Tests
To run all of the tests at once, execute `python3 -m unittest discover -s test -p '*_test.py'`. Alternatively, one can go into the `test` directory and
run the specific test file directly.

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
