"""
Reports module for Personal Expense Tracker.

This module generates various reports and visualizations using matplotlib
for expense analysis and summaries.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import os
import csv
from pathlib import Path

from database import ExpenseDatabase


class ExpenseReports:
    """Handles generation of expense reports and visualizations."""
    
    def __init__(self, db: ExpenseDatabase):
        """
        Initialize the reports generator.
        
        Args:
            db: ExpenseDatabase instance
        """
        self.db = db
        self._setup_matplotlib()
    
    def export_to_csv(self, file_path: Optional[str] = None) -> str:
        """
        Export all expenses to a CSV file.
        
        Args:
            file_path: Optional path for the CSV file. If not provided, a file
                       will be created under an `exports/` directory with a
                       timestamped filename.
        
        Returns:
            The path to the written CSV file.
        """
        expenses = self.db.get_all_expenses()
        if not expenses:
            raise ValueError("No expenses available to export.")

        # Determine output path
        if file_path is None:
            exports_dir = Path("exports")
            exports_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = str(exports_dir / f"expenses_{timestamp}.csv")
        else:
            out_path = Path(file_path)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            file_path = str(out_path)

        # Write CSV
        fieldnames = ["id", "date", "category", "description", "amount", "currency", "created_at"]
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for exp in expenses:
                # Ensure only expected fields are written
                row = {key: exp.get(key, "") for key in fieldnames}
                writer.writerow(row)

        print(f"CSV exported to: {file_path}")
        return file_path

    def _setup_matplotlib(self) -> None:
        """Configure matplotlib for better visualizations."""
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.alpha'] = 0.3
    
    def generate_category_chart(self, save_path: Optional[str] = None) -> None:
        """
        Generate a bar chart showing expenses by category.
        
        Args:
            save_path: Optional path to save the chart image
        """
        category_totals = self.db.get_category_totals()
        
        if not category_totals:
            print("No expense data available for category chart.")
            return
        
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())
        
        # Create the bar chart
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(categories, amounts, color='skyblue', edgecolor='navy', alpha=0.7)
        
        # Customize the chart
        ax.set_title('Expenses by Category', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Category', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, amount in zip(bars, amounts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(amounts)*0.01,
                   f'${amount:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Category chart saved to: {save_path}")
        
        plt.show()
    
    def print_budget_status(self, period: str, reference_date: Optional[str] = None) -> None:
        """Print budget utilization per category for a given period."""
        period = period.lower()
        if period not in ("weekly", "monthly", "yearly"):
            print("Error: Period must be weekly, monthly, or yearly.")
            return
        budgets = self.db.get_all_budgets(period)
        if not budgets:
            print(f"No budgets configured for {period} period.")
            return
        spent_by_category = self.db.get_spent_by_category_for_period(period, reference_date)
        print("\n" + "="*60)
        print(f"BUDGET STATUS ({period.upper()})")
        print("="*60)
        print(f"{'Category':<18} {'Budget':>10} {'Spent':>10} {'Remain':>10} {'Used%':>7}")
        print("-"*60)
        for b in budgets:
            category = b['category']
            budget_amount = float(b['amount'])
            spent = float(spent_by_category.get(category, 0.0))
            remain = budget_amount - spent
            used_pct = (spent / budget_amount * 100) if budget_amount > 0 else 0.0
            status_line = f"{category:<18} ${budget_amount:>9.2f} ${spent:>9.2f} ${remain:>9.2f} {used_pct:>6.1f}%"
            if remain < 0:
                status_line += "  OVER"
            print(status_line)
        print("="*60)

    def generate_monthly_chart(self, save_path: Optional[str] = None) -> None:
        """
        Generate a bar chart showing expenses by month.
        
        Args:
            save_path: Optional path to save the chart image
        """
        monthly_totals = self.db.get_monthly_totals()
        
        if not monthly_totals:
            print("No expense data available for monthly chart.")
            return
        
        # Sort months chronologically
        sorted_months = sorted(monthly_totals.items())
        months = [item[0] for item in sorted_months]
        amounts = [item[1] for item in sorted_months]
        
        # Create the bar chart
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(months, amounts, color='lightcoral', edgecolor='darkred', alpha=0.7)
        
        # Customize the chart
        ax.set_title('Monthly Expenses', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, amount in zip(bars, amounts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(amounts)*0.01,
                   f'${amount:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Monthly chart saved to: {save_path}")
        
        plt.show()
    
    def generate_pie_chart(self, save_path: Optional[str] = None) -> None:
        """
        Generate a pie chart showing expense distribution by category.
        
        Args:
            save_path: Optional path to save the chart image
        """
        category_totals = self.db.get_category_totals()
        
        if not category_totals:
            print("No expense data available for pie chart.")
            return
        
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())
        
        # Create the pie chart
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = plt.cm.Set3(range(len(categories)))
        
        wedges, texts, autotexts = ax.pie(amounts, labels=categories, autopct='%1.1f%%',
                                         colors=colors, startangle=90)
        
        # Customize the chart
        ax.set_title('Expense Distribution by Category', fontsize=16, fontweight='bold', pad=20)
        
        # Improve text readability
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Pie chart saved to: {save_path}")
        
        plt.show()
    
    def generate_trend_chart(self, days: int = 30, save_path: Optional[str] = None) -> None:
        """
        Generate a line chart showing expense trends over time.
        
        Args:
            days: Number of days to show in the trend
            save_path: Optional path to save the chart image
        """
        # Get expenses from the last N days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        expenses = self.db.get_all_expenses()
        
        # Filter expenses by date range
        filtered_expenses = []
        for expense in expenses:
            expense_date = datetime.strptime(expense['date'], '%Y-%m-%d')
            if start_date <= expense_date <= end_date:
                filtered_expenses.append(expense)
        
        if not filtered_expenses:
            print(f"No expense data available for the last {days} days.")
            return
        
        # Group expenses by date
        daily_totals = {}
        for expense in filtered_expenses:
            date = expense['date']
            if date not in daily_totals:
                daily_totals[date] = 0
            daily_totals[date] += expense['amount']
        
        # Sort dates
        sorted_dates = sorted(daily_totals.items())
        dates = [datetime.strptime(item[0], '%Y-%m-%d') for item in sorted_dates]
        amounts = [item[1] for item in sorted_dates]
        
        # Create the line chart
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(dates, amounts, marker='o', linewidth=2, markersize=6, color='green')
        
        # Customize the chart
        ax.set_title(f'Daily Expense Trend (Last {days} Days)', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        
        # Format x-axis dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, days//10)))
        plt.xticks(rotation=45)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Trend chart saved to: {save_path}")
        
        plt.show()
    
    def print_category_summary(self) -> None:
        """Print a formatted summary of expenses by category."""
        category_totals = self.db.get_category_totals()
        
        if not category_totals:
            print("No expense data available.")
            return
        
        print("\n" + "="*50)
        print("CATEGORY SUMMARY")
        print("="*50)
        
        total_amount = sum(category_totals.values())
        
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_amount) * 100
            print(f"{category:<20} ${amount:>8.2f} ({percentage:>5.1f}%)")
        
        print("-"*50)
        print(f"{'TOTAL':<20} ${total_amount:>8.2f}")
        print("="*50)
    
    def print_monthly_summary(self) -> None:
        """Print a formatted summary of expenses by month."""
        monthly_totals = self.db.get_monthly_totals()
        
        if not monthly_totals:
            print("No expense data available.")
            return
        
        print("\n" + "="*50)
        print("MONTHLY SUMMARY")
        print("="*50)
        
        total_amount = sum(monthly_totals.values())
        
        for month, amount in sorted(monthly_totals.items(), reverse=True):
            percentage = (amount / total_amount) * 100
            print(f"{month:<15} ${amount:>8.2f} ({percentage:>5.1f}%)")
        
        print("-"*50)
        print(f"{'TOTAL':<15} ${total_amount:>8.2f}")
        print("="*50)
    
    def print_detailed_report(self) -> None:
        """Print a comprehensive expense report."""
        expenses = self.db.get_all_expenses()
        stats = self.db.get_database_stats()
        
        if not expenses:
            print("No expense data available.")
            return
        
        print("\n" + "="*60)
        print("DETAILED EXPENSE REPORT")
        print("="*60)
        
        # Overall statistics
        print(f"Total Expenses: {stats['total_expenses']}")
        print(f"Total Amount: ${stats['total_amount']:.2f}")
        print(f"Categories: {stats['total_categories']}")
        print(f"Average per Expense: ${stats['total_amount']/stats['total_expenses']:.2f}")
        
        # Recent expenses
        print(f"\nRecent Expenses (Last 10):")
        print("-"*60)
        print(f"{'ID':<4} {'Date':<12} {'Category':<15} {'Description':<20} {'Amount':<10}")
        print("-"*60)
        
        for expense in expenses[:10]:
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['category']:<15} "
                  f"{expense['description'][:19]:<20} ${expense['amount']:<9.2f}")
        
        if len(expenses) > 10:
            print(f"... and {len(expenses) - 10} more expenses")
        
        print("="*60)


# TODO: Add Streamlit UI version for web visualization
# TODO: Improve CLI experience (colored output using rich)
