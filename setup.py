"""
任务清单应用安装配置文件
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="task-manager",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="一个基于tkintertools的任务清单管理应用",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/task-manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "tkintertools>=2.5.9",
    ],
    entry_points={
        "console_scripts": [
            "task-manager=main:main",
        ],
    },
    package_data={
        "": ["*.json", "*.ico"],
    },
    include_package_data=True,
)