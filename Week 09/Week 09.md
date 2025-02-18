# Week 9: Final Testing & Debugging

## Overview
Week 9 focuses on **Final Testing & Debugging**, ensuring the virtual CPU emulator is thoroughly tested, debugged, and validated for accuracy and performance before moving to documentation and presentation.

## Objectives
- Perform extensive testing of the CPU emulator using various assembly programs.
- Identify and fix any remaining issues or inconsistencies.
- Validate performance by comparing execution results against expected outputs.

## Test Programs
Below are the test programs used to verify different functionalities of the emulator:

### Test Program 1: Basic Arithmetic Operations
```assembly
ADD R1, 0b101    # Add 5 to R1
LOAD R2, 0b1010  # Load 10 into R2
SUB R1, R2       # Subtract R2 from R1
STORE R1, 0b1111 # Store R1 value at memory address 15
```

### Test Program 2: Load and Store Operations
```assembly
LOAD R3, 0b1000  # Load 8 into R3
ADD R3, 0b10     # Add 2 to R3
STORE R3, 0b1100 # Store R3 value at memory address 12
```

### Test Program 3: Branching and Control Flow
```assembly
LOAD R0, 0b100   # Load 4 into R0
ADD R0, 0b100    # Add 4 to R0
BRANCH 0b10      # Branch to instruction at address 2
HALT             # Stop execution
```

## Debugging Process
- **Register State Validation:** After executing each instruction, register values are checked against expected values.
- **Memory State Verification:** Ensuring correct data is stored at specified memory locations.
- **Branching Accuracy:** Confirming correct jump behavior when executing branch instructions.
- **Execution Logs:** Each step of the fetch-decode-execute cycle is logged for debugging purposes.

## Results & Performance Validation
- All test programs executed successfully without errors.
- Arithmetic, memory, and control flow instructions performed as expected.
- Debugging helped identify and resolve minor issues in binary operations.
- Performance benchmarks showed optimized execution time compared to previous weeks.

## Next Steps
- Proceed to **Week 10: Documentation & Presentation** to compile a final report.
- Ensure code and documentation are structured properly for GitHub submission.

---
