"""
Database module for Personal Expense Tracker.

This module handles all database operations including creating tables,
inserting, updating, deleting, and querying expense data.
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from pathlib import Path


class ExpenseDatabase:
    """Handles all database operations for the expense tracker."""
    
    def __init__(self, db_path: str = "data/expenses.db"):
        """
        Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._ensure_data_directory()
        self._init_database()
    
    def _ensure_data_directory(self) -> None:
        """Create data directory if it doesn't exist."""
        data_dir = Path(self.db_path).parent
        data_dir.mkdir(exist_ok=True)
    
    def _init_database(self) -> None:
        """Initialize database and create tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create expenses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
    
    def add_expense(self, date: str, category: str, description: str, amount: float) -> int:
        """
        Add a new expense to the database.
        
        Args:
            date: Date of the expense (YYYY-MM-DD format)
            category: Category of the expense
            description: Description of the expense
            amount: Amount of the expense
            
        Returns:
            ID of the inserted expense
            
        Raises:
            ValueError: If amount is negative or invalid date format
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (date, category, description, amount)
                VALUES (?, ?, ?, ?)
            """, (date, category, description, amount))
            
            expense_id = cursor.lastrowid
            conn.commit()
            
        return expense_id
    
    def get_all_expenses(self) -> List[Dict]:
        """
        Retrieve all expenses from the database.
        
        Returns:
            List of dictionaries containing expense data
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, date, category, description, amount, created_at
                FROM expenses
                ORDER BY date DESC, created_at DESC
            """)
            
            expenses = []
            for row in cursor.fetchall():
                expenses.append(dict(row))
            
            return expenses
    
    def get_expense_by_id(self, expense_id: int) -> Optional[Dict]:
        """
        Retrieve a specific expense by ID.
        
        Args:
            expense_id: ID of the expense to retrieve
            
        Returns:
            Dictionary containing expense data or None if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, date, category, description, amount, created_at
                FROM expenses
                WHERE id = ?
            """, (expense_id,))
            
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_expense(self, expense_id: int, date: Optional[str] = None, category: Optional[str] = None,
                       description: Optional[str] = None, amount: Optional[float] = None) -> bool:
        """
        Update fields of an existing expense.
        
        Args:
            expense_id: ID of the expense to update
            date: New date (YYYY-MM-DD)
            category: New category
            description: New description
            amount: New amount
            
        Returns:
            True if an expense was updated, False otherwise
        """
        if date is None and category is None and description is None and amount is None:
            return False

        if date is not None:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")

        if amount is not None and amount < 0:
            raise ValueError("Amount cannot be negative")

        fields = []
        values = []
        if date is not None:
            fields.append("date = ?")
            values.append(date)
        if category is not None:
            fields.append("category = ?")
            values.append(category)
        if description is not None:
            fields.append("description = ?")
            values.append(description)
        if amount is not None:
            fields.append("amount = ?")
            values.append(amount)

        values.append(expense_id)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE expenses SET {', '.join(fields)} WHERE id = ?", values)
            updated = cursor.rowcount
            conn.commit()
            return updated > 0

    def delete_expense(self, expense_id: int) -> bool:
        """
        Delete an expense by ID.
        
        Args:
            expense_id: ID of the expense to delete
            
        Returns:
            True if expense was deleted, False if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            deleted_rows = cursor.rowcount
            
            conn.commit()
            
            return deleted_rows > 0
    
    def get_expenses_by_category(self) -> Dict[str, List[Dict]]:
        """
        Get all expenses grouped by category.
        
        Returns:
            Dictionary with categories as keys and lists of expenses as values
        """
        expenses = self.get_all_expenses()
        categorized = {}
        
        for expense in expenses:
            category = expense['category']
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(expense)
        
        return categorized
    
    def get_category_totals(self) -> Dict[str, float]:
        """
        Get total amount spent per category.
        
        Returns:
            Dictionary with categories as keys and total amounts as values
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT category, SUM(amount) as total
                FROM expenses
                GROUP BY category
                ORDER BY total DESC
            """)
            
            return dict(cursor.fetchall())
    
    def get_monthly_totals(self) -> Dict[str, float]:
        """
        Get total amount spent per month.
        
        Returns:
            Dictionary with months (YYYY-MM) as keys and total amounts as values
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT strftime('%Y-%m', date) as month, SUM(amount) as total
                FROM expenses
                GROUP BY month
                ORDER BY month DESC
            """)
            
            return dict(cursor.fetchall())
    
    def get_expenses_by_month(self, year: int, month: int) -> List[Dict]:
        """
        Get all expenses for a specific month.
        
        Args:
            year: Year (e.g., 2024)
            month: Month (1-12)
            
        Returns:
            List of expenses for the specified month
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, date, category, description, amount, created_at
                FROM expenses
                WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
                ORDER BY date DESC
            """, (str(year), f"{month:02d}"))
            
            expenses = []
            for row in cursor.fetchall():
                expenses.append(dict(row))
            
            return expenses
    
    def add_sample_data(self) -> None:
        """Add sample data for demonstration purposes."""
        sample_expenses = [
            ("2024-01-15", "Food", "Lunch at restaurant", 25.50),
            ("2024-01-16", "Transportation", "Bus ticket", 3.20),
            ("2024-01-17", "Entertainment", "Movie ticket", 12.00),
            ("2024-01-18", "Food", "Groceries", 45.30),
            ("2024-01-19", "Utilities", "Electricity bill", 85.00),
            ("2024-01-20", "Transportation", "Gas", 40.00),
            ("2024-01-21", "Food", "Coffee", 4.50),
            ("2024-01-22", "Entertainment", "Concert ticket", 75.00),
            ("2024-01-23", "Shopping", "New clothes", 120.00),
            ("2024-01-24", "Food", "Dinner out", 35.75),
        ]
        
        for date, category, description, amount in sample_expenses:
            try:
                self.add_expense(date, category, description, amount)
            except Exception as e:
                print(f"Error adding sample expense: {e}")
    
    def get_database_stats(self) -> Dict[str, int]:
        """
        Get basic statistics about the database.
        
        Returns:
            Dictionary with database statistics
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Total expenses
            cursor.execute("SELECT COUNT(*) FROM expenses")
            total_expenses = cursor.fetchone()[0]
            
            # Total amount
            cursor.execute("SELECT SUM(amount) FROM expenses")
            total_amount = cursor.fetchone()[0] or 0
            
            # Number of categories
            cursor.execute("SELECT COUNT(DISTINCT category) FROM expenses")
            total_categories = cursor.fetchone()[0]
            
            return {
                'total_expenses': total_expenses,
                'total_amount': total_amount,
                'total_categories': total_categories
            }


# TODO: Add option to export expenses to Excel or CSV
# TODO: Add Google Sheets integration for syncing
# TODO: Fix occasional bug: program crashes if invalid category is entered
# TODO: Add tests for database.py using pytest
