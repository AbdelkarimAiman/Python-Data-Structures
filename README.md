# Python Data Structures & Algorithms Portfolio

## Overview
This repository serves as a comprehensive collection of fundamental Computer Science implementations using **Python**. 
Designed for educational purposes and technical interview preparation, each script emphasizes **Clean Code**, **Type Hinting**, and **Time Complexity Analysis (Big O)**.

> **Goal:** To demonstrate a deep understanding of how data structures work "under the hood," moving beyond simple library usage.

---

## Repository Contents

| File Name | Topic | Description | Complexity Focus |
|-----------|-------|-------------|------------------|
| `linked_list.py` | **Linked List** | Complete implementation of Singly Linked List (Insert, Delete, Search). | Memory Management |
| `stack_implementation.py` | **Stack** | LIFO (Last In, First Out) structure implementation. | $O(1)$ Operations |
| `queue_implementation.py` | **Queue** | FIFO (First In, First Out) structure using Python Lists. | Queue Logic |
| `2d_array_traversal.py` | **2D Arrays** | Matrix manipulation and traversal algorithms. | $O(n \times m)$ |
| `big_o_complexity.py` | **Big O Analysis** | Practical demonstration of time complexity classes ($O(1)$ to $O(2^n)$). | Algorithm Efficiency |

---

## Key Features
- **Type Hinting:** All functions use Python 3.5+ type hints (e.g., `def func(n: int) -> None:`) for clarity and static analysis.
- **Big O Documentation:** Every data structure includes comments explaining the time complexity of its operations.
- **Test-Driven:** Each file includes a `if __name__ == "__main__":` block with practical examples and edge cases.
- **Educational Comments:** Code is heavily commented to explain *why* specific logic is used.

---

## How to Run
You can test any data structure individually by running its script directly:

```bash
# To test the Stack implementation
python stack_implementation.py

# To see Big O examples in action
python big_o_complexity.py

#  Python Data Structures: Linked List
```
## Overview
This repository contains a clean, academic implementation of a **Singly Linked List** in Python. 
The goal of this project is to demonstrate understanding of low-level memory management, pointer manipulation, and algorithmic efficiency without relying on built-in dynamic arrays.

## Key Features
- **Insertion:** At beginning, end, and specific positions.
- **Deletion:** By value or position.
- **Traversal:** Efficient iteration through nodes.
- **Search:** Linear search implementation.

## Time Complexity (Big O)
| Operation | Complexity | Description |
|-----------|------------|-------------|
| **Access**| O(n)       | Linear time required to traverse. |
| **Search**| O(n)       | Worst-case scenario requires scanning the full list. |
| **Insert**| O(1)       | Constant time (at the head). |
| **Delete**| O(1)       | Constant time (if pointer is known). |

## Technologies
- **Language:** Python 3.x
- **Concepts:** OOP, Data Structures, Algorithms.

## Author
**Abdelkarim Abusamra** *AI Engineer | Strategic Data Analyst*
