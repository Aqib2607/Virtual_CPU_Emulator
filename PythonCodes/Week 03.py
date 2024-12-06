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
        operation = parts[0].lower()

        if operation == "add":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.add(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {result} in R{reg1}")
        elif operation == "sub":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.sub(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {result} in R{reg1}")
        elif operation == "and":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.and_op(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {result} in R{reg1}")
        elif operation == "or":
            reg1, reg2, reg3 = map(int, parts[1:])
            result = self.alu.or_op(self.registers.read(reg2), self.registers.read(reg3))
            self.registers.write(reg1, result)
            print(f"Stored {result} in R{reg1}")
        elif operation == "not":
            reg1, reg2 = map(int, parts[1:])
            result = self.alu.not_op(self.registers.read(reg2))
            self.registers.write(reg1, result)
            print(f"Stored {result} in R{reg1}")
        else:
            print("Invalid operation")


cpu = CPU()

while True:
    action = input("Choose action (load, execute, write, read, exit): ").lower()
    if action == "load":
        instruction = input("Enter instruction (e.g., ADD 0 1 2): ")
        cpu.load_instruction(instruction)
    elif action == "execute":
        cpu.execute_instruction()
    elif action == "write":
        reg_num = int(input("Enter register number (0-3): "))
        value = int(input("Enter value to store: "))
        cpu.registers.write(reg_num, value)
        print(f"Stored {value} in R{reg_num}")
    elif action == "read":
        reg_num = int(input("Enter register number (0-3): "))
        print(f"Value in R{reg_num}:", cpu.registers.read(reg_num))
    elif action == "exit":
        break
    else:
        print("Invalid action")
