# Virtual CPU Emulator

## Overview
This project implements a **Virtual CPU Emulator** to simulate essential CPU components and operations. The emulator is designed to cover concepts such as Instruction Set Architecture (ISA), Arithmetic Logic Unit (ALU), memory management, and I/O operations. The project follows a structured multi-week development plan, allowing incremental progress and feature integration.

## Features
- **Instruction Set Architecture (ISA):** Supports basic instructions like `ADD`, `SUB`, `LOAD`, and `STORE`.
- **ALU Operations:** Performs arithmetic and logic calculations.
- **Memory Management:** Implements memory read and write functionalities.
- **I/O Operations:** Includes basic input and output mechanisms.
- **Testing Environment:** Supports testing assembly programs within the emulator.

## Group Members 👥
- Member 1: [Aqib Jawwad Nahin **ID: 11220320969**](mailto:aqibjawwad2607@gmail.com)
- Member 2: [Mst. Suraia Akter **ID: 11220320951**](mailto:aktersuraia123@gmail.com)
- Member 3: [MD Robayet Hassan Rupom **ID: 11220320979**](mailto:rupomhossain58@gmail.com)

## Development Plan
The project is divided into weekly tasks to ensure gradual and systematic progress:

### Week 1
- Setting up the project environment.
- Writing initial documentation and creating project scaffolding.

### Week 2
- Developing the assembler to translate assembly language instructions into machine code.

### Week 3
- Implementing the register module for storing temporary data during execution.

### Week 4
- Building the fetch mechanism to retrieve instructions from memory.

### Week 5
- Implementing memory management and testing data read/write operations.

### Week 6
- Integrating all components and testing the overall emulator functionality.

## Usage

### Prerequisites
- **C++ Compiler:** Ensure a modern C++ compiler is installed.
- **CMake:** Build and manage the project.
- **Git:** Version control for collaborative development.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Aqib2607/Virtual_CPU_Emulator.git
   cd Virtual_CPU_Emulator
   ```
2. Build the project:
   ```bash
   mkdir build && cd build
   cmake ..
   make
   ```
3. Run the emulator:
   ```bash
   ./Virtual_CPU_Emulator
   ```

### Assembler Usage
To assemble a program:
```bash
./Assembler input.asm output.bin
```

## Project Structure
```
Project-vCPU-main
├── .vscode/              # IDE configuration files
├── CMakeLists.txt        # Build configuration
├── README.md             # Project documentation
├── Week 1/               # Week 1 tasks
├── Week 2/               # Week 2 tasks, including assembler
├── Week 3/               # Week 3 tasks, including register module
├── Week 4/               # Week 4 tasks, including fetch module
├── Week 5/               # Week 5 tasks, including memory management
├── Week 6/               # Week 6 tasks, final integration
├── build/                # Build artifacts
├── cpu-z-svgrepo-com.svg # CPU illustration
├── main.cpp              # Main source file
└── main                  # Compiled binary
```

## Collaboration
Our team uses GitHub for version control and progress tracking. Contributions are welcome!

## License
This project is licensed under the [MIT License](LICENSE).

---
For more details, refer to individual week documentation within the project folders.
