# Deadlock Prevention and Recovery Simulator

This project is an interactive web application built with **Streamlit** to demonstrate deadlock prevention (Banker's Algorithm) and deadlock recovery strategies (including process termination) for educational and simulation purposes.

## Features

- **Banker's Algorithm:**  
  Check if the system is in a safe state and find the safe sequence for process execution.

- **Resource Request Simulation:**  
  Simulate resource requests by processes and check if they can be safely granted.

- **Deadlock Detection & Recovery:**  
  - Detect unsafe states (potential deadlock).
  - Recover from deadlock using:
    - **Process Termination:** Terminate a process, release its resources, and update the system state.
    - **Resource Preemption:** (Optional, if implemented) Preempt resources from a process.
    - **Rollback:** (Optional, if implemented) Roll back a process to a previous state.

- **Resource Allocation Graph (RAG) Visualization:**  
  (If implemented) Visualize the current allocation and detect cycles.

- **User-Friendly UI:**  
  Step-by-step interface for inputting system parameters, matrices, and interacting with the algorithms.

## How Process Termination Works

When a process is terminated as part of deadlock recovery:
- Its allocated resources are released back to the available pool.
- Its allocation and maximum demand in the system matrices are set to zero.
- It is excluded from future safe sequence calculations and resource requests.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/deadlock-simulator.git
    cd deadlock-simulator
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Main dependency: `streamlit`)*

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run ui.py
    ```

2. **Follow the on-screen instructions:**
    - Set the number of processes and resource types.
    - Enter the allocation, maximum demand, and available resources.
    - Check the system state and safe sequence.
    - Simulate resource requests or recover from deadlock by terminating processes.

## File Structure

```
.
├── ui.py           
├── bankers.py    
├── recovery.py     
├── requirements.txt
└── README.md
```

