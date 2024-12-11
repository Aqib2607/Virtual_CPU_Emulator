# Virtual CPU Emulator

## Overview
This project implements a **Virtual CPU Emulator** to simulate essential CPU components and operations. The emulator is designed to cover concepts such as Instruction Set Architecture (ISA), Arithmetic Logic Unit (ALU), memory management, and I/O operations. The project follows a structured multi-week development plan, allowing incremental progress and feature integration.

## Features
- **Instruction Set Architecture (ISA):** Supports basic instructions like `ADD`, `SUB`, `LOAD`, and `STORE`.
- **ALU Operations:** Performs arithmetic and logic calculations.
- **Memory Management:** Implements memory read and write functionalities.
- **I/O Operations:** Includes basic input and output mechanisms.
- **Testing Environment:** Supports testing assembly programs within the emulator.

## Group Members
- Member 1: [Aqib Jawwad Nahin **ID: 11220320969**](mailto:aqibjawwad2607@gmail.com)
- Member 2: [Mst. Suraia Akter **ID: 11220320951**](mailto:aktersuraia123@gmail.com)
- Member 3: [MD Robayet Hassan Rupom **ID: 11220320979**](mailto:rupomhossain58@gmail.com)

## Course Details
- **Course Name:** Computer Architecture 
- **Course Code:** 3101 
- **Section:** 5D 
- **Department:** Computer Science & Engineering 
- **Instructor:** Vashkar Kar  (Lecturer)
- **Institute:** Northern University of Business & Technology Khulna
- **Website:** www.nubtkhulna.ac.bd

## Development Plan
The project is divided into weekly tasks to ensure gradual and systematic progress:

### [Week 1: Project Planning & Setup](https://github.com/Aqib2607/Virtual_CPU_Emulator/blob/main/Week%2001/Week%2001.md)
- Setting up the project environment.
- Writing initial documentation and creating project scaffolding.

### [Week 2: Instruction Set Architecture (ISA)](https://github.com/Aqib2607/Virtual_CPU_Emulator/blob/main/Week%2002/Week%2002.md)
- Developing the assembler to translate assembly language instructions into machine code.

### [Week 3: Basic CPU Components](https://github.com/Aqib2607/Virtual_CPU_Emulator/blob/main/Week%2003/Week%2003.md)
- Implementing the register module for storing temporary data during execution.

### [Week 4: Instruction Execution](https://github.com/Aqib2607/Virtual_CPU_Emulator/blob/main/Week%2004/Week%2004.md)
- Building the fetch mechanism to retrieve instructions from memory.

### [Week 5: Memory Management](https://github.com/Aqib2607/Virtual_CPU_Emulator/blob/main/Week%2005/Week%2005.md)
- Implementing memory management and testing data read/write operations.

## Usage

### Prerequisites
- **Python Interpreter:** Ensure Python 3.x is installed on your system.
- **pip:** Python's package manager for installing dependencies.
- **Git:** Version control for collaborative development.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Aqib2607/Virtual_CPU_Emulator.git
   cd your-python-project

   ```
2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Assembler Usage
To run the assembler:
```bash
python assembler.py input.asm output.bin
```

## Collaboration
Our team uses GitHub for version control and progress tracking. Contributions are welcome!

## License
This project is licensed under the [MIT License](LICENSE).

---
For more details, refer to individual week documentation within the project folders.
