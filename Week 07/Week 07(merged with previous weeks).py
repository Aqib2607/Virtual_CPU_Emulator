# Week 2: Instruction Set Architecture (ISA)
def week_2_define_instructions():
    """
    Week 2: Define ISA and create an assembler to convert assembly to machine code.
    """
    isa = {
        "ADD": "0001",  # Opcode for addition
        "SUB": "0010",  # Opcode for subtraction
        "LOAD": "0011",  # Opcode for loading from memory
        "STORE": "0100",  # Opcode for storing to memory
    }

    def assembler(instruction):
        parts = instruction.split()
        opcode = isa[parts[0]]
        reg = f"{int(parts[1][-1]):04b} "  # Register in binary (e.g., R1 -> 01)
        value = f"{int(parts[2]):08b}" if len(parts) > 2 else "000000"  # Value in binary
        return opcode +" "+ reg + value

    # Example assembly instructions
    instructions = ["ADD R1 10", "SUB R2 5", "LOAD R1 20", "STORE R2 15"]
    machine_code = [assembler(inst) for inst in instructions]
    return machine_code


# Week 3: Basic CPU Components
def week_3_cpu_components():
    """
    Week 3: Build basic CPU components: ALU, registers, and program counter.
    """
    class ALU:
        def operate(self, opcode, operand1, operand2):
            if opcode == "0001":  # ADD
                return operand1 + operand2
            elif opcode == "0010":  # SUB
                return operand1 - operand2

    class Registers:
        def __init__(self):
            self.regs = [0b000000] * 4  # Four 6-bit registers

        def write(self, reg_num, value):
            self.regs[reg_num] = value

        def read(self, reg_num):
            return self.regs[reg_num]

    alu = ALU()
    registers = Registers()
    pc = 0b000000  # Program counter

    # Example operations
    registers.write(0, 0b000010)  # Write 2 to R0
    registers.write(1, 0b000011)  # Write 3 to R1
    result = alu.operate("0001", registers.read(0), registers.read(1))  # ADD R0, R1
    main_result= f"Result of ADD: {result:06d}"
    pc_results= f"\nProgram Counter: {pc:06b}"

    return main_result + pc_results


# Week 4: Instruction Execution
def week_4_execute_instructions():
    """
    Week 4: Implement fetch-decode-execute cycle.
    """
    memory = [ "LOAD R1, 10", "ADD R1, R2", "STORE R1, 20" ]  # Binary instructions in memory
    registers = {"R1": 0b00, "R2": 0b101}  # Initialize registers
    pc = 0  # Program counter
    
    # Function to decode an instruction
    def decode(instruction):
        parts = instruction.split()  # Split into operation and operands
        opcode = parts[0]  # The operation (e.g., LOAD, ADD, STORE)
        operands = parts[1:]  # The arguments (e.g., R1, 10)
        return opcode, operands

    # Function to execute an instruction
    def execute(opcode, operands):
        if opcode == "LOAD":
            reg, value = operands[0], int(operands[1])  # Extract register and value
            registers[reg] = value  # Load the value into the register
        elif opcode == "ADD":
            reg1, reg2 = operands[0], operands[1]  # Extract the two registers
            registers[reg1] += registers[reg2]  # Perform addition
        elif opcode == "STORE":
            reg, address = operands[0], int(operands[1])  # Extract register and address
            print(f"Value at Memory Address {address}: {registers[reg]}")
        else:
            print("Unknown instruction")

    main_result= []
    # Fetch-Decode-Execute Cycle
    while (pc < len(memory)):
        instruction = memory[pc]  # Fetch
        a1=f"Fetched Instruction: {instruction}"
        opcode, operands = decode(instruction)  # Decode
        b1=f"\nDecoded Instruction: Opcode = {opcode}, Operands = {operands}"
        execute(opcode, operands)  # Execute
        c1=f"\nRegisters after execution: {registers}"
        pc += 1  # Update Program Counter to the next instruction
        main_result.append(a1)
        main_result.append(b1)
        main_result.append(c1)

    return  main_result

# Week 5: Memory Management
def week_5_memory_management():
    """
    Week 5: Implement memory management for the virtual CPU.
    """
    memory = [0b000000] * 16  # 16 memory locations
    
    def write_memory(address, value):
        memory[address] = value

    def read_memory(address):
        return memory[address]

    # Example operations
    write_memory(2, 0b000101)  # Write value 5 to address 2
    write_memory(5, 0b001011)  # Write value 11 to address 5
    
    return [f"Address {i:0d}: {v:06b}" for i, v in enumerate(memory)]

# Week 6: I/O Operations
def week_6_io_operations():
    """
    Week 6: Implement basic I/O operations with simulated keyboard and display.
    """
    io_devices = {"keyboard": 0b000000, "display": 0b000000}

    def read_input(device):
        if device == "keyboard":
            # Simulate reading input from keyboard (e.g., entering the number 12)
            io_devices[device] = 0b000110  # Binary of 12

    def write_output(device):
        if device == "display":
            return f"Display Output: {io_devices[device]:0d}"

    # Example I/O operations
    read_input("keyboard")
    io_devices["display"] = io_devices["keyboard"]  # Copy keyboard input to display
    return write_output("display")

# Week 7: Advanced Features
def week_7_advanced_features():
    """
    Week 7: Implement branching, subroutines, and simple pipelining.
    """
    memory = ["011000000010", "000101000001", "111100000000"]  # Branch, ADD, HALT
    registers = [0b000000] * 4
    pc = 0  # Program counter

    def execute(instruction):
        nonlocal pc
        opcode = instruction[:4]
        if opcode == "0110":  # Branch to address
            pc = int(instruction[4:], 2)
        elif opcode == "0001":  # ADD
            reg_num = int(instruction[4:6], 2)
            value = int(instruction[6:], 2)
            registers[reg_num] += value

    # Pipeline: Fetch, Decode, Execute
    pipeline = {"fetch": None, "decode": None, "execute": None}
    while pc < len(memory):
        pipeline["execute"] = pipeline["decode"]
        pipeline["decode"] = pipeline["fetch"]
        pipeline["fetch"] = memory[pc]
        if pipeline["execute"]:
            execute(pipeline["execute"])
        pc += 1
    return [f"R{i}: {reg:06b}" for i, reg in enumerate(registers)]

# Execute all weeks
def main():
    print("Week 2 Output:")
    print(week_2_define_instructions())
    print("\nWeek 3 Output:")
    print(week_3_cpu_components())
    print("\nWeek 4 Output:")
    print(week_4_execute_instructions())
    print("\nWeek 5 Output:")
    print(week_5_memory_management())
    print("\nWeek 6 Output:")
    print(week_6_io_operations())
    print("\nWeek 7 Output:")
    print(week_7_advanced_features())

if __name__ == "__main__":
    main()
