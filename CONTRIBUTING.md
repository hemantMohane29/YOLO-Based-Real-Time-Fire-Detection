# Contributing to Fire Detection System

Thank you for your interest in contributing to the YOLO-Based Real-Time Fire Detection System! 

## How to Contribute

### 🐛 Reporting Bugs
- Use the GitHub Issues tab
- Include detailed steps to reproduce
- Provide system information (OS, Python version, etc.)
- Include error messages and logs

### 💡 Suggesting Features
- Open a GitHub Issue with the "enhancement" label
- Describe the feature and its benefits
- Include mockups or examples if applicable

### 🔧 Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Include docstrings for new functions
4. **Test your changes**
   ```bash
   python manage.py test
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### 📝 Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Keep functions small and focused
- Add type hints where appropriate
- Write clear commit messages

### 🧪 Testing
- Test your changes locally before submitting
- Include tests for new features
- Ensure existing tests still pass
- Test on both demo mode and full AI mode

### 📚 Documentation
- Update README.md if needed
- Add docstrings to new functions
- Update configuration examples
- Include usage examples for new features

## Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/YOLO-Based-Real-Time-Fire-Detection.git
   cd YOLO-Based-Real-Time-Fire-Detection/Fire_detector
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-full.txt  # or requirements.txt for demo mode
   ```

4. **Run the development server**
   ```bash
   cd Fire_detector
   python manage.py migrate
   python manage.py runserver
   ```

## Questions?

Feel free to open an issue for any questions about contributing!

Thank you for helping make this project better! 🔥