# File 02: Assembler
OPCODES = {
    'ADD': 0x01,
    'SUB': 0x02,
    'LOAD': 0x03,
    'STORE': 0x04,
    'AND': 0x05,  # Added opcode for AND
    'OR': 0x06,   # Added opcode for OR
    'NOT': 0x07   # Added opcode for NOT
}

def assemble_instruction(instruction):
    parts = instruction.split()
    opcode = OPCODES.get(parts[0].upper())
    if opcode is None:
        raise ValueError(f"Unknown instruction: {parts[0]}")
    if parts[0].upper() in ['ADD', 'SUB', 'AND', 'OR']:
        dest = int(parts[1])  # Register number in decimal
        src1 = int(parts[2])  # Source register 1 in decimal
        src2 = int(parts[3])  # Source register 2 in decimal
        return f"{opcode:08b} {dest:08b} {src1:08b} {src2:08b}"
    elif parts[0].upper() == 'NOT':
        dest = int(parts[1])  # Destination register
        src = int(parts[2])   # Source register
        return f"{opcode:08b} {dest:08b} {src:08b}"
    elif parts[0].upper() == 'LOAD':
        reg = int(parts[1])  # Register number in decimal
        address = int(parts[2].strip(','))  # Address in decimal
        return f"{opcode:08b} {reg:08b} {address:016b}"
    elif parts[0].upper() == 'STORE':
        address = int(parts[1].strip(','))  # Address in decimal
        reg = int(parts[2])  # Register number in decimal
        return f"{opcode:08b} {address:016b} {reg:08b}"
    else:
        raise ValueError("Unsupported instruction format.")

# File 03: CPU and ALU Simulation
class ALU:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def and_op(self, a, b):
        return a & b

    def or_op(self, a, b):
        return a | b

    def not_op(self, a):
        return ~a


class Registers:
    def __init__(self, size=4):
        self.registers = [0] * size

    def write(self, reg_num, value):
        self.registers[reg_num] = value

    def read(self, reg_num):
        return self.registers[reg_num]


class CPU:
    def __init__(self):
        self.alu = ALU()
        self.registers = Registers()
        self.program_counter = 0
        self.instruction_register = None

    def load_instruction(self, instruction):
        self.instruction_register = instruction
        print(f"Loaded instruction: {instruction}")

    def execute_instruction(self):
        if self.instruction_register:
            print(f"Executing instruction at PC={self.program_counter}: {self.instruction_register}")
            self.process_instruction(self.instruction_register)
            self.program_counter += 1
        else:
            print("No instruction loaded")

    def process_instruction(self, instruction):
        parts = instruction.split()
        operation = parts[0].upper()

        if operation == "ADD":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.add(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {bin(result)[2:]} in R{reg1}")
        elif operation == "SUB":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.sub(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {bin(result)[2:]} in R{reg1}")
        elif operation == "AND":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.and_op(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {bin(result)[2:]} in R{reg1}")
        elif operation == "OR":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.or_op(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {bin(result)[2:]} in R{reg1}")
        elif operation == "NOT":
            reg1, reg2 = map(int, parts[1:])
            result = self.alu.not_op(self.registers.read(reg2))
            self.registers.write(reg1, result)
            print(f"Stored {bin(result & 0xFFFFFFFF)[2:]} in R{reg1}")
        else:
            print("Invalid operation")

# Predefined inputs and execution
cpu = CPU()

# Initializing registers with values (from File 03)
cpu.registers.write(0, 5)  # R0 = 5
cpu.registers.write(1, 3)  # R1 = 3
cpu.registers.write(2, 7)  # R2 = 7

# Assembly instructions (from File 02)
assembly_code = [
    "ADD 3 0 1",  # Add R0 and R1, store in R3
    "SUB 2 2 1",  # Subtract R1 from R2, store in R2
    "AND 0 0 1",  # AND operation between R0 and R1, store in R0
    "OR 1 1 2",   # OR operation between R1 and R2, store in R1
    "NOT 2 2"      # NOT operation on R2, store in R2
]

# Convert assembly to machine code
print("\n[Attachment: File 02 - Machine Code]")
machine_code = [assemble_instruction(instr) for instr in assembly_code]
print("\n".join(machine_code))

# Execute instructions
print("\n[Attachment: File 03 - Instruction Execution]")
for instruction in assembly_code:
    cpu.load_instruction(instruction)
    cpu.execute_instruction()

# Display final register states
print("\n[Attachment: File 03 - Final Register States]")
for i in range(4):
    value = cpu.registers.read(i)
    print(f"R{i}: {bin(value & 0xFFFFFFFF)[2:]}")

# File 04: Memory and Program Execution

def add(op1, op2):
    return op1 + op2

def sub(op1, op2):
    return op1 - op2

# Memory initialization (256 locations)
memory = [None] * 256
# Registers initialization (8 general-purpose registers)
registers = [0] * 8

def execute_program(program):
    # Program Counter initialization
    pc = 0
    # Load program into memory
    for i, instruction in enumerate(program):
        memory[i] = instruction
    
    # Instruction execution loop
    while pc < len(program) and memory[pc] is not None:
        instruction = memory[pc]
        pc += 1
        # Check instruction type and process accordingly
        if isinstance(instruction[0], int):  # Load value into register
            reg_num = instruction[1]
            registers[reg_num] = instruction[0]
        elif instruction[0] == 'ADD':  # Perform addition
            reg1, reg2, reg_dest = instruction[1], instruction[2], instruction[3]
            registers[reg_dest] = add(registers[reg1], registers[reg2])
        elif instruction[0] == 'SUB':  # Perform subtraction
            reg1, reg2, reg_dest = instruction[1], instruction[2], instruction[3]
            registers[reg_dest] = sub(registers[reg1], registers[reg2])
        elif instruction[0] == 'STORE':  # Store register value into memory
            reg_num, mem_addr = instruction[1], instruction[2]
            memory[mem_addr] = registers[reg_num]

    return memory, registers

def display_memory(memory):
    print("\n[Attachment: File 04 - Final Memory State (Binary)]")
    for addr, val in enumerate(memory):
        if isinstance(val, int):  # Ensure the value is an integer
            print(f"Memory[{addr}] = {bin(val)}")
        elif val is not None:  # Handle non-integer values (e.g., instructions)
            print(f"Memory[{addr}] contains non-integer data: {val}")

def display_registers(registers):
    print("\n[Attachment: File 04 - Final Register State (Binary)]")
    for reg, val in enumerate(registers):
        print(f"R{reg} = {bin(val)}")

# Predefined program inputs in decimal (hardcoded here)
# Each instruction format:
#   [value, register] - Load value into register
#   ['ADD', reg1, reg2, reg_dest] - Add reg1 and reg2, store in reg_dest
#   ['SUB', reg1, reg2, reg_dest] - Subtract reg2 from reg1, store in reg_dest
#   ['STORE', reg, mem_addr] - Store reg value into memory address
user_program = [
    [10, 0],               # Load 10 into R0
    [20, 1],               # Load 20 into R1
    ['ADD', 0, 1, 2],      # Add R0 and R1, store result in R2
    ['SUB', 1, 0, 3],      # Subtract R0 from R1, store result in R3
    ['STORE', 2, 100],     # Store value of R2 into memory[100]
    ['STORE', 3, 101]      # Store value of R3 into memory[101]
]

# Execute the program
final_memory, final_registers = execute_program(user_program)

# Display memory and registers in binary
display_memory(final_memory)
display_registers(final_registers)
