# 🤝 Contributing to Fire Detection System

Thank you for your interest in contributing to the Fire Detection System! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic knowledge of Django, OpenCV, and AI/ML concepts
- Webcam for testing

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOLO-Based-Real-Time-Fire-Detection.git
   cd YOLO-Based-Real-Time-Fire-Detection/Fire_detector
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements-full.txt
   ```

4. **Download Model**
   ```bash
   python download_model.py
   ```

5. **Run Development Server**
   ```bash
   cd Fire_detector
   python manage.py migrate
   python manage.py runserver
   ```

## 📋 How to Contribute

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** describing the issue
- **Steps to reproduce** the behavior
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, browser)
- **Error messages** or logs

### 💡 Suggesting Features

Feature requests are welcome! Please:

- **Check existing issues** to avoid duplicates
- **Describe the feature** clearly
- **Explain the use case** and benefits
- **Consider implementation** complexity

### 🔧 Code Contributions

#### Pull Request Process

1. **Create a branch** from `master`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes** thoroughly
   ```bash
   python manage.py test
   python test_camera.py
   ```

4. **Update documentation** if needed

5. **Commit with clear messages**
   ```bash
   git commit -m "Add: New fire detection algorithm"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

#### Coding Standards

- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use modern ES6+ syntax
- **HTML/CSS**: Semantic markup, responsive design
- **Comments**: Clear, concise documentation
- **Variables**: Descriptive names

#### Code Review Checklist

- [ ] Code follows project style guidelines
- [ ] Changes are tested and working
- [ ] Documentation is updated
- [ ] No breaking changes (or clearly documented)
- [ ] Performance impact considered
- [ ] Security implications reviewed

## 🎯 Areas for Contribution

### 🔥 High Priority
- **AI Model Improvements** - Better fire detection accuracy
- **Performance Optimization** - Reduce memory usage, faster processing
- **Mobile Support** - Responsive design improvements
- **Testing** - Unit tests, integration tests
- **Documentation** - API docs, tutorials

### 🛠️ Medium Priority
- **New Features** - Smoke detection, heat detection
- **Integrations** - Slack, Discord, email alerts
- **Deployment** - Docker, Kubernetes support
- **Monitoring** - Metrics, logging improvements

### 🎨 Low Priority
- **UI/UX** - Design improvements, animations
- **Localization** - Additional language support
- **Accessibility** - Screen reader support, keyboard navigation

## 🧪 Testing

### Running Tests
```bash
# Django tests
python manage.py test

# Camera tests
python test_camera.py

# Manual testing
python manage.py runserver
# Open http://localhost:8000 and test all features
```

### Test Coverage
- **Unit Tests** - Individual functions and methods
- **Integration Tests** - Component interactions
- **End-to-End Tests** - Full user workflows
- **Performance Tests** - Memory usage, response times

## 📚 Documentation

### Types of Documentation
- **Code Comments** - Inline explanations
- **Docstrings** - Function/class documentation
- **README** - Project overview and setup
- **API Docs** - Endpoint documentation
- **User Guides** - How-to tutorials

### Documentation Standards
- Clear, concise language
- Code examples where helpful
- Screenshots for UI changes
- Keep documentation up-to-date

## 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to docs
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `priority: high` - Critical issues
- `priority: medium` - Important improvements
- `priority: low` - Nice to have features

## 📞 Getting Help

### Communication Channels
- **GitHub Issues** - Bug reports, feature requests
- **GitHub Discussions** - General questions, ideas
- **Email** - Direct contact for sensitive issues

### Response Times
- **Bug reports** - Within 48 hours
- **Feature requests** - Within 1 week
- **Pull requests** - Within 1 week

## 📜 Code of Conduct

### Our Standards
- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Focus on the code**, not the person
- **Help others** learn and grow

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing private information
- Spam or off-topic content

## 🎉 Recognition

Contributors will be:
- **Listed** in the README.md
- **Credited** in release notes
- **Thanked** publicly for significant contributions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make this project better. Whether you're fixing a typo, reporting a bug, or adding a major feature, your help is appreciated!

**Happy Contributing!** 🔥🚨