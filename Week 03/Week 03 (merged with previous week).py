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
print("\n[Week 02 - Machine Code]")
machine_code = [assemble_instruction(instr) for instr in assembly_code]
print("\n".join(machine_code))

# Execute instructions
print("\n[Week 03 - Instruction Execution]")
for instruction in assembly_code:
    cpu.load_instruction(instruction)
    cpu.execute_instruction()

# Display final register states
print("\n[Week 03 - Final Register States]")
for i in range(4):
    value = cpu.registers.read(i)
    print(f"R{i}: {bin(value & 0xFFFFFFFF)[2:]}")
