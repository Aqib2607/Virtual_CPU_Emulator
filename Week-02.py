OPCODES = {
    'ADD': 0x01,
    'SUB': 0x02,
    'LOAD': 0x03,
    'STORE': 0x04
}

def assemble_instruction(instruction):
    parts = instruction.split()
    opcode = OPCODES.get(parts[0].upper())
    if opcode is None:
        raise ValueError(f"Unknown instruction: {parts[0]}")
    if parts[0].upper() in ['ADD', 'SUB']:
        dest = int(parts[1][1])
        src1 = int(parts[2][1])
        src2 = int(parts[3][1])
        return f"{opcode:02x} {dest:02x} {src1:02x} {src2:02x}"
    elif parts[0].upper() == 'LOAD':
        reg = int(parts[1][1])
        address = int(parts[2].strip(',').strip(), 16) if parts[2].startswith('0x') else int(parts[2].strip(',').strip())
        return f"{opcode:02x} {reg:02x} {address:04x}"
    elif parts[0].upper() == 'STORE':
        address = int(parts[1].strip(',').strip(), 16) if parts[1].startswith('0x') else int(parts[1].strip(',').strip())
        reg = int(parts[2][1])
        return f"{opcode:02x} {address:04x} {reg:02x}"
    else:
        raise ValueError("Unsupported instruction format.")

assembly_code = [
    "ADD R1, R2, R3",
    "LOAD R1, 0x10",
    "STORE 0x10, R1"
]

machine_code = [assemble_instruction(instr) for instr in assembly_code]
print("Machine Code:")
print("\n".join(machine_code))
