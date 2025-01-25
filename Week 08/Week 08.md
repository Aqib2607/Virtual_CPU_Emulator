# Week 08: Profiling and Optimized Instruction Decoder

## Objective
Optimize the Virtual CPU Emulator's performance by profiling and caching frequently used operations.

## Tasks
- Profile the original instruction decoder to identify bottlenecks.
- Implement an optimized decoder using caching techniques (`lru_cache`).
- Compare the performance of the original and optimized emulators.

## Features

### Original Instruction Decoder
The original decoder converts high-level instructions into binary. While functional, it decodes each instruction independently, leading to redundant computations.

#### Code Example:
```python
# Original Instruction Decoder (Binary Output)
def decode_instructions(instructions):
    result = []
    for instruction in instructions:
        if instruction.startswith("LOAD"):
            result.append(bin(int(instruction.split()[1])))
        elif instruction.startswith("ADD"):
            result.append(bin(int(instruction.split()[1])))
        elif instruction.startswith("SUB"):
            result.append(bin(int(instruction.split()[1])))
    return result
```

### Optimized Instruction Decoder
The optimized version employs `lru_cache` to reuse previously computed results, reducing computation time for repeated instructions.

#### Code Example:
```python
# Optimized Instruction Decoder (Binary Output)
@lru_cache(maxsize=None)
def decode_instruction(instruction):
    if instruction.startswith("LOAD"):
        return bin(int(instruction.split()[1]))
    elif instruction.startswith("ADD"):
        return bin(int(instruction.split()[1]))
    elif instruction.startswith("SUB"):
        return bin(int(instruction.split()[1]))

def decode_instructions_optimized(instructions):
    return [decode_instruction(instruction) for instruction in instructions]
```

## Performance Profiling
Python's `cProfile` module is used to measure the execution time and identify bottlenecks in the code.

#### Profiling Function:
```python
# Profiling Function
def profile_emulator(func):
    pr = cProfile.Profile()
    pr.enable()
    func()
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
```

## Testing

### Input Instructions
The following instructions were used to test both emulators:
```python
instructions = [
    "LOAD 10",  # Load 10 in decimal
    "ADD 20",   # Add 20 in decimal
    "SUB 30",   # Subtract 30 in decimal
    "LOAD 10",  # Load 10 in decimal (repeated to demonstrate caching)
    "ADD 20"    # Add 20 in decimal (repeated to demonstrate caching)
]
```

### Results

#### Profiling Output for Original Emulator:
```
Profiling Original Emulator:
... (profiling stats here)
```

#### Profiling Output for Optimized Emulator:
```
Profiling Optimized Emulator:
... (profiling stats here)
```

#### Outputs:
- **Original Emulator Output (Binary):**
  ```
  ['0b1010', '0b10100', '0b11110', '0b1010', '0b10100']
  ```

- **Optimized Emulator Output (Binary):**
  ```
  ['0b1010', '0b10100', '0b11110', '0b1010', '0b10100']
  ```

## Conclusion
Using caching (`lru_cache`) significantly improves the performance of the instruction decoder, particularly for repeated instructions. This optimization can handle large instruction sets efficiently, making the emulator faster and more responsive.
