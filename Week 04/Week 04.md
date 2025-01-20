# Week 04: Instruction Execution

This documentation outlines the development and implementation of the Fetch-Decode-Execute Cycle using Python for a basic CPU simulation. The goal of Week 4 was to create a simplified CPU model capable of executing basic instructions through a structured cycle.

## Objective

- Develop a basic CPU model that can fetch instructions from memory, decode them, and execute using an ALU and registers.
- Test the cycle with a set of sample instructions to ensure correct operation.

## Fetch-Decode-Execute Cycle: Overview

The cycle is divided into three main stages:

1. **Fetch**: Retrieve the next instruction from memory.
2. **Decode**: Break down the instruction into its components (opcode and operands).
3. **Execute**: Perform the operation using the ALU and registers.

## Algorithm for Instruction Execution

**Step 1: Initialization**

1. Create a memory list containing a set of instructions.
2. Initialize the Program Counter (PC) to 0.
3. Create a register file (e.g., R1, R2) and set initial values to 0.
4. Instantiate the ALU (Arithmetic Logic Unit) for performing operations.

**Step 2: Fetch Stage**

1. Retrieve the instruction from memory at the address pointed to by the PC.
2. Store the fetched instruction in the Instruction Register (IR).

**Step 3: Decode Stage**

1. Parse the opcode and operands from the IR.
2. Identify the operation to be performed and the involved registers or immediate values.

**Step 4: Execute Stage**

1. Perform the operation specified by the opcode using the ALU.
2. Update the destination register with the result.
3. Increment the PC to point to the next instruction.

**Step 5: Repeat**

1. Continue the cycle until a halt instruction is encountered or the end of the instruction list is reached.

## Sample Instructions and Execution

Consider the following set of instructions:

1. `LOAD R1, 5`  — Load the immediate value 5 into register R1.
2. `ADD R1, R2`  — Add the value of R2 to R1 and store the result in R1.
3. `SUB R1, 2`   — Subtract the immediate value 2 from R1.
4. `STORE R1, 100` — Store the value of R1 into memory address 100.

**Execution Steps:**

- **Fetch**: Retrieve `LOAD R1, 5` from memory.
- **Decode**: Identify the opcode `LOAD` and operands `R1` and `5`.
- **Execute**: Load the value 5 into register R1.

- **Fetch**: Retrieve `ADD R1, R2` from memory.
- **Decode**: Identify the opcode `ADD` and operands `R1` and `R2`.
- **Execute**: Add the value of R2 to R1 and store the result in R1.

- **Fetch**: Retrieve `SUB R1, 2` from memory.
- **Decode**: Identify the opcode `SUB` and operands `R1` and `2`.
- **Execute**: Subtract 2 from R1.

- **Fetch**: Retrieve `STORE R1, 100` from memory.
- **Decode**: Identify the opcode `STORE`, operand `R1`, and address `100`.
- **Execute**: Store the value of R1 into memory address 100.

## Conclusion

By following this structured Fetch-Decode-Execute cycle, the CPU model can effectively process a sequence of instructions, demonstrating fundamental CPU operations in a simulated environment.
