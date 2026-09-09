E-Library Data Insights Dashboard

Introduction

This is a small Python project for analysing book borrowing records.
I used Pandas for data handling, NumPy for calculations and
Matplotlib/Seaborn for charts.

Files

• library_dashboard.py - main Python program
• library_transactions.csv - sample dataset
• README.md - project information

Libraries Required

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Dataset Columns

The CSV file contains:

• Transaction ID
• Date
• User ID
• Book Title
• Genre
• Borrowing Duration

How to Run

Keep all the files in the same folder and run:

```bash
python library_dashboard.py
```

When asked for the file name, enter:

```text
library_transactions.csv
```

Features

1. Checks the CSV file and required columns.
2. Removes missing and duplicate records.
3. Finds the most borrowed book.
4. Calculates average borrowing time and standard deviation.
5. Finds the busiest day.
6. Groups borrowing records by genre.
7. Allows a simple Pandas filter.
8. Displays:
  • Top 5 books bar chart
  • Monthly borrowing line graph
  • Genre pie chart
  • Genre/day heatmap

OOP

The project uses a LibraryDashboard class.

Important methods are:

• load_data()
• calculate_statistics()
• filter_transactions()
• generate_report()
• show_charts()

Example Filter

When the program asks for a filter, you can enter:

```text
Genre == 'Fiction'
```

or:

```text
Borrowing Duration > 10
```
