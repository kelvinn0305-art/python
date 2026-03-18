import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    def __init__(self):
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv("retailandsales.csv")
            print(" Data loaded successfully!\n")
        except Exception as e:
            print(" Error loading file:", e)

    def calculate_metrics(self):
        try:    
            print("Sales Metrics:\n")
            total_sales = np.sum(self.data['Total Sales'])
            avg_sales = np.mean(self.data['Total Sales'])
            popular_product = self.data.groupby('Product')['Quantity Sold'].sum().idxmax()
            print(f"Total Sales: {total_sales}")
            print(f"Average Sales: {avg_sales}")
            print(f"Most Popular Product: {popular_product}\n")
        except Exception as e:
            print("Error :",e)

    def filter_data(self):
        try:
            category = input("Enter category to filter: ")
            filtered = self.data[self.data['Category'] == category]
            if filtered.empty:
                print("No data found for this category\n")
            else:
                print("\nFiltered Data:\n")
                print(filtered)
        except Exception as e:
            print("Error :",e)

    def display_summary(self):
        try:
            print("\n Summary:\n")
            print(self.data.describe())
        except exception as e:
            print("Error :",e)

    def bar_chart(self):
        try:
            category_sales = self.data.groupby('Category')['Total Sales'].sum()
            category_sales.plot(kind='bar')
            plt.title("Total Sales by Category")
            plt.xlabel("Category")
            plt.ylabel("Sales")
            plt.show()
        except exception as e:
            print("Error :",e)

    def Line_Chart(self):
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            daily_sales = self.data.groupby('Date')['Total Sales'].sum()
            daily_sales.plot()
            plt.title("Sales Trend Over Time")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.show()
        except exception as e:
            print("Error :",e)

    def Heatmap(self):
        try:
            corr = self.data[['Price', 'Quantity Sold', 'Total Sales']].corr()
            sns.heatmap(corr, annot=True)
            plt.title("Correlation Heatmap")
            plt.show()
        except Exception as e:
            print("Error :",e)
        
    def __del__(self):
        pass

ra = RetailAnalyzer()

while True:
    print("\nRetail Sales")
    print("1. load data")
    print("2. view matrics")
    print("3. Filter Data")
    print("4. Show Summary")
    print("5. Visualize Data")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        ra.load_data()
    elif choice == 2:
        ra.calculate_metrics()
    elif choice == 3:
        ra.filter_data()
    elif choice == 4:
        ra.display_summary()
    elif choice == 5:
        try:
            while True:
                print("visulaize data")
                print("1. bar chart")
                print("2. line chart")
                print("3. heatmap")
                print("4. go back")
                achoice = int(input("enter your choice: "))
                if achoice == 1:
                    ra.bar_chart()
                elif achoice == 2:
                    ra.line_chart()
                elif achoice == 3:
                    ra.Heatmap()                        
                elif achoice == 4:
                    print("\nReturning to Main Menu....\n")
                    break
                else:
                    print("\n Invalid choice\n")
        except Exception as e:
            print("error :",e)
            
        
    elif choice ==6:
        print("Exiting program")
        break
    else:
        print("\nInvalid choice!")