'''Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class LibraryDashboard:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        if not file_path.endswith(".csv") or not os.path.exists(file_path):
            print("Please enter a valid CSV file.")
            return False

        df = pd.read_csv(file_path)

        columns = ["Transaction ID", "Date", "User ID",
                   "Book Title", "Genre", "Borrowing Duration"]

        for col in columns:
            if col not in df.columns:
                print("Missing column:", col)
                return False

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Borrowing Duration"] = pd.to_numeric(
            df["Borrowing Duration"], errors="coerce"
        )

        df = df.dropna()
        df = df.drop_duplicates(subset=["Transaction ID"])

        # A small computed column for the report
        df["Long Borrow"] = df["Borrowing Duration"] > 14

        self.data = df
        return True

    def calculate_statistics(self):
        duration = np.array(self.data["Borrowing Duration"])
        books = self.data["Book Title"].value_counts()

        busy_day = self.data["Date"].dt.day_name().value_counts().idxmax()

        print("\n--- Statistics ---")
        print("Most borrowed book:", books.index[0])
        print("Average borrowing days:", round(np.mean(duration), 2))
        print("Standard deviation:", round(np.std(duration), 2))
        print("Busiest day:", busy_day)

    def filter_transactions(self, condition):
        try:
            result = self.data.query(condition)
            print("\nFiltered records:")
            print(result.head(10))
            print("Number of records:", len(result))
        except Exception:
            print("Invalid filter condition.")

    def generate_report(self):
        print("\n--- Simple Report ---")
        print("Total transactions:", len(self.data))
        print("Different books:", self.data["Book Title"].nunique())
        print("Different genres:", self.data["Genre"].nunique())

        print("\nBorrowings by genre:")
        print(self.data.groupby("Genre").size())

    def show_charts(self):
        # Bar chart
        top = self.data["Book Title"].value_counts().head(5)
        top.plot(kind="bar", title="Top 5 Most Borrowed Books")
        plt.xlabel("Book")
        plt.ylabel("Borrowings")
        plt.tight_layout()
        plt.show()

        # Line graph
        monthly = self.data.groupby(self.data["Date"].dt.to_period("M")).size()
        monthly.index = monthly.index.astype(str)
        monthly.plot(kind="line", marker="o", title="Monthly Borrowing Trend")
        plt.xlabel("Month")
        plt.ylabel("Borrowings")
        plt.tight_layout()
        plt.show()

        # Pie chart
        self.data["Genre"].value_counts().plot(
            kind="pie", autopct="%1.1f%%", title="Borrowings by Genre"
        )
        plt.ylabel("")
        plt.show()

        # Heatmap
        table = pd.crosstab(
            self.data["Genre"], self.data["Date"].dt.day_name()
        )
        sns.heatmap(table, annot=True, fmt="d")
        plt.title("Genre Borrowing Activity")
        plt.tight_layout()
        plt.show()


def main():
    print("E-Library Data Insights Dashboard")
    file_name = input(
        "Enter CSV file name [library_transactions.csv]: "
    ).strip()

    if file_name == "":
        file_name = "library_transactions.csv"

    dashboard = LibraryDashboard()

    if dashboard.load_data(file_name):
        print("Data loaded successfully.")
        dashboard.calculate_statistics()
        dashboard.generate_report()

        condition = input(
            "\nEnter filter, e.g. Genre == 'Fiction' "
            "(press Enter to skip): "
        ).strip()

        if condition:
            dashboard.filter_transactions(condition)

        dashboard.show_charts()


if __name__ == "__main__":
    main()
