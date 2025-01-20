# Week 3: Basic CPU Components

This week's project focuses on simulating the basic operations of a CPU, allowing users to interact with the system through various commands such as load, execute, write, read, and exit. The algorithm utilizes an Arithmetic Logic Unit (ALU) and a set of general-purpose registers to perform fundamental arithmetic and logical instructions.

## Algorithm

1. **Initialization**:
   - Initialize four registers (R0 to R3), each set to 0.
   - Set the Program Counter (PC) to 0.
   - Prepare an Instruction Register to store the current instruction.

2. **Input and Actions**:
   - **Write Action**:
     - Prompt the user to select a register (R0 to R3) and input a value to store.
     - Store the input value in the chosen register.
   - **Read Action**:
     - Prompt the user to select a register (R0 to R3).
     - Display the current value stored in the selected register.
   - **Load Instruction**:
     - Prompt the user to input an instruction (e.g., `ADD 0 1 2`).
     - Parse the instruction to identify the operation (`ADD`, `SUB`, `AND`, `OR`, `NOT`) and the registers involved.
     - Store the instruction in the Instruction Register.
   - **Execute Instruction**:
     - Fetch the instruction from the Instruction Register.
     - Decode the operation and identify the source and destination registers.
     - Perform the operation using the ALU.
     - Store the result in the specified register.
     - Increment the Program Counter.
   - **Exit**:
     - Terminate the simulation.

## Sample Operations

- **Write to Register**:
  - User selects `R1` and inputs the value `5`.
  - Register `R1` now contains `5`.

- **Read from Register**:
  - User selects `R1`.
  - System outputs the value `5`.

- **Load and Execute Instruction**:
  - User inputs the instruction `ADD 0 1 2`.
  - The system adds the values in `R1` and `R2`, stores the result in `R0`, and increments the Program Counter.

## Conclusion

This simulation provides a foundational understanding of CPU operations, including register manipulation and basic instruction execution. It serves as a stepping stone for more complex CPU functionalities in subsequent weeks.
