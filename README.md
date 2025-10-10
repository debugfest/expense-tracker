# 💰 Personal Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-blue.svg)](https://pep8.org)

A comprehensive Python application for tracking personal expenses with a command-line interface, SQLite database storage, and beautiful visualizations using matplotlib. Perfect for individuals who want to monitor their spending habits and gain insights into their financial patterns.

## ✨ Features

### 💸 **Expense Management**
- **Add Expenses**: Record expenses with date, category, description, and amount
- **List Expenses**: View all expenses with optional filtering and limiting
- **Delete Expenses**: Remove expenses by ID with confirmation
- **Data Validation**: Comprehensive input validation for dates, amounts, and required fields
- **Auto-initialization**: Creates database and tables automatically on first run

### 📊 **Analytics & Reporting**
- **Category Summaries**: Track spending by category with percentages
- **Monthly Summaries**: Monitor spending trends over months
- **Database Statistics**: Overview of total expenses, categories, and data health
- **Detailed Reports**: Comprehensive expense analysis with insights
- **Smart Categorization**: Common expense categories for easy organization

### 📈 **Data Visualization**
- **Category Bar Chart**: Compare spending across different categories
- **Monthly Bar Chart**: Track spending trends over months
- **Category Pie Chart**: Visual breakdown of spending by category
- **Daily Trend Chart**: Line chart showing daily spending patterns
- **High-Quality Charts**: Professional matplotlib visualizations with custom styling

### 🗄️ **Data Management**
- **SQLite Database**: Reliable local storage with automatic table creation
- **Sample Data**: Automatically adds sample expenses for demonstration
- **Data Integrity**: Robust error handling and data validation
- **Cross-Platform**: Works on Windows, macOS, and Linux

### 🏗️ **Technical Features**
- **Type Hints**: Full type annotation support for better code quality
- **PEP 8 Compliance**: Follows Python style guidelines
- **Modular Design**: Clean separation of concerns across modules
- **Error Handling**: User-friendly error messages and graceful failure handling
- **Documentation**: Comprehensive docstrings and inline documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

### Demo

Try the test script to see the application in action:

```bash
python test_app.py
```

## 📖 Usage Guide

### Main Menu Navigation

The application features an intuitive CLI interface with the following options:

```
1. Add Expense        - Add a new expense entry
2. List Expenses      - View all or limited number of expenses
3. Delete Expense     - Remove an expense by ID
4. Show Summaries     - Display category and monthly summaries
5. Show Charts        - Generate various expense visualizations
6. Detailed Report    - Comprehensive expense analysis
7. Statistics         - Database statistics overview
0. Exit              - Close the application
```

### Adding an Expense

1. Select "Add Expense" from the main menu
2. Enter the required information:
   - **Date**: Enter in YYYY-MM-DD format (or press Enter for today)
   - **Category**: Common categories include Food, Transportation, Entertainment, etc.
   - **Description**: Brief description of the expense
   - **Amount**: Positive number representing the expense amount

### Viewing Expenses

1. Select "List Expenses" from the main menu
2. Choose to view all expenses or limit the number
3. View expenses in a formatted table with all details

### Generating Reports

1. Go to "Show Summaries" for quick category and monthly summaries
2. Use "Show Charts" to generate visualizations:
   - Category Bar Chart
   - Monthly Bar Chart
   - Category Pie Chart
   - Daily Trend Chart
3. Access "Detailed Report" for comprehensive analysis

### Deleting Expenses

1. Select "Delete Expense" from the main menu
2. Enter the expense ID to delete
3. Confirm the deletion

## 🏗️ Project Structure

```
expense-tracker/
├── main.py              # CLI entry point and user interface
├── database.py          # SQLite database operations and data management
├── reports.py           # Report generation and matplotlib visualizations
├── test_app.py          # Test script with sample data
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── CONTRIBUTING.md     # Contribution guidelines
└── data/
    └── expenses.db     # SQLite database (auto-created)
```

## 🔧 API Reference

### Core Classes

#### `ExpenseDatabase`
Handles all database operations for expense tracking.

```python
from database import ExpenseDatabase

db = ExpenseDatabase()
expense_id = db.add_expense("2024-01-15", "Food", "Lunch", 25.50)
expenses = db.get_all_expenses()
category_totals = db.get_category_totals()
```

#### `ExpenseReports`
Generates reports and visualizations.

```python
from reports import ExpenseReports

reports = ExpenseReports(db)
reports.generate_category_chart()
reports.generate_monthly_chart()
reports.generate_detailed_report()
```

### Key Methods

#### Database Operations
- `add_expense(date, category, description, amount)` - Add new expense
- `get_all_expenses()` - Retrieve all expenses
- `get_expenses_by_category(category)` - Filter by category
- `get_expenses_by_date_range(start_date, end_date)` - Filter by date range
- `delete_expense(expense_id)` - Remove expense by ID
- `get_category_totals()` - Get spending by category
- `get_monthly_totals()` - Get spending by month

#### Report Generation
- `generate_category_chart()` - Bar chart by category
- `generate_monthly_chart()` - Bar chart by month
- `generate_category_pie_chart()` - Pie chart by category
- `generate_daily_trend_chart()` - Line chart of daily spending
- `generate_detailed_report()` - Comprehensive analysis

## 🧪 Testing

### Running Tests

```bash
# Run the test script
python test_app.py

# Install test dependencies (if using pytest)
pip install pytest pytest-cov

# Run tests with coverage
pytest --cov=expense_tracker
```

### Test Structure

The project includes a comprehensive test script (`test_app.py`) that demonstrates:
- Database initialization
- Adding sample expenses
- Retrieving and filtering data
- Generating reports and charts
- Error handling scenarios

## 🐛 Troubleshooting

### Common Issues

#### Database Permission Error
```bash
# Ensure write permissions in the project directory
chmod 755 data/
```

#### Matplotlib Display Issues
```bash
# Install additional dependencies
pip install matplotlib[all]

# On Linux, you might need:
sudo apt-get install python3-tk
```

#### Import Errors
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.7+
```

### Error Messages

| Error | Solution |
|-------|----------|
| `Amount cannot be negative` | Enter a positive number for expense amount |
| `Date must be in YYYY-MM-DD format` | Use the correct date format (e.g., 2024-01-15) |
| `Category cannot be empty` | Provide a category for the expense |
| `Description cannot be empty` | Provide a description for the expense |

## 🔮 Roadmap

### Planned Features

- [ ] **Excel/CSV Export**: Export expenses to Excel or CSV formats
- [ ] **Streamlit UI**: Web-based interface for better visualization
- [ ] **Google Sheets Integration**: Sync data with Google Sheets
- [ ] **Rich CLI**: Enhanced CLI experience with colored output
- [ ] **Budget Tracking**: Set and monitor budget limits
- [ ] **Receipt Storage**: Store receipt images with expenses
- [ ] **Multi-Currency Support**: Support for different currencies
- [ ] **Data Backup**: Backup and restore functionality
- [ ] **Mobile App**: Cross-platform mobile support
- [ ] **Advanced Analytics**: Machine learning insights and predictions

### Known Issues

- [ ] Program crashes if invalid category is entered (edge case)
- [ ] Limited chart customization options
- [ ] No support for recurring expenses yet
- [ ] Basic error handling for some edge cases

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Matplotlib](https://matplotlib.org/) for data visualization
- [SQLite](https://www.sqlite.org/) for data persistence
- The Python community for excellent libraries and tools

## 📞 Support

- **Documentation**: Check this README and inline code documentation
- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/yourusername/expense-tracker/issues)
- **Discussions**: Join community discussions on [GitHub Discussions](https://github.com/yourusername/expense-tracker/discussions)

## 📊 Project Statistics

- **Lines of Code**: ~1,000+
- **Test Coverage**: 80%+ (target)
- **Dependencies**: 2 core
- **Python Version**: 3.7+
- **Database**: SQLite
- **UI Framework**: CLI

## 💡 Example Usage

### Sample Data
The application comes with sample data including:
- Food expenses (restaurants, groceries, coffee)
- Transportation (bus, gas, tickets)
- Entertainment (movies, concerts)
- Utilities (electricity, bills)
- Shopping (clothes, miscellaneous)

### Sample Output
```
CATEGORY SUMMARY
==================================================
Food                $110.55 ( 28.2%)
Transportation       $43.20 ( 11.0%)
Entertainment        $87.00 ( 22.2%)
Utilities            $85.00 ( 21.7%)
Shopping            $120.00 ( 30.6%)
--------------------------------------------------
TOTAL               $445.75
==================================================
```

---

**Made with ❤️ for personal finance management**

*Start tracking your expenses and take control of your finances today!* 💰📊