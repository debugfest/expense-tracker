#!/usr/bin/env python3
"""
Personal Expense Tracker - Main CLI Application

This is the main entry point for the Personal Expense Tracker application.
It provides a command-line interface for managing personal expenses.
"""

import sys
import os
from datetime import datetime, date
from typing import Optional, List
import argparse

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import ExpenseDatabase
from reports import ExpenseReports


class ExpenseTrackerCLI:
    """Command-line interface for the Personal Expense Tracker."""
    
    def __init__(self):
        """Initialize the CLI application."""
        self.db = ExpenseDatabase()
        self.reports = ExpenseReports(self.db)
        self._check_first_run()
    
    def _check_first_run(self) -> None:
        """Check if this is the first run and add sample data if needed."""
        stats = self.db.get_database_stats()
        if stats['total_expenses'] == 0:
            print("Welcome to Personal Expense Tracker!")
            print("This appears to be your first time using the app.")
            print("Adding sample data to get you started...")
            self.db.add_sample_data()
            print("Sample data added successfully!")
            print("You can now explore the features or add your own expenses.\n")
    
    def add_expense(self) -> None:
        """Add a new expense interactively."""
        print("\n" + "="*40)
        print("ADD NEW EXPENSE")
        print("="*40)
        
        try:
            # Get date
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date_input:
                expense_date = date.today().strftime("%Y-%m-%d")
            else:
                expense_date = date_input
            
            # Get category
            print("\nCommon categories: Food, Transportation, Entertainment, Utilities, Shopping, Healthcare")
            category = input("Enter category: ").strip()
            if not category:
                print("Error: Category cannot be empty.")
                return
            
            # Get description
            description = input("Enter description: ").strip()
            if not description:
                print("Error: Description cannot be empty.")
                return
            
            # Get amount
            amount_input = input("Enter amount: $").strip()
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("Error: Amount must be positive.")
                    return
            except ValueError:
                print("Error: Invalid amount. Please enter a valid number.")
                return
            
            # Add expense to database
            expense_id = self.db.add_expense(expense_date, category, description, amount)
            
            print(f"\n✅ Expense added successfully!")
            print(f"   ID: {expense_id}")
            print(f"   Date: {expense_date}")
            print(f"   Category: {category}")
            print(f"   Description: {description}")
            print(f"   Amount: ${amount:.2f}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def list_expenses(self, limit: Optional[int] = None) -> None:
        """List all expenses or a limited number."""
        print("\n" + "="*80)
        print("EXPENSE LIST")
        print("="*80)
        
        expenses = self.db.get_all_expenses()
        
        if not expenses:
            print("No expenses found.")
            return
        
        if limit:
            expenses = expenses[:limit]
            print(f"Showing last {len(expenses)} expenses:")
        else:
            print(f"Showing all {len(expenses)} expenses:")
        
        print("-"*80)
        print(f"{'ID':<4} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<10}")
        print("-"*80)
        
        for expense in expenses:
            description = expense['description'][:24] if len(expense['description']) > 24 else expense['description']
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['category']:<15} "
                  f"{description:<25} ${expense['amount']:<9.2f}")
        
        print("-"*80)
        print(f"Total: {len(expenses)} expenses")
    
    def delete_expense(self) -> None:
        """Delete an expense by ID."""
        print("\n" + "="*40)
        print("DELETE EXPENSE")
        print("="*40)
        
        try:
            expense_id_input = input("Enter expense ID to delete: ").strip()
            expense_id = int(expense_id_input)
            
            # Check if expense exists
            expense = self.db.get_expense_by_id(expense_id)
            if not expense:
                print(f"Error: Expense with ID {expense_id} not found.")
                return
            
            # Show expense details
            print(f"\nExpense to delete:")
            print(f"  ID: {expense['id']}")
            print(f"  Date: {expense['date']}")
            print(f"  Category: {expense['category']}")
            print(f"  Description: {expense['description']}")
            print(f"  Amount: ${expense['amount']:.2f}")
            
            # Confirm deletion
            confirm = input("\nAre you sure you want to delete this expense? (y/N): ").strip().lower()
            if confirm in ['y', 'yes']:
                if self.db.delete_expense(expense_id):
                    print("✅ Expense deleted successfully!")
                else:
                    print("Error: Failed to delete expense.")
            else:
                print("Deletion cancelled.")
                
        except ValueError:
            print("Error: Please enter a valid expense ID (number).")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def edit_expense(self) -> None:
        """Edit an existing expense by ID."""
        print("\n" + "="*40)
        print("EDIT EXPENSE")
        print("="*40)
        
        try:
            expense_id_input = input("Enter expense ID to edit: ").strip()
            expense_id = int(expense_id_input)
            
            expense = self.db.get_expense_by_id(expense_id)
            if not expense:
                print(f"Error: Expense with ID {expense_id} not found.")
                return
            
            print("\nLeave a field blank to keep the current value.")
            print(f"Current Date: {expense['date']}")
            new_date = input("New Date (YYYY-MM-DD): ").strip()
            
            print(f"Current Category: {expense['category']}")
            new_category = input("New Category: ").strip()
            
            print(f"Current Description: {expense['description']}")
            new_description = input("New Description: ").strip()
            
            print(f"Current Amount: ${expense['amount']:.2f}")
            new_amount_input = input("New Amount: $").strip()
            
            # Prepare updated values; only include changed fields
            update_kwargs = {}
            if new_date:
                update_kwargs['date'] = new_date
            if new_category:
                update_kwargs['category'] = new_category
            if new_description:
                update_kwargs['description'] = new_description
            if new_amount_input:
                try:
                    new_amount = float(new_amount_input)
                    if new_amount <= 0:
                        print("Error: Amount must be positive.")
                        return
                    update_kwargs['amount'] = new_amount
                except ValueError:
                    print("Error: Invalid amount. Please enter a valid number.")
                    return
            
            if not update_kwargs:
                print("No changes provided. Nothing to update.")
                return
            
            updated = self.db.update_expense(expense_id, **update_kwargs)
            if updated:
                updated_expense = self.db.get_expense_by_id(expense_id)
                print("\n✅ Expense updated successfully!")
                print(f"  ID: {updated_expense['id']}")
                print(f"  Date: {updated_expense['date']}")
                print(f"  Category: {updated_expense['category']}")
                print(f"  Description: {updated_expense['description']}")
                print(f"  Amount: ${updated_expense['amount']:.2f}")
            else:
                print("No changes were applied.")
        except ValueError:
            print("Error: Please enter a valid expense ID (number).")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def show_summaries(self) -> None:
        """Show category and monthly summaries."""
        print("\n" + "="*50)
        print("EXPENSE SUMMARIES")
        print("="*50)
        
        # Category summary
        self.reports.print_category_summary()
        
        # Monthly summary
        self.reports.print_monthly_summary()
    
    def show_charts(self) -> None:
        """Display various expense charts."""
        print("\n" + "="*40)
        print("EXPENSE CHARTS")
        print("="*40)
        
        stats = self.db.get_database_stats()
        if stats['total_expenses'] == 0:
            print("No expense data available for charts.")
            return
        
        while True:
            print("\nChart Options:")
            print("1. Category Bar Chart")
            print("2. Monthly Bar Chart")
            print("3. Category Pie Chart")
            print("4. Daily Trend Chart (Last 30 days)")
            print("5. All Charts")
            print("0. Back to main menu")
            
            choice = input("\nSelect chart option (0-5): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.reports.generate_category_chart()
            elif choice == '2':
                self.reports.generate_monthly_chart()
            elif choice == '3':
                self.reports.generate_pie_chart()
            elif choice == '4':
                self.reports.generate_trend_chart()
            elif choice == '5':
                print("Generating all charts...")
                self.reports.generate_category_chart()
                self.reports.generate_monthly_chart()
                self.reports.generate_pie_chart()
                self.reports.generate_trend_chart()
            else:
                print("Invalid option. Please try again.")
    
    def show_detailed_report(self) -> None:
        """Show a detailed expense report."""
        self.reports.print_detailed_report()
    
    def show_stats(self) -> None:
        """Show database statistics."""
        stats = self.db.get_database_stats()
        
        print("\n" + "="*40)
        print("DATABASE STATISTICS")
        print("="*40)
        print(f"Total Expenses: {stats['total_expenses']}")
        print(f"Total Amount: ${stats['total_amount']:.2f}")
        print(f"Categories: {stats['total_categories']}")
        
        if stats['total_expenses'] > 0:
            avg_expense = stats['total_amount'] / stats['total_expenses']
            print(f"Average per Expense: ${avg_expense:.2f}")
        
        print("="*40)
    
    def export_to_csv(self) -> None:
        """Export all expenses to a CSV file."""
        print("\n" + "="*40)
        print("EXPORT TO CSV")
        print("="*40)
        custom_path = input("Enter output CSV path (or press Enter for default): ").strip()
        try:
            output_path = self.reports.export_to_csv(custom_path or None)
            print(f"\n✅ Export successful! File saved at: {output_path}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error during export: {e}")
    
    def manage_budgets(self) -> None:
        """Manage budgets: set/update and view status."""
        while True:
            print("\n" + "="*40)
            print("BUDGETS")
            print("="*40)
            print("1. Set/Update Budget")
            print("2. View Budget Status")
            print("0. Back to main menu")
            choice = input("\nSelect option (0-2): ").strip()
            if choice == '0':
                break
            elif choice == '1':
                category = input("Category: ").strip()
                if not category:
                    print("Error: Category cannot be empty.")
                    continue
                period = input("Period (weekly/monthly/yearly): ").strip().lower()
                amount_input = input("Budget amount: $").strip()
                try:
                    amount = float(amount_input)
                    if amount < 0:
                        print("Error: Budget amount cannot be negative.")
                        continue
                    self.db.set_budget(category, period, amount)
                    print("✅ Budget saved.")
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
            elif choice == '2':
                period = input("Period (weekly/monthly/yearly): ").strip().lower()
                ref = input("Reference date YYYY-MM-DD (optional, Enter for today): ").strip()
                ref = ref or None
                self.reports.print_budget_status(period, ref)
            else:
                print("Invalid option. Please try again.")
    
    def run(self) -> None:
        """Run the main CLI loop."""
        print("Personal Expense Tracker")
        print("=" * 50)
        
        while True:
            print("\nMain Menu:")
            print("1. Add Expense")
            print("2. List Expenses")
            print("3. Delete Expense")
            print("4. Show Summaries")
            print("5. Show Charts")
            print("6. Detailed Report")
            print("7. Statistics")
            print("8. Export to CSV")
            print("9. Edit Expense")
            print("10. Budgets")
            print("0. Exit")
            
            choice = input("\nSelect option (0-10): ").strip()
            
            if choice == '0':
                print("\nThank you for using Personal Expense Tracker!")
                print("Goodbye! 👋")
                break
            elif choice == '1':
                self.add_expense()
            elif choice == '2':
                limit_input = input("Enter number of expenses to show (or press Enter for all): ").strip()
                limit = int(limit_input) if limit_input.isdigit() else None
                self.list_expenses(limit)
            elif choice == '3':
                self.delete_expense()
            elif choice == '4':
                self.show_summaries()
            elif choice == '5':
                self.show_charts()
            elif choice == '6':
                self.show_detailed_report()
            elif choice == '7':
                self.show_stats()
            elif choice == '8':
                self.export_to_csv()
            elif choice == '9':
                self.edit_expense()
            elif choice == '10':
                self.manage_budgets()
            else:
                print("Invalid option. Please try again.")


def main():
    """Main entry point for the application."""
    try:
        app = ExpenseTrackerCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
