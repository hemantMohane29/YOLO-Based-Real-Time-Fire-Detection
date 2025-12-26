"""
Setup script for Fire Detection System Python Library
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fire-detection-system",
    version="1.0.0",
    author="Hemant Mohane",
    author_email="hemantmohane29@gmail.com",
    description="AI-powered real-time fire detection system with web dashboard and SMS alerts",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection",
    project_urls={
        "Bug Tracker": "https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection/issues",
        "Documentation": "https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection#readme",
        "Source Code": "https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "fire_detection": [
            "Fire_detector/static/*",
            "Fire_detector/ML_Model/*",
            "Fire_detector/Home/templates/Home/*",
            "Fire_detector/manage.py",
            "Fire_detector/Fire_detector/*.py",
            "Fire_detector/Home/*.py",
            "Fire_detector/Home/migrations/*.py",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Multimedia :: Video :: Capture",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "full": [
            "ultralytics>=8.0.0",
            "torch>=1.9.0",
            "torchvision>=0.10.0",
            "torchaudio>=0.9.0",
        ],
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "fire-detection=fire_detection.cli:main",
            "fire-detector=fire_detection.cli:main",
        ],
    },
    keywords=[
        "fire detection",
        "computer vision",
        "YOLO",
        "AI",
        "machine learning",
        "safety",
        "monitoring",
        "django",
        "opencv",
        "real-time",
    ],
    zip_safe=False,
)