# 💰 Personal Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)


A Python application for tracking personal expenses with CLI interface, SQLite database, and matplotlib visualizations.

## ✨ Features

- **Expense Management**: Add, list, delete expenses with date, category, description, and amount
- **Analytics**: Category summaries, monthly trends, and database statistics
- **Charts**: Bar charts, pie charts, and daily trend visualizations
- **Auto-initialization**: Database and tables created automatically
- **Data Validation**: Comprehensive input validation

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/debugfest/expense-tracker.git
cd expense-tracker

# Create virtual environment (optional)
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Demo

```bash
python test_app.py
```

## 📖 Usage

**Main Menu:**
- Add, list, delete expenses
- Show category and monthly summaries
- Generate charts and detailed reports
- View database statistics

**Adding Expenses:**
Enter date (YYYY-MM-DD), category (Food, Transportation, etc.), description, and amount.

**Reports:**
Generate category bar charts, monthly bar charts, pie charts, and daily trend visualizations.

## 🏗️ Project Structure

- **`main.py`**: CLI entry point and user interface
- **`database.py`**: SQLite database operations
- **`reports.py`**: Report generation and matplotlib visualizations
- **`test_app.py`**: Test script with sample data
- **`data/expenses.db`**: SQLite database (auto-created)

## 🐛 Troubleshooting

**Common Issues:**
- Database errors: Ensure write permissions in project directory (`chmod 755 data/`)
- Matplotlib issues: Install `matplotlib[all]` or run `pip install --upgrade matplotlib`
- Import errors: Run `pip install -r requirements.txt` and verify Python 3.7+

**Input Format:**
- Date must be YYYY-MM-DD format (e.g., 2024-01-15)
- Amount must be a positive number
- Category and description cannot be empty

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick Start:**
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a Pull Request



**Acknowledgments:** [Matplotlib](https://matplotlib.org/), [SQLite](https://www.sqlite.org/)

---

**Made with ❤️ for personal finance management** 💰📊
