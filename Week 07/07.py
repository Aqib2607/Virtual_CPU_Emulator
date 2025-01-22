class SimulatedCPU:
    def __init__(self):
        self.registers = {"A": 0, "B": 0, "PC": 0}  # Registers: A, B, and PC (Program Counter)
        self.memory = [0] * 256  # Memory initialized to 256 locations
        self.stack = []  # Stack for CALL/RET instructions
        self.io_devices = {
            "keyboard": SimulatedKeyboard(),  # Simulated keyboard for input
            "display": SimulatedDisplay()  # Simulated display for output
        }

    def execute(self, instruction):
        opcode, *operands = instruction

        if opcode == "READ":  # Read input from the simulated keyboard
            self.registers["A"] = self.io_devices["keyboard"].read_input()
        elif opcode == "WRITE":  # Write output to the simulated display
            self.io_devices["display"].write_output(self.registers["A"])
        elif opcode == "LOAD":  # Load immediate value into register A
            self.registers["A"] = operands[0]
        elif opcode == "ADD":  # Add immediate value to register A
            self.registers["A"] += operands[0]
        elif opcode == "JUMP":  # Jump to a specific memory address
            self.registers["PC"] = operands[0]
        elif opcode == "CALL":  # Call a subroutine
            self.stack.append(self.registers["PC"])
            self.registers["PC"] = operands[0]
        elif opcode == "RET":  # Return from a subroutine
            self.registers["PC"] = self.stack.pop()
        elif opcode == "IF":  # Conditional jump based on register A
            if self.registers["A"] > operands[0]:
                self.registers["PC"] = operands[1]
        else:
            print(f"Unknown instruction: {opcode}")

    def display_state(self):
        # Return the current state of the registers and memory
        return self.registers, self.memory

class SimulatedKeyboard:
    def read_input(self):
        # Hardcoded decimal input
        value = 9  # Example: Input value is set as 8 in decimal
        print(f"Input: {value}")  # Display the input value
        return value

class SimulatedDisplay:
    def write_output(self, value):
        # Output in binary format
        print(f"Output to display: {bin(value)[2:]}")  # Convert to binary and strip the "0b" prefix

if __name__ == "__main__":
    cpu = SimulatedCPU()
    # Predefined program instructions
    program = [
        ("READ", None),         # Read hardcoded input (8 in decimal) into register A
        ("ADD", 10),            # Add 10 to register A (A = A + 10)
        ("WRITE", None),        # Write the value of register A to the display in binary
        ("JUMP", 6),            # Jump to instruction at index 6
        ("LOAD", 20),           # Load 20 into register A (skipped due to the JUMP)
        ("ADD", 5),             # Add 5 to register A (skipped due to the JUMP)
        # Removed second "WRITE" instruction
        ("IF", 10, 15),         # If register A > 10, jump to instruction at index 15
        ("CALL", 10),           # Call subroutine at index 10
        ("LOAD", 30),           # Load 30 into register A
        ("RET", None)           # Return from subroutine
    ]
    
    # Execute the program
    for instruction in program:
        cpu.execute(instruction)
    
    # Display final state of registers and memory
    registers, memory = cpu.display_state()
    print("\nFinal Registers:", registers)
    print("\nMemory State:", memory)
