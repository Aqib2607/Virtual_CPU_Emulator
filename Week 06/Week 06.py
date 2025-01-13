class SimulatedCPU:
    def __init__(self):
        self.registers = {"A": 0}
        self.io_devices = {
            "keyboard": SimulatedKeyboard(),
            "display": SimulatedDisplay()
        }

    def execute(self, instruction):
        opcode, operand = instruction

        if opcode == "READ":
            self.registers["A"] = self.io_devices["keyboard"].read_input()
        elif opcode == "WRITE":
            self.io_devices["display"].write_output(self.registers["A"])
        elif opcode == "LOAD":
            self.registers["A"] = operand
        elif opcode == "ADD":
            self.registers["A"] += operand
        else:
            print(f"Unknown instruction: {opcode}")

class SimulatedKeyboard:
    def read_input(self):
        value = int(input("Enter a number: "))
        return value

class SimulatedDisplay:
    def write_output(self, value):
        print(f"Output to display: {value}")

if __name__ == "__main__":
    cpu = SimulatedCPU()
    program = [
        ("READ", None),
        ("ADD", 10),
        ("WRITE", None)
    ]
    for instruction in program:
        cpu.execute(instruction)
