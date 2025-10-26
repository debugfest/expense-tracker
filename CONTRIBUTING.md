# 🤝 Contributing to Personal Expense Tracker

Thank you for your interest in contributing! This guide will help you get started.

## 📜 Code of Conduct

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community

## 🚀 Getting Started

**Prerequisites:** Python 3.7+, Git, GitHub account

**Setup:**
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

# Add upstream remote
git remote add upstream https://github.com/debugfest/expense-tracker.git

# Create virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy

# Verify installation
python main.py        # Run application
python test_app.py    # Run test script
pytest               # Run tests
```

## 📁 Project Structure

- **`main.py`**: CLI interface and user interaction
- **`database.py`**: SQLite database operations
- **`reports.py`**: Report generation and visualizations
- **`test_app.py`**: Test script with sample data

## 📝 How to Contribute

**We welcome:**
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Tests and test coverage
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🔧 Code refactoring

**Before starting:**
1. Check existing issues
2. Create an issue for significant changes
3. Follow coding standards below

## 🎯 Priority TODOs

**High Priority:**
- Fix bug: program crashes with invalid category (2-3 hours)
- Add tests: `test_database.py` (6-8 hours)
- Excel/CSV export feature (4-6 hours)
- Streamlit UI version (8-12 hours)

**Medium Priority:**
- Google Sheets integration (10-15 hours)
- Rich CLI with colored output (4-6 hours)
- Budget tracking and alerts (8-10 hours)

**Lower Priority:**
- Receipt photo storage (12-15 hours)
- Multi-currency support (10-12 hours)
- Data backup and restore (6-8 hours)

## 📏 Coding Standards

**General:**
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write docstrings for all functions, classes, and modules
- Keep line length under 88 characters

**Tools:**
```bash
# Format code
black expense-tracker/

# Lint code
flake8 expense-tracker/

# Type checking
mypy expense-tracker/
```

## 🧪 Testing

**Create tests in `tests/` directory:**
- `test_database.py`, `test_reports.py`, `test_main.py`

**Naming:**
- Functions start with `test_`
- Use descriptive names like `test_add_expense_success`
- Group related tests in classes

**Running:**
```bash
pytest                              # Run all tests
pytest --cov --cov-report=html     # With coverage
pytest tests/test_database.py      # Specific file
```

## 🔄 Pull Request Process

**Steps:**
1. Create feature branch: `git checkout -b feature/your-feature-name`
2. Make changes following coding standards
3. Add tests for new functionality
4. Run tests and linting:
   ```bash
   pytest
   flake8 expense-tracker/
   black --check expense-tracker/
   mypy expense-tracker/
   ```
5. Commit and push: `git push origin feature/your-feature-name`

**PR Checklist:**
- [ ] Code follows coding standards
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests pass
- [ ] No linting errors

## 🐛 Issue Guidelines

**Bug Reports:**
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Error messages and stack traces

**Feature Requests:**
- Clear description and use case
- Proposed solution
- Alternatives considered

**Labels:** `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`

## 📚 Resources

- [Python Docs](https://docs.python.org/3/)
- [Matplotlib](https://matplotlib.org/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Pytest](https://docs.pytest.org/)
- [Streamlit](https://docs.streamlit.io/)
- [Black](https://black.readthedocs.io/)
- [Flake8](https://flake8.pycqa.org/)
- [MyPy](https://mypy.readthedocs.io/)

## 💬 Getting Help

- Check existing issues
- Read documentation and code comments
- Create a new issue with details
- Join GitHub Discussions

---

**Thank you for contributing!** 💰📊
