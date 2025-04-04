# ReadMe - Instructions to Run the 8-Puzzle Solver

## Overview
This project implements an **8-Puzzle Solver** using the **Breadth-First Search (BFS) algorithm**.
The solver finds the shortest path from an initial state to the goal state, storing results in text files for further analysis.

## Why is the Initial and Goal State Taken in Column Order?
In the implementation, the **initial state and goal state** are provided in **column-major order** instead of the conventional row-major order. This approach is used because:

1. **Consistency with Output Format:** The project requires writing output states in column-major order.
2. **Matrix Representation Alignment:** Many textbooks and examples represent 8-puzzle states in a column-wise format.
3. **Ease of Reading in Visualization:** When transposing the matrix for better visualization, a column-order input simplifies transformations.

If needed, you can convert the input to row-major format by modifying the way matrices are stored and manipulated in the code.

## Prerequisites
Before running the code, ensure you have **Python 3.x** installed along with the required libraries.

### Required Libraries:
- **NumPy**: For efficient matrix operations
  ```sh
  pip install numpy
  ```

## How to Run the Code in VS Code
Follow these steps to run the 8-Puzzle solver locally in VS Code:

### 1. Open VS Code and Set Up Environment
- Open **VS Code**.
- Install **Python extension** if not already installed.
- Create a new **workspace folder** and place the Python script inside it.

### 2. Open a Terminal and Navigate to the Script Directory
```sh
cd path/to/your/script/folder
```

### 3. Run the Python Script
Execute the following command:
```sh
python 8puzzle_solver.py
```
(Replace `8puzzle_solver.py` with the actual filename.)

### 4. Expected Output
- The script prints the **initial state**, the **number of explored nodes**, and whether a solution is found.
- If a solution is found, it writes three output files:
  - **`Nodes.txt`**: Contains all explored states.
  - **`NodesInfo.txt`**: Contains node index, parent node index, and corresponding state.
  - **`nodePath.txt`**: Contains the sequence of states from the initial state to the goal.

### 5. Open Output Files
After execution, check the output files in the same directory to analyze the solution.


Solution found! Output files generated.
```

## Troubleshooting
- If **NumPy is missing**, install it using:
  ```sh
  pip install numpy
  ```
- If **Python is not recognized**, ensure it is installed and added to your system **PATH**.
- If execution is slow, try **running in a dedicated terminal** instead of VS Code’s built-in terminal.


## Conclusion
This project successfully implements an **efficient 8-Puzzle solver** using BFS, allowing users to find solutions to a given puzzle state and analyze the output via generated files.

🚀 Happy Coding!
