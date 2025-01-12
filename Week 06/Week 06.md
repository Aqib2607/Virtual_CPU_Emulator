# Week 6: I/O Operations Documentation

## Objective
To implement basic input/output operations for the Virtual CPU Emulator, enabling the CPU to interact with simulated I/O devices like a keyboard (for input) and a display (for output). This functionality allows the emulator to run I/O-intensive programs.

## Design Overview
This implementation consists of two primary components:

1. **IODevice**: A simulated I/O device that manages input and output buffers.
2. **CPU**: The central processing unit that executes I/O instructions and integrates with the IODevice.

## Algorithm for I/O Operations

1. **Initialize an IODevice**:
    - Create an `input_buffer` to hold user inputs.
    - Create an `output_buffer` to store outputs to be displayed.

2. **Design Methods for the IODevice**:
    - **Load Input**: Accept multiple inputs and store them in the `input_buffer`.
    - **Read Input**: Retrieve the next input from the `input_buffer`.
    - **Write Output**: Add data to the `output_buffer`.
    - **Display Output**: Print and clear all data from the `output_buffer`.

3. **Integrate the IODevice with the CPU**:
    - Create a `CPU` class with:
        - Registers for storing intermediate values (e.g., register `R1`).
        - A method to execute instructions (`execute_instruction`).

4. **Define the Following I/O Instructions**:
    - **READ**: Fetch data from the `IODevice`’s input buffer and store it in register `R1`.
    - **WRITE**: Write data directly to the `IODevice`’s output buffer.
    - **DISPLAY_REG**: Retrieve the value of register `R1` and send it to the `output_buffer`.

5. **Develop a Sample Program**:
    - Use a sequence of instructions such as `READ`, `WRITE`, and `DISPLAY_REG` to demonstrate I/O functionality.

6. **Execute the Sample Program**:
    - Process each instruction in order and update the state of the CPU and IODevice accordingly.

7. **Output the Results**:
    - After executing all instructions, call the `display_output` method to present the final outputs.

## Sample Program Execution

### Input
Preloaded by the user: `["Input1", "Input2"]`.

### Program
1. READ input into register `R1`.
2. DISPLAY_REG to show the value in `R1`.
3. WRITE "Processing..." to the output buffer.
4. READ another input into `R1`.
5. DISPLAY_REG to show the updated value in `R1`.
6. WRITE "Completed!" to the output buffer.

### Output
```plaintext
R1: Input1
Processing...
R1: Input2
Completed!
```

## Testing Notes
- Inputs are preloaded using the `load_input` method.
- The program handles both dynamic user inputs (via `READ`) and static outputs (via `WRITE`).
- Outputs are displayed in sequence using the `display_output` method.

## Conclusion
The implementation of Week 6 successfully integrates simulated I/O devices with the CPU, enabling robust input and output operations. This foundation can be further extended for advanced I/O handling in subsequent weeks.
