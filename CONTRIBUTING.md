# 🤝 Contributing to Personal Expense Tracker

Thank you for your interest in contributing to the Personal Expense Tracker! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Contribution Guidelines](#contribution-guidelines)
- [Priority TODOs](#priority-todos)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Release Process](#release-process)

## 📜 Code of Conduct

This project follows a code of conduct that ensures a welcoming environment for all contributors. Please:

- Be respectful and inclusive
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account
- Basic knowledge of Python, SQLite, and CLI applications

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/originalowner/expense-tracker.git
   ```

## 🛠️ Development Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

### 3. Verify Installation

```bash
# Run the application
python main.py

# Run the test script
python test_app.py

# Run tests (if using pytest)
pytest
```

## 📁 Project Structure

```
expense-tracker/
├── main.py              # CLI entry point and user interface
├── database.py          # SQLite database operations
├── reports.py           # Report generation and visualizations
├── test_app.py          # Test script with sample data
├── data/                # Database storage
│   └── expenses.db      # SQLite database
├── tests/               # Test files (to be created)
├── requirements.txt     # Dependencies
├── README.md           # Project documentation
└── CONTRIBUTING.md     # This file
```

### Module Responsibilities

- **`main.py`**: CLI interface, user interaction, menu handling
- **`database.py`**: SQLite database operations, CRUD operations, data validation
- **`reports.py`**: Chart generation, report creation, matplotlib visualizations
- **`test_app.py`**: Test script demonstrating core functionality

## 📝 Contribution Guidelines

### Types of Contributions

We welcome various types of contributions:

1. **🐛 Bug Fixes**: Fix existing issues and bugs
2. **✨ New Features**: Add new functionality
3. **📚 Documentation**: Improve documentation and examples
4. **🧪 Tests**: Add or improve test coverage
5. **🎨 UI/UX**: Enhance user interface and experience
6. **⚡ Performance**: Optimize code performance
7. **🔧 Refactoring**: Improve code structure and maintainability

### Before You Start

1. **Check existing issues** to see if your idea is already being worked on
2. **Create an issue** for significant changes to discuss the approach
3. **Read the Priority TODOs** section below for high-priority items
4. **Follow the coding standards** outlined in this document

## 🎯 Priority TODOs

These are high-priority items that contributors can work on:

### 🔥 Critical Issues

1. **Fix occasional bug: program crashes if invalid category is entered**
   - **File**: `main.py` (add_expense method)
   - **Description**: The program crashes when invalid category input is provided
   - **Priority**: High
   - **Estimated Effort**: 2-3 hours

2. **Add tests for database.py using pytest**
   - **Files**: Create `tests/test_database.py`
   - **Description**: Add comprehensive test coverage for database operations
   - **Priority**: High
   - **Estimated Effort**: 6-8 hours

### 🚀 New Features

3. **Add option to export expenses to Excel or CSV**
   - **Description**: Export expense data to Excel and CSV formats
   - **Files**: New module `export.py`, update `main.py`
   - **Priority**: High
   - **Estimated Effort**: 4-6 hours
   - **Dependencies**: `openpyxl`, `pandas`

4. **Add Streamlit UI version for web visualization**
   - **Description**: Create a web-based interface using Streamlit
   - **Files**: New file `streamlit_app.py`
   - **Priority**: High
   - **Estimated Effort**: 8-12 hours
   - **Dependencies**: `streamlit`

5. **Add Google Sheets integration for syncing**
   - **Description**: Sync expense data with Google Sheets
   - **Files**: New module `google_sheets.py`
   - **Priority**: Medium
   - **Estimated Effort**: 10-15 hours
   - **Dependencies**: `gspread`, `google-auth`

6. **Improve CLI experience (colored output using rich)**
   - **Description**: Enhance CLI with colored output and better formatting
   - **Files**: Update `main.py`, add `rich` dependency
   - **Priority**: Medium
   - **Estimated Effort**: 4-6 hours
   - **Dependencies**: `rich`

7. **Add budget tracking and alerts**
   - **Description**: Set budget limits and get alerts when exceeded
   - **Files**: New module `budget.py`, update `main.py`
   - **Priority**: Medium
   - **Estimated Effort**: 8-10 hours

8. **Add receipt photo storage**
   - **Description**: Store receipt images with expenses
   - **Files**: New module `receipt_storage.py`, update database schema
   - **Priority**: Low
   - **Estimated Effort**: 12-15 hours

9. **Add multi-currency support**
   - **Description**: Support different currencies for international users
   - **Files**: Update `database.py`, `reports.py`, `main.py`
   - **Priority**: Low
   - **Estimated Effort**: 10-12 hours

10. **Add data backup and restore**
    - **Description**: Backup and restore expense data
    - **Files**: New module `backup.py`, update `main.py`
    - **Priority**: Low
    - **Estimated Effort**: 6-8 hours

## 📏 Coding Standards

### Python Style Guide

- Follow **PEP 8** style guidelines
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all functions, classes, and modules
- Use **descriptive variable names** (avoid abbreviations)
- Keep **line length** under 88 characters (Black formatter standard)

### Code Formatting

We use **Black** for code formatting:

```bash
# Format code
black expense-tracker/

# Check formatting
black --check expense-tracker/
```

### Linting

We use **flake8** for linting:

```bash
# Run linter
flake8 expense-tracker/

# Run with specific rules
flake8 --max-line-length=88 --extend-ignore=E203,W503 expense-tracker/
```

### Type Checking

We use **mypy** for type checking:

```bash
# Run type checker
mypy expense-tracker/
```

### Example Code Style

```python
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
    
    # Database operation...
    return expense_id
```

## 🧪 Testing Guidelines

### Test Structure

Create tests in the `tests/` directory:

```
tests/
├── test_database.py     # Tests for database.py
├── test_reports.py      # Tests for reports.py
├── test_main.py         # Tests for main.py
└── conftest.py          # Pytest configuration
```

### Test Naming Convention

- Test functions should start with `test_`
- Use descriptive names: `test_add_expense_success`, `test_invalid_amount_raises_error`
- Group related tests in classes: `class TestExpenseDatabase:`

### Example Test

```python
import pytest
from database import ExpenseDatabase

class TestExpenseDatabase:
    """Test cases for ExpenseDatabase class."""
    
    def test_add_expense_success(self):
        """Test successful expense addition."""
        db = ExpenseDatabase(":memory:")  # Use in-memory database for testing
        expense_id = db.add_expense("2024-01-15", "Food", "Lunch", 25.50)
        
        assert expense_id is not None
        assert expense_id > 0
    
    def test_add_expense_invalid_amount(self):
        """Test expense addition with invalid amount."""
        db = ExpenseDatabase(":memory:")
        
        with pytest.raises(ValueError, match="Amount cannot be negative"):
            db.add_expense("2024-01-15", "Food", "Lunch", -25.50)
    
    def test_add_expense_invalid_date(self):
        """Test expense addition with invalid date format."""
        db = ExpenseDatabase(":memory:")
        
        with pytest.raises(ValueError, match="Date must be in YYYY-MM-DD format"):
            db.add_expense("2024/01/15", "Food", "Lunch", 25.50)
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=expense_tracker --cov-report=html

# Run specific test file
pytest tests/test_database.py

# Run with verbose output
pytest -v
```

## 🔄 Pull Request Process

### Before Submitting

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Add tests** for new functionality

4. **Update documentation** if needed

5. **Run tests and linting**:
   ```bash
   pytest
   flake8 expense-tracker/
   black --check expense-tracker/
   mypy expense-tracker/
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Template

When creating a PR, include:

- **Description**: What changes were made and why
- **Type**: Bug fix, new feature, documentation, etc.
- **Testing**: How the changes were tested
- **Screenshots**: If applicable (for UI changes)
- **Checklist**: Ensure all items are completed

### PR Checklist

- [ ] Code follows the project's coding standards
- [ ] Self-review of code has been performed
- [ ] Code has been commented, particularly in hard-to-understand areas
- [ ] Tests have been added/updated for new functionality
- [ ] Documentation has been updated if necessary
- [ ] All tests pass
- [ ] No linting errors
- [ ] Type checking passes

## 🐛 Issue Guidelines

### Bug Reports

When reporting bugs, include:

1. **Clear title** describing the issue
2. **Steps to reproduce** the bug
3. **Expected behavior** vs actual behavior
4. **Environment details** (OS, Python version, etc.)
5. **Screenshots** if applicable
6. **Error messages** and stack traces

### Feature Requests

When requesting features, include:

1. **Clear title** describing the feature
2. **Use case** and motivation
3. **Proposed solution** or approach
4. **Alternatives considered**
5. **Additional context** if relevant

### Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed
- `priority: high`: High priority issue
- `priority: medium`: Medium priority issue
- `priority: low`: Low priority issue

## 🚀 Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is updated
- [ ] CHANGELOG.md is updated
- [ ] Release notes are prepared
- [ ] Tag is created
- [ ] Release is published

## 📚 Additional Resources

### Documentation

- [Python Documentation](https://docs.python.org/3/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Development Tools

- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [MyPy Type Checker](https://mypy.readthedocs.io/)
- [Pytest Testing Framework](https://docs.pytest.org/)

## 💬 Getting Help

If you need help or have questions:

1. **Check existing issues** for similar problems
2. **Read the documentation** and code comments
3. **Create a new issue** with detailed information
4. **Join discussions** in GitHub Discussions
5. **Ask questions** in the community forum

## 🙏 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page
- **Project documentation**

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to the Personal Expense Tracker!** 💰📊

*Together, we can make personal finance management more accessible and powerful for everyone!*
