from setuptools import setup, find_packages

setup(
    name="ai-arena",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
        "mypy>=1.0.0",
        "pytest>=7.0.0"
    ],
    python_requires=">=3.8",
) 