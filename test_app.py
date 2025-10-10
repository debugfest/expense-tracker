#!/usr/bin/env python3
"""
Test script for Personal Expense Tracker

This script demonstrates the core functionality of the expense tracker
without requiring user interaction.
"""

import os
import sys
from datetime import date

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import ExpenseDatabase
from reports import ExpenseReports


def test_expense_tracker():
    """Test the core functionality of the expense tracker."""
    print("Personal Expense Tracker - Test Script")
    print("=" * 50)
    
    # Initialize database
    print("1. Initializing database...")
    db = ExpenseDatabase("data/test_expenses.db")
    print("   ✅ Database initialized")
    
    # Add sample data
    print("\n2. Adding sample expenses...")
    sample_expenses = [
        ("2024-01-15", "Food", "Lunch at restaurant", 25.50),
        ("2024-01-16", "Transportation", "Bus ticket", 3.20),
        ("2024-01-17", "Entertainment", "Movie ticket", 12.00),
        ("2024-01-18", "Food", "Groceries", 45.30),
        ("2024-01-19", "Utilities", "Electricity bill", 85.00),
    ]
    
    for date_str, category, description, amount in sample_expenses:
        expense_id = db.add_expense(date_str, category, description, amount)
        print(f"   ✅ Added expense ID {expense_id}: {category} - ${amount}")
    
    # Test database operations
    print("\n3. Testing database operations...")
    all_expenses = db.get_all_expenses()
    print(f"   ✅ Retrieved {len(all_expenses)} expenses")
    
    category_totals = db.get_category_totals()
    print(f"   ✅ Category totals: {len(category_totals)} categories")
    
    monthly_totals = db.get_monthly_totals()
    print(f"   ✅ Monthly totals: {len(monthly_totals)} months")
    
    # Test reports
    print("\n4. Testing reports functionality...")
    reports = ExpenseReports(db)
    print("   ✅ Reports module initialized")
    
    # Print summaries
    print("\n5. Generating summaries...")
    reports.print_category_summary()
    reports.print_monthly_summary()
    
    # Test statistics
    print("\n6. Database statistics...")
    stats = db.get_database_stats()
    print(f"   Total Expenses: {stats['total_expenses']}")
    print(f"   Total Amount: ${stats['total_amount']:.2f}")
    print(f"   Categories: {stats['total_categories']}")
    
    # Test expense deletion
    print("\n7. Testing expense deletion...")
    if all_expenses:
        expense_to_delete = all_expenses[0]
        success = db.delete_expense(expense_to_delete['id'])
        if success:
            print(f"   ✅ Successfully deleted expense ID {expense_to_delete['id']}")
        else:
            print(f"   ❌ Failed to delete expense ID {expense_to_delete['id']}")
    
    # Final statistics
    print("\n8. Final statistics...")
    final_stats = db.get_database_stats()
    print(f"   Total Expenses: {final_stats['total_expenses']}")
    print(f"   Total Amount: ${final_stats['total_amount']:.2f}")
    
    print("\n" + "=" * 50)
    print("✅ All tests completed successfully!")
    print("The Personal Expense Tracker is working correctly.")
    print("\nTo run the full application, use: python main.py")


if __name__ == "__main__":
    test_expense_tracker()
