def add(op1, op2):
    return op1 + op2

def sub(op1, op2):
    return op1 - op2

memory = [None] * 256
registers = [0] * 8

def execute_program(program):
    global memory, registers
    pc = 0
    for i, instruction in enumerate(program):
        memory[i] = instruction
    while pc < len(program) and memory[pc] is not None:
        instruction = memory[pc]
        pc += 1
        if isinstance(instruction[0], int):
            registers[instruction[1]] = instruction[0]
        elif instruction[0] == 'ADD':
            registers[instruction[3]] = add(registers[instruction[1]], registers[instruction[2]])
        elif instruction[0] == 'SUB':
            registers[instruction[3]] = sub(registers[instruction[1]], registers[instruction[2]])
        elif instruction[0] == 'STORE':
            memory[instruction[2]] = registers[instruction[1]]
    return memory, registers

def get_user_input():
    print("Enter the program instructions in the format:")
    print("[Operation, Operand1, Operand2, ...] (e.g., [10, 0] for LOAD or ['ADD', 0, 1, 2] for ADD)")
    print("Type 'END' to finish.")
    program = []
    while True:
        user_input = input("Enter instruction: ")
        if user_input.strip().upper() == 'END':
            break
        try:
            instruction = eval(user_input)
            program.append(instruction)
        except:
            print("Invalid input. Try again.")
    return program

print("Virtual CPU Emulator")
user_program = get_user_input()
final_memory, final_registers = execute_program(user_program)

print("\nFinal Memory State:")
for addr, val in enumerate(final_memory):
    if val is not None:
        print(f"Memory[{addr}] = {val}")

print("\nFinal Register State:")
for reg, val in enumerate(final_registers):
    print(f"R{reg} = {val}")
