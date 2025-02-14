class CPU:
    def __init__(self):
        # ISA definition
        self.isa = {
            "ADD": "0001",
            "SUB": "0010",
            "LOAD": "0011",
            "STORE": "0100"
        }

        # Initialize CPU components
        self.registers = {"R1": 0b000000, "R2": 0b000000}  # Two 6-bit registers
        self.memory = [0b000000] * 16  # 16 memory locations
        self.io_devices = {"keyboard": 0b000000, "display": 0b000000}
        self.pc = 0  # Program counter

    def assembler(self, instruction):
        """Convert an assembly instruction to machine code."""
        parts = instruction.split()
        opcode = self.isa[parts[0]]
        reg = f"{int(parts[1][-1]):04b}"  # Convert register (e.g., R1 -> binary)
        value = f"{int(parts[2]):08b}" if len(parts) > 2 else "000000"
        return opcode + " " + reg + " " + value

    def write_memory(self, address, value):
        """Write a value to memory."""
        self.memory[address] = value

    def read_memory(self, address):
        """Read a value from memory."""
        return self.memory[address]

    def read_input(self, device):
        """Simulate reading input from a device."""
        if device == "keyboard":
            self.io_devices[device] = 0b000110  # Simulate input value of 12

    def write_output(self, device):
        """Simulate writing output to a device."""
        if device == "display":
            return f"Display Output: {self.io_devices[device]:0d}"

    def decode(self, instruction):
        """Decode an instruction into opcode and operands."""
        parts = instruction.split()
        opcode = parts[0]
        operands = parts[1:]
        return opcode, operands

    def execute(self, opcode, operands):
        """Execute the instruction based on the opcode."""
        if opcode == "LOAD":
            reg, value = operands[0], int(operands[1])
            self.registers[reg] = value
        elif opcode == "ADD":
            reg1, reg2 = operands[0], operands[1]
            self.registers[reg1] += self.registers[reg2]
        elif opcode == "STORE":
            reg, address = operands[0], int(operands[1])
            self.memory[address] = self.registers[reg]
        else:
            print("Unknown instruction")

    def fetch_decode_execute(self, instructions):
        """Perform the fetch-decode-execute cycle."""
        results = []
        while self.pc < len(instructions):
            instruction = instructions[self.pc]
            results.append(f"Fetched Instruction: {instruction}")
            opcode, operands = self.decode(instruction)
            results.append(f"Decoded Instruction: Opcode = {opcode}, Operands = {operands}")
            self.execute(opcode, operands)
            results.append(f"Registers after execution: {self.registers}")
            self.pc += 1
        return results


# Main Function to Demonstrate Functionality
if __name__ == "__main__":
    cpu = CPU()

    # Week 2: Convert assembly to machine code
    instructions = ["ADD R1 10", "SUB R2 5", "LOAD R1 20", "STORE R2 15"]
    machine_code = [cpu.assembler(inst) for inst in instructions]
    print("Machine Code:", machine_code)

    # Week 4: Execute Instructions
    execution_result = cpu.fetch_decode_execute(["LOAD R1 10", "ADD R1 R2", "STORE R1 5"])
    print("\n".join(execution_result))

    # Week 5: Memory Management
    cpu.write_memory(2, 0b000101)  # Write value 5 to address 2
    cpu.write_memory(5, 0b001011)  # Write value 11 to address 5
    print("\nMemory State:")
    print([f"Address {i}: {v:06b}" for i, v in enumerate(cpu.memory)])

    # Week 6: I/O Operations
    cpu.read_input("keyboard")
    cpu.io_devices["display"] = cpu.io_devices["keyboard"]  # Copy input to display
    display_output = cpu.write_output("display")
    print("\n", display_output)
