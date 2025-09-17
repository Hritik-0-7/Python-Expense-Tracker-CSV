Basic Python Expense Tracker

A simple, command-line expense tracker built with Python. This project allows you to log your daily expenses and saves them to a CSV file for easy viewing and management.
Features

    Add a New Expense: Easily log a new expense with a category, description, and amount.

    View All Expenses: Get a clean, formatted table of all your past expenses.

    Calculate Total: Automatically calculates and displays the sum of all your expenses.

    Persistent Storage: Your data is saved to a local expenses.csv file, so you'll never lose it.

    Zero Dependencies: The script uses only Python's built-in standard libraries—no need to install anything extra!

Project Goal

It is designed to cover these fundamental concepts:

    File I/O (reading from and writing to CSV files)

    Handling user input

    Working with dates and times

    Structuring a program with functions

    Basic data validation and error handling

Tech Stack

    Language: Python 3

    Modules Used:

        csv: For handling data storage in the CSV file.

        datetime: To automatically timestamp new expenses.

        os: To check for the existence of the CSV file.
Getting Started

Follow these instructions to get a copy of the project running on your local machine.
Prerequisites

Make sure you have Python 3 installed on your system. You can check your version by running:

python --version

Installation & Usage

    Clone the repository (or download the main.py file):

    git clone [https://github.com/your-username/python-expense-tracker.git](https://github.com/your-username/python-expense-tracker.git)

    Navigate to the project directory:

    cd python-expense-tracker

    Run the application from your terminal:

    python main.py

The program will start, and you can begin adding and viewing your expenses! An expenses.csv file will be automatically created in the same directory to store your data.
Future Improvements

This is a basic version, but it can be expanded! Here are some ideas:

    Add functionality to edit or delete existing expenses.

    Implement a feature to summarize or filter expenses by category or date range.

    Develop a Graphical User Interface (GUI) using a library like Tkinter or PyQt.
