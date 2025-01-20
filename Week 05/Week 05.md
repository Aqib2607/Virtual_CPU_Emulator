# Week 05: Memory Management

## Objective

Implement memory management for the virtual CPU by:
- Setting up a simulated memory space.
- Performing read/write operations.
- Handling address mapping with segmentation.

## Key Concepts

1. **Simulated Memory Space**:
   - A contiguous block of memory allocated within the program to represent the CPU's memory.

2. **Memory Segmentation**:
   - Dividing memory into logical segments (e.g., Code, Data, Stack), each with defined sizes and boundaries for structured access.

3. **Logical to Physical Address Mapping**:
   - Translating logical addresses (relative to a segment) into physical addresses (absolute within memory) for operations.

4. **Memory Operations**:
   - **Write**: Store a value at a specific logical address within a defined segment.
   - **Read**: Retrieve a value from a specific logical address within a defined segment.

## Algorithm

1. **Initialize Memory**:
   - **Input**: Total memory size and segment definitions (name and size).
   - **Process**:
     - Create a memory array of the specified total size.
     - Divide memory into segments with base and limit addresses based on segment sizes.
     - Validate that total segment sizes do not exceed the total memory size.
   - **Output**: Memory structure with defined segments.

2. **Write Operation**:
   - **Input**: Segment name, logical address, and value to write.
   - **Process**:
     - Verify the segment exists.
     - Check that the logical address is within the segment's bounds.
     - Calculate the physical address by adding the segment's base address to the logical address.
     - Store the value at the calculated physical address in memory.
   - **Output**: Updated memory with the new value stored.

3. **Read Operation**:
   - **Input**: Segment name and logical address.
   - **Process**:
     - Verify the segment exists.
     - Check that the logical address is within the segment's bounds.
     - Calculate the physical address by adding the segment's base address to the logical address.
     - Retrieve the value from the calculated physical address in memory.
   - **Output**: Retrieved value from memory.

## Example

```python
# Initialize memory with total size and segment definitions
memory = Memory(total_size=1024, segments={'Code': 256, 'Data': 512, 'Stack': 256})

# Write value 42 to logical address 10 in 'Data' segment
memory.write('Data', 10, 42)

# Read value from logical address 10 in 'Data' segment
value = memory.read('Data', 10)
print(value)  # Output: 42
