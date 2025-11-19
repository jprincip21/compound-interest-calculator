# Compound Interest Calculator

This project is a simple **GUI-based Compound Interest Calculator** built with **FreeSimpleGUI** and **Matplotlib**. It allows users to enter an initial investment amount, interest rate, compounding period, and number of years, then displays both the calculated values and a bar chart of the growth over time.

## Features
- Simple and user-friendly interface  
- Multiple compounding periods (Annually, Semi-Annually, Quarterly, Monthly, Daily)  
- Generates a bar chart showing the value growth over time  
- Handles invalid input with built-in error messages  

## How It Works
1. The user enters:
   - Initial value  
   - Interest rate  
   - Compounding period  
   - Number of years

2. The calculator uses the formula: A = P * (1 + r/n)^(n * t)

3. A bar graph is created and displayed in the GUI.

## File Overview
- **main.py** — GUI and program logic  
- **calculations.py** — Compound interest calculations  
- **chart.py** — Chart creation and drawing  

## Requirements
pip install FreeSimpleGUI matplotlib
