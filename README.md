# Matrix-Operations-Tool

Matrix Operations Tool is a web-based application built with **Streamlit** and **NumPy** that allows users to perform common matrix operations through an interactive and user-friendly interface.

---

## Features

- **Addition (+)**: Adds two matrices of the same dimensions.  
- **Subtraction (-)**: Subtracts one matrix from another (matrices must have the same dimensions).  
- **Multiplication (×)**: Multiplies two matrices, checking for compatibility.  
- **Transpose (T)**: Transposes a single matrix.  
- **Determinant**: Calculates the determinant of a square matrix.  

---

## How to Use

### 1. Enter Your Matrices
In the **Matrix Operations** tab, you will see two text areas for **Matrix A** and **Matrix B**. Enter your matrix elements here.  

- Separate elements in a row with a space.  
- Use a new line for each new row of the matrix.  

**Example**: A 2×2 matrix with elements 1, 2, 3, 4 should be entered as:
1 2
3 4


### 2. Select an Operation
Click the button for the operation you want to perform (e.g., **Addition (+)**).

### 3. View the Result
The calculated result will be displayed below the buttons.  
If there is an error (e.g., mismatched dimensions), an error message will appear.

---

## Installation and Setup

1. Make sure you have **Python** installed.  
2. Install the required libraries:

```bash
pip install streamlit numpy


Save the provided Python code as streamlit_matrix_tool.py.

Run the application from your terminal:

streamlit run streamlit_matrix_tool.py

Cheat Sheet

A dedicated Cheat Sheet tab is included in the application.
It provides a quick reference for the rules and requirements of each matrix operation to help you avoid common errors.
