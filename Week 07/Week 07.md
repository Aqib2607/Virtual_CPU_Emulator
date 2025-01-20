# Week 7: Advanced Features

## Objective
Enhance the Virtual CPU Emulator by introducing advanced features:
1. Branching and control flow instructions.
2. Subroutines and interrupt handling.
3. Pipeline mechanism for efficient instruction processing.

---

## Tasks and Algorithms

### 1. Branching and Control Flow Instructions
**Purpose**: Allow the CPU to change the execution flow based on conditions or jump to specific memory addresses.

**Algorithm**:
1. Fetch the instruction.
2. If the instruction is `JUMP`:
   - Set the program counter to the specified target address.
3. If the instruction is `JUMP_IF_ZERO`:
   - Check the value of the specified register.
   - If the value is `0`, set the program counter to the target address.
4. If the condition is not met, proceed to the next instruction.

---

### 2. Subroutines and Interrupts
**Purpose**: Enable reusable code blocks (subroutines) and asynchronous handling of events (interrupts).

**Algorithm**:
1. Fetch the instruction.
2. If the instruction is `CALL`:
   - Push the current program counter to the stack.
   - Set the program counter to the target subroutine address.
3. If the instruction is `RET`:
   - Pop the return address from the stack.
   - Set the program counter to the return address.
4. If the instruction is `INTERRUPT`:
   - Print or handle the custom interrupt message.
5. Resume execution at the next instruction.

---

### 3. Pipeline Mechanism
**Purpose**: Simulate the overlapping stages of instruction processing to improve execution efficiency.

**Pipeline Stages**:
1. **Fetch**: Load the instruction from memory into the pipeline.
2. **Decode**: Interpret the fetched instruction to determine its operation and operands.
3. **Execute**: Perform the operation using the registers and update CPU state.

**Algorithm**:
1. Initialize a pipeline with a fixed size (e.g., 3 stages).
2. Repeat until all instructions are processed:
   - **Fetch**: Add the next instruction to the pipeline.
   - **Decode**: Parse the operation and operands of the fetched instruction.
   - **Execute**: Perform the operation and update the registers or program counter.
3. Clear the pipeline when a branch or subroutine modifies the program counter.

---

## Sample Workflow

### Input Instructions:
1. Load `5` into Register 1 (R1).
2. Subtract `5` from R1.
3. If R1 is zero, jump to instruction `7`.
4. Skip instructions for R2 due to the jump.
5. Call a subroutine to load `20` into R3.
6. Return to the main program and handle an interrupt.

---

### Output:
**Registers**:
- R1: 0
- R2: 0
- R3: 20

**Interrupt Message**:
`End of program`
