class VirtualMemory:
    def __init__(self, total_size, segment_sizes):
        self.total_size = total_size
        self.memory = [0] * total_size
        self.segments = self.setup_segments(segment_sizes)

    def setup_segments(self, segment_sizes):
        segments = {}
        base_address = 0
        for segment_name, size in segment_sizes.items():
            if base_address + size > self.total_size:
                raise ValueError(f"Segment {segment_name} exceeds memory limits.")
            segments[segment_name] = (base_address, base_address + size - 1)
            base_address += size
        return segments

    def write(self, segment_name, logical_address, value):
        if segment_name not in self.segments:
            raise KeyError(f"Segment {segment_name} does not exist.")
        base, limit = self.segments[segment_name]
        physical_address = base + logical_address
        if physical_address > limit or logical_address < 0:
            raise ValueError(f"Logical address {logical_address} exceeds segment limit.")
        self.memory[physical_address] = value
        return f"Value {value} written to segment {segment_name} at logical address {logical_address}."

    def read(self, segment_name, logical_address):
        if segment_name not in self.segments:
            raise KeyError(f"Segment {segment_name} does not exist.")
        base, limit = self.segments[segment_name]
        physical_address = base + logical_address
        if physical_address > limit or logical_address < 0:
            raise ValueError(f"Logical address {logical_address} exceeds segment limit.")
        return self.memory[physical_address]

    def display_memory(self):
        return self.memory

def main():
    total_size = int(input("Enter total memory size: "))
    num_segments = int(input("Enter number of segments: "))
    
    segment_sizes = {}
    for _ in range(num_segments):
        segment_name = input("Enter segment name: ")
        segment_size = int(input(f"Enter size for segment {segment_name}: "))
        segment_sizes[segment_name] = segment_size

    vm = VirtualMemory(total_size, segment_sizes)

    while True:
        print("\nChoose an operation:")
        print("1. Write")
        print("2. Read")
        print("3. Display Memory")
        print("4. Exit")
        operation = int(input("Enter operation number: "))

        if operation == 1:
            segment_name = input("Enter segment name to write to: ")
            logical_address = int(input("Enter logical address to write to: "))
            value = int(input("Enter value to write: "))
            print(vm.write(segment_name, logical_address, value))

        elif operation == 2:
            segment_name = input("Enter segment name to read from: ")
            logical_address = int(input("Enter logical address to read from: "))
            print(f"Value at logical address {logical_address} in {segment_name} segment: {vm.read(segment_name, logical_address)}")

        elif operation == 3:
            print("Full Memory State:", vm.display_memory())

        elif operation == 4:
            print("Exiting...")
            break

        else:
            print("Invalid operation. Try again.")

if __name__ == "__main__":
    main()
